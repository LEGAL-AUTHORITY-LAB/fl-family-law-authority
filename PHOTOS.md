# Photos — how to drop in the real headshots

The site is wired to use dedicated photo files **if they exist**, and to fall
back to placeholders until they do (see the `photo()` slots at the top of
`build.py`). To put the real shots in, upload files with these **exact names**
into `assets/images/`, then rebuild (`python3 build.py`) and commit.

| Upload this file | Used for | Best crop |
|---|---|---|
| `hero-duo.jpg`   | Homepage hero (both attorneys) | landscape, both of you, room on the left for text |
| `leisa.jpg`      | Leisa's team card + bio portrait | portrait / headshot |
| `nazarena.jpg`   | Nazarena's team card + bio portrait | portrait / headshot |
| `team-trio.jpg`  | Team page banner (Leisa · Nazarena · associate) | landscape group shot |

Until each file is present, the slot falls back to:
`hero-duo.jpg → team-laptop.jpg`, `leisa.jpg → portrait-seated-1.jpg`,
`nazarena.jpg → team-laptop.jpg`, `team-trio.jpg → (nothing rendered)`.

## Uploading from a browser (no command line)

1. In the repo, open the `assets/images` folder.
2. **Add file → Upload files.**
3. Drag/select the headshots, renamed to match the table above.
4. Commit to the working branch.
5. A maintainer re-runs `python3 build.py` (bakes the new filenames into every
   page) and commits — then the portraits appear everywhere automatically.
