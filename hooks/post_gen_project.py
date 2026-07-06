#!/usr/bin/env python3
"""Post-generation hook: make scripts executable + print next steps."""

import os
import shutil
import stat


def make_scripts_executable():
    scripts_dir = "scripts"
    if not os.path.isdir(scripts_dir):
        return
    for name in os.listdir(scripts_dir):
        path = os.path.join(scripts_dir, name)
        if path.endswith(".sh") and os.path.isfile(path):
            st = os.stat(path)
            os.chmod(path, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print("✅ Made scripts/*.sh executable")


def check_tool(name, install_hint):
    if shutil.which(name):
        print(f"✅ Found: {name}")
        return True
    print(f"⚠️  Missing: {name} — {install_hint}")
    return False


def main():
    print("🚀 Setting up your Flatcar Marp slides project...")

    make_scripts_executable()

    print("\n🔍 Checking required tools...")
    check_tool("podman", "install 'podman' to use 'make build' / 'make setup'")
    check_tool(
        "node",
        "install Node.js (nodejs.org, or `dnf install nodejs npm` / `apt install nodejs npm` / `brew install node`) to use 'make native-build' / 'make watch'",
    )

    print("\n🎨 Flatcar theme lives at themes/flatcar.css (partials in themes/flatcar/).")
    print("   Slide layouts: <!-- _class: cover | lead | section | closing | agenda | sidebar | sidebar whoami | quote -->")
    print("   Full theme + utility reference: MANUAL.md")

    speaker_photo = "{{ cookiecutter.speaker_photo }}"
    maintainer = "{{ cookiecutter.maintainer }}"
    photo_dir = os.path.join("assets", "photo", "individual_photos")
    if maintainer == "Custom (bring your own)":
        print(
            f"\n🖼️  Add your portrait as {photo_dir}/speaker.jpg "
            "(the whoami slide references it)."
        )
        print(
            "   Maintainer photos are still shipped alongside — handy if you want to build a collage."
        )
    else:
        photo_path = os.path.join(photo_dir, speaker_photo)
        exists = "✅" if os.path.isfile(photo_path) else "⚠️  MISSING:"
        print(f"\n🖼️  {exists} whoami slide will use {photo_path} ({maintainer}).")
        print(
            "   All other maintainer photos remain in the folder — use them for a collage if you like."
        )

    print("\n📋 Next steps:")
    print("  cd {{ cookiecutter.project_slug }}")
    print("  make setup           # one-time container image build")
    print("  make build           # → build/slides.pdf")
    print("  make watch           # live rebuild while editing (needs npm ci first)")
    print("  make help            # show all targets")
    print("\n🎉 Happy presenting!")


if __name__ == "__main__":
    main()
