/* FMLG site interactions: header state, mobile nav, hero load-in, scroll reveal */
(function () {
  'use strict';

  // Header solid-on-scroll
  var header = document.getElementById('siteHeader');
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 40);
  }
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile nav
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // Dropdown menus (mobile tap to expand; desktop uses hover via CSS)
  document.querySelectorAll('.has-menu > .menu-btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (window.innerWidth > 940) return; // desktop = hover
      e.preventDefault();
      var parent = btn.parentElement;
      var wasOpen = parent.classList.contains('open');
      document.querySelectorAll('.has-menu.open').forEach(function (m) { m.classList.remove('open'); });
      if (!wasOpen) parent.classList.add('open');
    });
  });

  // Hero load-in
  window.addEventListener('DOMContentLoaded', function () {
    var chev = document.getElementById('heroChevrons');
    if (chev) chev.classList.add('run');
    document.querySelectorAll('.hero h1 .cut').forEach(function (el, i) {
      setTimeout(function () { el.classList.add('in'); }, 220 + i * 120);
    });
    var sub = document.getElementById('heroSub');
    if (sub) setTimeout(function () { sub.classList.add('in'); }, 220 + 4 * 120);
  });

  // Scroll reveal
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }
})();
