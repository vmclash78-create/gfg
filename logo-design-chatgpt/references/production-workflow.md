# Production workflow

1. Brief: exact name, audience, positioning, restrictions and use cases.
2. Research: review category conventions and authorized references; extract principles, never copy artwork.
3. Divergence: draft 8–12 short ideas before selecting three genuinely different directions.
4. Build: create SVGs with explicit viewBox, deliberate geometry, negative space and verified lettering.
5. Audit: run python scripts/svg_audit.py concepts/*.svg. Its score is heuristic, not design approval.
6. Compare: run python scripts/preview_sheet.py concepts/*.svg -o review.html; open in a browser and inspect actual use cases.
7. Checkpoint: show three concepts, recommend one and wait for the user to choose or request changes.
8. Craft: refine geometry, kerning, optical alignment, small-size behavior and palette roles.
9. Export: create monochrome/reversed SVGs, render output sizes and inspect generated files.
10. Handoff: include source, previews, color values, typography/licensing notes, clear space, minimum size, misuse guidance and limitations.

## Automated checks vs design judgment

Scripts can catch malformed XML, missing viewBox, suspicious active content, external dependencies and excessive complexity. They cannot establish memorability, cultural appropriateness, strategic fit or legal clearance. Never describe a heuristic score as objective design quality or trademark clearance.

## Reference library

The bundled catalog is only a starter schema, not a 1,400-logo corpus. Add only assets you have rights to redistribute and record source, classification, license and attribution.
