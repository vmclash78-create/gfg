# Logo Design for ChatGPT and compatible coding agents

A practical logo-design toolkit with reusable instructions, Python utilities, a starter reference catalog, tests and GitHub Actions CI.

## Features
- Design workflow with a concept approval checkpoint.
- SVG structural audit with heuristic warnings.
- Standalone HTML preview sheet for size, monochrome, reversed, squint and mirror checks.
- SVG-to-PNG rendering via optional CairoSVG or Inkscape.
- Monochrome/reversed SVG variant generator and web manifest scaffold.
- Searchable local JSON metadata catalog.
- Unit tests and GitHub Actions workflow.

## Quick start

Run from the logo-design-chatgpt directory:

    python scripts/svg_audit.py path/to/logo.svg
    python scripts/preview_sheet.py path/to/a.svg path/to/b.svg -o review.html
    python scripts/export_variants.py path/to/logo.svg --mono "#111111" --reverse "#ffffff"
    python scripts/search_library.py "negative space" --catalog assets/library/catalog.json
    python -m unittest discover -s tests -v

PNG rendering requires CairoSVG (python -m pip install cairosvg) or Inkscape:

    python scripts/render_png.py path/to/logo.svg --size 512 -o logo.png

## Use in ChatGPT

Copy skills/logo-design/SKILL.md or the main SKILL.md into a ChatGPT Project or custom GPT instructions. GitHub storage does not automatically activate a skill in the ChatGPT mobile app. Coding agents that support the Agent Skills format can use the portable folder in skills/logo-design, subject to their installation conventions.

## Honest scope and limitations

This is a functional starter toolkit, not yet feature-parity with the upstream project. The local catalog is only a schema with two original descriptive entries; it does not include the upstream library of 1,400+ real logos. The scripts provide basic checks and helpers, not the upstream's full geometric analysis, industry mockup engine, complete icon export pipeline or reference corpus. PNG/ICO export and web manifest files must be verified before production.

## Reference and licensing

Inspired by https://github.com/kaankiziltug/logo-design-skill. This adaptation does not copy that project's logo corpus or claim ownership of third-party marks. Review the original project's license and trademark notices before reusing upstream code or assets.
