---
marp: true
theme: flatcar
paginate: true
size: 16:9
title: "{{ cookiecutter.talk_title }}"
author: {{ cookiecutter.author_full_name }}
---

<!-- _class: cover -->
<!-- _paginate: false -->

# {{ cookiecutter.talk_title }}

## {{ cookiecutter.talk_subtitle }}

##### {{ cookiecutter.author_full_name }}

---

<!-- _class: sidebar whoami -->

# whoami

<div class="pin-tr" style="display: flex; gap: 20px; align-items: center">
  <img class="img-h-xs" src="./assets/logos/external/flatcar-logo-other.png" alt="Flatcar">
</div>


## {{ cookiecutter.author_full_name }}

{{ cookiecutter.author_role }}

{{ cookiecutter.author_affiliation }}

{%- set _photo_overrides = {'Custom (bring your own)': 'speaker.jpg', 'John Doe (placeholder)': 'john-doe-example.png', 'Jeremi Piotrowski': 'jeremi-piotrowski.jpg', 'Thilo Fromm': 'thilo-fromm.png'} %}
{%- set _speaker_photo = _photo_overrides.get(cookiecutter.maintainer, cookiecutter.maintainer.lower().replace(' ', '-') + '.jpeg') %}
<img class="bio-photo" style="--bio-photo-size: 320px; top: 180px" src="assets/photo/individual_photos/{{ _speaker_photo }}" alt="{{ cookiecutter.author_full_name }}">

<p class="bio-github"><img src="assets/logos/external/github-white.png" alt="GitHub">@{{ cookiecutter.author_github_handle }}</p>

---

<!-- _class: agenda -->

# Agenda

- First topic
- Second topic
- Third topic
- Live demo

---

<!-- _class: section -->

# Section divider

## Use this to break your talk into chapters

---

<!-- Default content slide. Available layouts (set via `<!-- _class: ... -->` at the top of a slide):
     cover | lead | section | closing | agenda | sidebar | sidebar whoami | quote
     See MANUAL.md for the full theme + utility reference. -->

# Your first slide

- Replace this content with your own
- See `MANUAL.md` for layouts, utilities, and asset conventions
- Drop images into `assets/` and reference them with relative paths

---

<!-- _class: closing -->
<!-- _paginate: false -->

# Thank you!

<p class="closing-qr-caption"><img src="assets/logos/external/discord-white.svg" alt=""> Join our Discord!</p>

<p class="closing-links">
  <a href="https://flatcar.org"><img src="assets/logos/flatcar-logotype/icon/white/flatcar-icon-white.svg" alt=""> flatcar.org</a>
  <a href="https://github.com/flatcar"><img src="assets/logos/external/github-white.png" alt=""> github.com/flatcar</a>
  <a href="https://discord.gg/PMYjFUsJyq"><img src="assets/logos/external/discord-white.svg" alt=""> discord.gg/PMYjFUsJyq</a>
</p>

<p class="closing-meetings">
  <span><strong>Office hours</strong> · every 2nd Tue, 16:30 CEST</span>
  <span><strong>Dev sync</strong> · every 4th Tue, 16:30 CEST</span>
</p>

<p class="closing-cta"><strong>Everyone welcome.</strong> Users, contributors, or just curious. Ask questions, get help, share what you're building!</p>
