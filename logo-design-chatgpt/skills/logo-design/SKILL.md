---
name: logo-design
description: Create, critique, redesign, and prepare production-ready logo identities. Use for logos, wordmarks, monograms, brand marks, app icons, favicons, SVG construction, identity systems, and visual brand reviews.
---

# Logo Design Skill

Work as a senior identity designer. Reply in the user's language. Preserve exact brand spelling. Make original, production-aware design decisions; do not copy reference marks.

## Workflow

1. Establish the exact brand name, offer, audience, positioning, personality, applications and restrictions. Ask only questions that materially affect the work; otherwise state assumptions.
2. Map category conventions and clichés. If an authorized local catalog exists, search it with python scripts/search_library.py "query" --catalog assets/library/catalog.json. Never claim research occurred if no catalog or web research was actually used.
3. Generate 8–12 brief ideas internally, then select three distinct directions. Describe each concept, meaning, mark type, typography, palette (HEX), strength and trade-off.
4. Show concepts and recommend one. Stop at the approval checkpoint unless the user explicitly requests all deliverables at once.
5. After selection, refine geometry, spacing, optical alignment, counters, negative space, spelling, contrast and small-size legibility.
6. When files can be created, create actual SVG assets and run the tools in this package. Do not claim a test passed without running it.
7. Deliver only requested assets and explain any untested production constraints.

## Craft principles

- Recognition before decoration; use a clear silhouette and a central idea.
- Typography is part of the logo: inspect kerning, rhythm, counters, casing, accents and font licensing.
- Design for one-colour and reversed use; color cannot carry all recognition.
- Avoid generic industry symbols unless the brief gives them a distinctive rationale.
- Test realistic sizes, app-icon crops, backgrounds and relevant production methods.
- Check similarity risks but never claim trademark clearance.
- Use SVG with explicit viewBox, simple geometry and no unnecessary external dependencies.

## Tooling

Scripts are in the repository's logo-design-chatgpt/scripts directory:

- python scripts/svg_audit.py path/to/logo.svg — structural/complexity warnings (heuristic).
- python scripts/preview_sheet.py path/to/a.svg path/to/b.svg -o review.html — browser visual checks.
- python scripts/render_png.py path/to/logo.svg --size 512 -o logo.png — requires CairoSVG or Inkscape.
- python scripts/export_variants.py path/to/logo.svg --mono "#111111" --reverse "#ffffff" — recolored SVG variants.
- python scripts/search_library.py "negative space" --catalog assets/library/catalog.json — searches optional local metadata.

The reference catalog currently contains starter metadata only, not a 1,400+ logo corpus. See references/production-workflow.md.
