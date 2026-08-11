/* ============================================================================
   FMLG lead forms — conditional logic, validation, i18n, Smokeball payload,
   webhook POST, thank-you redirect.
   Webhook URL is read from window.ZAPIER_LEAD_WEBHOOK_URL (set per-page); when
   empty the form still validates and advances to the thank-you page so UX is
   never blocked while the Zap is being wired.
   ============================================================================ */
(function () {
  "use strict";

  /* ---------------- language toggle (smart form) ----------------
     The language bar, H1, and lede sit in the form wrapper OUTSIDE <form>, so
     translation operates on the whole wrapper; state is stamped on the form. */
  function applyLang(wrap, form, lang) {
    wrap.querySelectorAll("[data-es]").forEach(function (el) {
      if (el.dataset.en === undefined) el.dataset.en = el.innerHTML;
      el.innerHTML = lang === "es" ? el.dataset.es : el.dataset.en;
    });
    wrap.querySelectorAll("[data-es-ph]").forEach(function (el) {
      if (el.dataset.enPh === undefined) el.dataset.enPh = el.getAttribute("placeholder") || "";
      el.setAttribute("placeholder", lang === "es" ? el.dataset.esPh : el.dataset.enPh);
    });
    var hidden = form.querySelector('[data-role="language"]');
    if (hidden) hidden.value = lang === "es" ? "Español" : "English";
    var bar = wrap.querySelector(".fmlg-langbar");
    if (bar) bar.querySelectorAll("button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
    });
    form.setAttribute("data-lang", lang);
  }

  function initLang(form) {
    var wrap = form.closest(".fmlg-form-wrap") || form;
    var bar = wrap.querySelector(".fmlg-langbar");
    var params = new URLSearchParams(location.search);
    var start = params.get("lang") === "es" ? "es" : "en";
    if (bar) {
      bar.querySelectorAll("button").forEach(function (b) {
        b.addEventListener("click", function () { applyLang(wrap, form, b.dataset.lang); });
      });
    }
    if (wrap.querySelector("[data-es]") || bar) applyLang(wrap, form, start);
  }

  /* ---------------- service preset from URL / page ---------------- */
  function initPreset(form) {
    var params = new URLSearchParams(location.search);
    var svc = params.get("service");
    var sel = form.querySelector('[data-role="service"]');
    if (svc && sel) {
      var match = Array.prototype.find.call(sel.options, function (o) {
        return o.value.toLowerCase() === svc.toLowerCase();
      });
      if (match) {
        sel.value = match.value;
        var field = sel.closest(".fmlg-field");
        if (field) field.classList.add("hidden");
        sel.dispatchEvent(new Event("change", { bubbles: true }));
      }
    }
  }

  /* ---------------- conditional visibility ---------------- */
  function fieldValue(form, name) {
    var els = form.querySelectorAll('[name="' + CSS.escape(name) + '"]');
    if (!els.length) return "";
    if (els.length === 1 && els[0].type !== "checkbox" && els[0].type !== "radio")
      return els[0].value.trim();
    var checked = [];
    els.forEach(function (e) {
      if ((e.type === "checkbox" || e.type === "radio") && e.checked) checked.push(e.value);
      else if (e.type === "checkbox" && e.checked) checked.push(e.value);
    });
    if (els.length === 1 && els[0].type === "checkbox")
      return els[0].checked ? (els[0].dataset.yes || "Yes") : "No";
    return checked.join(", ");
  }

  function evalShowIf(form) {
    form.querySelectorAll("[data-showif]").forEach(function (wrap) {
      var rule;
      try { rule = JSON.parse(wrap.dataset.showif); } catch (e) { return; }
      var v = fieldValue(form, rule.field);
      var vals = (rule.in || []).map(String);
      var show = vals.some(function (x) { return v.split(", ").indexOf(x) !== -1 || v === x; });
      wrap.classList.toggle("hidden", !show);
      wrap.querySelectorAll("input,select,textarea").forEach(function (i) { i.disabled = !show; });
    });
  }

  /* ---------------- validation ---------------- */
  function setError(field, msg) {
    field.classList.add("invalid");
    var input = field.querySelector("input,select,textarea");
    if (input) input.setAttribute("aria-invalid", "true");
    var box = field.querySelector(".fmlg-error");
    if (box && msg) box.textContent = msg;
  }
  function clearError(field) {
    field.classList.remove("invalid");
    field.querySelectorAll('[aria-invalid]').forEach(function (i) { i.removeAttribute("aria-invalid"); });
  }

  function validate(form) {
    var firstBad = null;
    form.querySelectorAll(".fmlg-field").forEach(function (field) {
      clearError(field);
      if (field.classList.contains("hidden")) return;
      if (!field.dataset.required) return;
      var name = field.dataset.name;
      var v = fieldValue(form, name);
      var bad = false, msg = "This field is required.";
      if (!v) bad = true;
      if (!bad && field.dataset.type === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) {
        bad = true; msg = "Please enter a valid email address.";
      }
      if (bad) { setError(field, msg); if (!firstBad) firstBad = field; }
    });
    if (firstBad) {
      var f = firstBad.querySelector("input,select,textarea");
      if (f) f.focus();
      firstBad.scrollIntoView({ behavior: "smooth", block: "center" });
    }
    return !firstBad;
  }

  /* ---------------- payload composition (Smokeball Create Lead) ---------------- */
  function interp(tpl, form) {
    return (tpl || "").replace(/\{([^}]+)\}/g, function (_, name) {
      return fieldValue(form, name.trim()) || "—";
    });
  }

  function buildPayload(form) {
    var role = function (r) {
      var el = form.querySelector('[data-role="' + r + '"]');
      return el ? el.value.trim() : "";
    };
    var referralEl = form.querySelector('[data-role="referralType"]');
    return {
      firstName: role("firstName"),
      lastName: role("lastName"),
      email: role("email"),
      mobilePhoneNumber: role("phone"),
      contactType: "Person",
      location: "FL",
      matterTypeId: "Family - FL",
      isExistingClient: false,
      referralType: referralEl ? referralEl.value.trim() : (form.dataset.referral || "Website Form Inquiry"),
      description: interp(form.dataset.descTemplate, form),
      notes: interp(form.dataset.notesTemplate, form)
    };
  }

  /* ---------------- submit ---------------- */
  function go(form, paid) {
    var lang = form.getAttribute("data-lang") || "en";
    var url = (form.dataset.thankyou || "../thank-you/") +
      "?form=" + encodeURIComponent(form.dataset.formId || "") +
      "&paid=" + (paid ? "1" : "0") + "&lang=" + lang;
    location.assign(url);
  }

  function handleSubmit(form, e) {
    e.preventDefault();
    // LEAD 2 out-of-state gate
    if (form.dataset.stateGate) {
      var st = fieldValue(form, form.dataset.stateGate).toLowerCase();
      if (st && st !== "fl" && st !== "florida") {
        var block = form.querySelector(".fmlg-block");
        if (block) { block.style.display = "block"; block.scrollIntoView({ behavior: "smooth", block: "center" }); }
        return;
      }
    }
    if (!validate(form)) return;

    var payload = buildPayload(form);
    var paidField = form.querySelector('[data-role="consultation"]');
    var paid = paidField ? /paid|\$?250|attorney/i.test(fieldValue(form, paidField.name || "")) : false;
    // consultation may be a radio group named for role
    if (!paid) {
      var cons = fieldValue(form, "consultation");
      paid = /paid|250|attorney/i.test(cons);
    }

    var btn = form.querySelector(".fmlg-submit");
    if (btn) { btn.disabled = true; }

    var hook = window.ZAPIER_LEAD_WEBHOOK_URL || "";
    var done = function () { go(form, paid); };
    if (hook) {
      try {
        fetch(hook, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
          keepalive: true,
          mode: "no-cors"
        }).then(done, done);
        setTimeout(done, 1200); // fail-safe redirect
      } catch (err) { done(); }
    } else {
      if (window.console) console.warn("[FMLG] ZAPIER_LEAD_WEBHOOK_URL not set — payload not sent:", payload);
      done();
    }
  }

  /* ---------------- init ---------------- */
  function initAttribution(form) {
    var u = form.querySelector('[data-fill="url"]'); if (u) u.value = location.href;
    var ts = form.querySelector('[data-fill="ts"]'); if (ts) { try { ts.value = new Date().toISOString(); } catch (e) {} }
    var qp = new URLSearchParams(location.search);
    ["utm_source", "utm_campaign"].forEach(function (k) {
      var el = form.querySelector('[name="' + k + '"]');
      if (el && qp.get(k)) el.value = qp.get(k);
    });
    // auto-detect referral from utm_source (field 14 pre-fill)
    var src = qp.get("utm_source");
    var ref = form.querySelector('[data-role="referralType"]');
    if (src && ref && ref.tagName === "SELECT") {
      var m = Array.prototype.find.call(ref.options, function (o) {
        return o.value.toLowerCase() === src.toLowerCase();
      });
      if (m) ref.value = m.value;
    }
  }

  function initForm(form) {
    initLang(form);
    initPreset(form);
    initAttribution(form);
    evalShowIf(form);
    form.addEventListener("change", function () { evalShowIf(form); });
    form.addEventListener("input", function (ev) {
      var field = ev.target.closest(".fmlg-field");
      if (field && field.classList.contains("invalid")) clearError(field);
    });
    form.addEventListener("submit", function (e) { handleSubmit(form, e); });
  }

  /* ---------------- thank-you page ---------------- */
  function initThanks() {
    var t = document.querySelector(".fmlg-thanks");
    if (!t) return;
    var p = new URLSearchParams(location.search);
    if (p.get("paid") === "1") {
      var box = t.querySelector(".fmlg-paybox");
      if (box) box.style.display = "block";
    }
    if (p.get("lang") === "es") {
      t.querySelectorAll("[data-es]").forEach(function (el) { el.innerHTML = el.dataset.es; });
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form.fmlg-form").forEach(initForm);
    initThanks();
  });
})();
