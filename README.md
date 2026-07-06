# 📑 Cookiecutter Marp Flatcar

A cookiecutter template that scaffolds a **single-deck** Flatcar Container Linux
Marp presentation. One talk = one repo. It ships a full working intro-to-Flatcar
deck (whoami · community · provisioning · A/B updates · demo · thank-you) that
you can either present as-is or gut and rewrite — the theme, utilities, and
build pipeline stay the same.

|                                       |                                        |
| ------------------------------------- | -------------------------------------- |
| ![cover slide](preview/01-cover.png)  | ![agenda slide](preview/02-listing.png) |
| ![code slide](preview/03-code.png)    | ![closing slide](preview/04-closing.png) |

Full example rendered PDF: **[`preview/slides.pdf`](preview/slides.pdf)**
(24 slides, produced by `cookiecutter --no-input`). The same PDF also ships
inside every generated project at its root, next to `slides.md`, so you can
see the starting deck without running a build.

## Who is this for?

**Everyone who wants to talk about Flatcar.** You don't need to be a
maintainer to use this — the template is for the whole community. That said,
the deck ships a set of maintainer headshots (sourced from LinkedIn) because:

- Flatcar maintainers are usually the ones giving Flatcar talks, so their
  photo is one click away on the whoami slide (`maintainer` prompt).
- Anyone building a "meet the team" / community slide can grab the whole set
  from `assets/photo/individual_photos/` instead of hunting down each portrait.

If you're **not** a maintainer, pick `Custom (bring your own)` (or accept the
John Doe placeholder for a quick preview) and drop your own picture in.

## What you get

The generated deck is a **generic Flatcar 101** talk — cover, whoami, agenda,
community/CNCF, "runs everywhere", provisioning story, A/B updates diagram,
Butane example, demos + thank-you. You can present it as-is at a meetup, or
gut it and use it as scaffolding for your own talk.

It also doubles as a **showcase of what the template + Marp can do**: every
slide layout (`cover`, `lead`, `section`, `closing`, `agenda`, `sidebar`,
`sidebar whoami`, `quote`) plus most utility classes (`img-*`, `pin-*`,
`pane-*`, `row`, `cols-*`, `callout`, `logo-wall`, `ab-slide`, …) is used
somewhere in the deck — so before you rewrite it, skim it to see which
building blocks are available. Full reference in
[`MANUAL.md`](%7B%7B%20cookiecutter.project_slug.replace%28%27_%27%2C%20%27-%27%29%20%7D%7D/MANUAL.md).

## What's inside

- `slides.md` at the repo root, complete with a working set of intro slides
- `themes/flatcar.css` + `themes/flatcar/{base,dark,sidebar}.css` — the Flatcar
  theme with 9 slide layouts + utility classes (`img-*`, `pin-*`, `pane-*`,
  `row`, `cols-*`, `callout`, `logo-wall`, `ab-slide`, …)
- `MANUAL.md` — full authoring reference for the theme + utilities
- Podman + Make workflow, native Node.js fallback for CI
- GitHub Actions: PDF on every push, GitHub Release on `v*` tag
- Flatcar asset set: logotype, staircases, cloud/company logos, group photos, QR
- Maintainer photo set (LinkedIn-sourced) for whoami + team collages
- Closing slide auto-includes a QR code + **Join our Discord!** CTA

## Usage

```bash
cookiecutter gh:John15321/cookiecutter-marp-flatcar
cd <your-project-slug>
make setup        # one-time container image build
make build        # → build/slides.pdf
```

## Prompts

| Prompt                      | Purpose                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| `maintainer`                | Pick a Flatcar maintainer to auto-select their photo, "Custom" to bring your own, or accept the default John Doe placeholder |
| `author_full_name`          | Speaker name (frontmatter + cover + whoami + README footer)                                   |
| `author_email`              | `package.json` author email                                                                   |
| `author_github_handle`      | GitHub handle rendered on the whoami slide                                                    |
| `author_role`               | First bio line on the whoami slide (e.g. "Flatcar Maintainer")                                |
| `author_affiliation`        | Second bio line on the whoami slide (e.g. "Software Engineer @ …")                            |
| `project_full_name`         | Human-readable talk name (README h1)                                                          |
| `project_slug`              | Auto-derived directory name (kebab-case)                                                      |
| `project_short_description` | `package.json` + README description                                                           |
| `talk_title`                | The h1 shown on the cover slide                                                               |
| `talk_subtitle`             | The h2 subtitle under the cover title                                                         |
| `demos_url`                 | URL shown on the "Demos!" slide                                                               |

## After generation

If you picked a maintainer, their portrait is already wired into the whoami
slide. If you picked "Custom", drop your portrait at
`assets/photo/individual_photos/speaker.jpg`. The default is a John Doe
placeholder — fine for a quick preview, swap it out before you present.
Either way, all shipped maintainer photos stay in that folder — handy if
you want to build a collage of the team.

```bash
make setup                  # first-time container image build (Podman)
make build                  # → build/slides.pdf
make clean                  # remove build/ and artifacts/
make watch                  # live-rebuild while editing (native, needs npm ci)
make preview                # live browser preview
make help                   # every target
```

See [`MANUAL.md`](%7B%7B%20cookiecutter.project_slug.replace%28%27_%27%2C%20%27-%27%29%20%7D%7D/MANUAL.md)
inside the generated project for the authoring reference (slide layouts,
utility classes, both HTML-class and markdown-alt-text syntaxes).

Push a `v*` tag to publish a GitHub Release with the PDF attached.

