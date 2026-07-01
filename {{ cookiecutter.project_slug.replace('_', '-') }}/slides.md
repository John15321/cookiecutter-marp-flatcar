---
marp: true
theme: flatcar
paginate: true
size: 16:9
title: {{ cookiecutter.project_full_name }}
author: {{ cookiecutter.author_full_name }}
---

<!-- _class: cover -->
<!-- _paginate: false -->

# {{ cookiecutter.talk_title }}

{{ cookiecutter.author_full_name }}

---

<!-- _class: sidebar whoami -->

# whoami

<div class="bio-logos">
  <img src="assets/logos/icon/color/flatcar-icon-color.png" alt="Flatcar">
</div>

## {{ cookiecutter.author_full_name }}

Flatcar Maintainer

<img class="bio-photo" src="assets/photo/jan-bronicki.jpg" alt="{{ cookiecutter.author_full_name }}">

<p class="bio-github"><img src="assets/logos/external/github-white.png" alt="GitHub">@{{ cookiecutter.author_github_handle }}</p>

---

<!-- _class: agenda -->

# Agenda

- What is Flatcar Container Linux
- The UX philosophy
- Immutable by design
- A/B updates and channels
- Live demo
- Try it today

---

<!-- _class: section -->

# Part I
## What is Flatcar?

---

<!-- _class: sidebar -->

# Flatcar in one slide

- **Minimal, immutable Linux** built for running containers
- **Automatic atomic updates** — no in-place package upgrades
- **Runs anywhere** — bare metal, all major clouds, edge
- **CNCF Incubating project** since August 2024

---

<!-- _class: quote -->

> The operating system as an implementation detail.

- attributed to the CoreOS founders

---

## Default content slide

The unclassed slide uses a **white background** with a **navy title bar**
carrying the Flatcar logo. Use this for most of your content.

- Bullets get a cyan `::marker`
- Inline `code` gets a light grey pill
- **Bold** `**text**` stays ink-navy

```yaml
# Fenced code blocks get a cyan left rule
variant: flatcar
version: 1.0.0
```

---

<!-- _class: lead -->

# Lead slide

## Full-bleed navy — use for a single big statement.

---

<!-- _class: closing -->
<!-- _paginate: false -->

# Thank you!

<p class="closing-links">
  <a href="https://flatcar.org"><img src="assets/logos/icon/white/flatcar-icon-white.svg" alt=""> flatcar.org</a>
  <a href="https://github.com/flatcar"><img src="assets/logos/external/github-white.png" alt=""> github.com/flatcar</a>
  <a href="https://discord.gg/PMYjFUsJyq"><img src="assets/logos/external/discord-white.svg" alt=""> discord.gg/PMYjFUsJyq</a>
</p>

*Questions?*
