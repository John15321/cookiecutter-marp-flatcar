# 📑 Cookiecutter Marp Flatcar

A cookiecutter template that scaffolds a **single-deck** Flatcar Container Linux
Marp presentation. One talk = one repo. It ships a full working intro-to-Flatcar
deck (whoami · community · provisioning · A/B updates · demo · thank-you) that
you can either present as-is or gut and rewrite — the theme, utilities, and
build pipeline stay the same.

- `slides.md` at the repo root, complete with a working set of intro slides
- `themes/flatcar.css` + `themes/flatcar/{base,dark,sidebar}.css` — the Flatcar
  theme with 9 slide layouts + utility classes (`img-*`, `pin-*`, `pane-*`,
  `row`, `cols-*`, `callout`, `logo-wall`, `ab-slide`, …)
- `MANUAL.md` — full authoring reference for the theme + utilities
- Podman + Make workflow, native Node.js fallback for CI
- GitHub Actions: PDF on every push, GitHub Release on `v*` tag
- Flatcar asset set: logotype, staircases, cloud/company logos, group photos, QR
- Closing slide auto-includes a QR code + **Join our Discord!** CTA

## Usage

```bash
cookiecutter gh:John15321/cookiecutter-marp-flatcar
cd <your-project-slug>
make setup        # one-time container image build
make build        # → build/slides.pdf
```

## Prompts

| Prompt                      | Purpose                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| `author_full_name`          | Speaker name (frontmatter + cover + whoami + README footer)        |
| `author_email`              | `package.json` author email                                        |
| `author_github_handle`      | GitHub handle rendered on the whoami slide                         |
| `author_role`               | First bio line on the whoami slide (e.g. "Flatcar Maintainer")     |
| `author_affiliation`        | Second bio line on the whoami slide (e.g. "Software Engineer @ …") |
| `project_full_name`         | Human-readable talk name (README h1)                               |
| `project_slug`              | Auto-derived directory name (kebab-case)                           |
| `project_short_description` | `package.json` + README description                                |
| `talk_title`                | The h1 shown on the cover slide                                    |
| `talk_subtitle`             | The h2 subtitle under the cover title                              |
| `demos_url`                 | URL shown on the "Demos!" slide                                    |

## After generation

Swap the speaker photo at `assets/photo/individual_photos/speaker.jpg` for your
own, then:

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

