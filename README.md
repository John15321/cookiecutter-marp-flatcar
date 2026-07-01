# 📑 Cookiecutter Marp Flatcar

A cookiecutter template that scaffolds a **single-deck** Flatcar Container Linux
Marp presentation. One talk = one repo, mirroring the layout of
[flatcar-presentation-devops-days](https://github.com/John15321/flatcar-presentation-devops-days)
exactly:

- `slides.md` at the repo root
- `themes/flatcar.css` + `themes/flatcar/{base,dark,sidebar}.css` — the real Flatcar theme with 9 slide layouts
- Podman + Make workflow, native Node.js fallback for CI
- GitHub Actions: PDF on every push, GitHub Release on `v*` tag
- Flatcar asset set: logos, backgrounds, staircases, photo, QR
- Closing slide auto-includes a QR code + **Join our Discord!** CTA

## Usage

```bash
cookiecutter gh:John15321/cookiecutter-marp-flatcar
cd <your-project-slug>
make setup        # one-time container image build
make build        # → build/slides.pdf
```

## Prompts

| Prompt                      | Purpose                                                         |
| --------------------------- | --------------------------------------------------------------- |
| `author_full_name`          | Author name (frontmatter + package.json + README footer)        |
| `author_email`              | package.json author email                                       |
| `author_github_handle`      | GitHub handle rendered on the whoami slide                      |
| `project_full_name`         | Human-readable talk name (README h1 + frontmatter title)        |
| `project_slug`              | Auto-derived directory name (kebab-case)                        |
| `project_short_description` | package.json + README description                               |
| `talk_title`                | The h1 shown on the cover slide (defaults to a Flatcar tagline) |

## Slide layouts (from the theme)

Applied via `<!-- _class: NAME -->` on any slide:

- *(none)* — white slide with navy title bar
- `cover` — navy title slide with Flatcar icon behind the title
- `lead` — navy full-bleed for a single statement
- `section` — section divider (cyan title + staircase artwork)
- `closing` — thank-you slide with QR code + "Join our Discord!" CTA
- `agenda` — 25 % navy rail + bullet list
- `sidebar` — 33 % navy rail + free-form right pane
- `sidebar whoami` — bio variant
- `quote` — blockquote slide with cyan opening quote mark

## After generation

```bash
make setup                  # first-time container image build (Podman)
make build                  # → build/slides.pdf
make clean                  # remove build/ and artifacts/
make watch                  # live-rebuild while editing (native, needs npm ci)
make preview                # live browser preview
make help                   # every target
```

Push a `v*` tag to publish a GitHub Release with the PDF attached.

