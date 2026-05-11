# Homepage Redesign — Design

**Date:** 2026-05-11
**Scope:** CV + Publications redesign with light cross-page polish

## Motivation

The current FastHTML + MonsterUI homepage renders CV entries, publications, and talks as `Card` components. The visual treatment feels cluttered. The goal is to replace these card-style components with simple plain bulleted lists and apply small cross-page consistency tweaks.

Stack stays the same (FastHTML + MonsterUI, Theme.blue light mode, static GitHub Pages build). Page structure (sidebar + main grid) and routing are unchanged.

## Visual direction

Simple plain text with bullet points. No card backgrounds, no chip tags, no leading icons on list items. Title bold, journal italic, own name underlined in publication authors. Standard `list-disc` bullets with consistent vertical rhythm.

## File-level changes

| File | Change |
|------|--------|
| `src/home.py` | Rename `cv_timeline_item` → `cv_entry`. Returns `Li` instead of `Card`. Wrap CV entries in one `Ul`. Drop the interest-chips block (Large Language Models / Machine Learning / Healthcare / Biophysics / Statistical Physics) at the end of About. CV content update for consistency with the About paragraph: add a new top entry "Feb 2026 – present, Solutions Architect, NVIDIA"; change the Tech Lead and Researcher PFN entries' end dates from "present" to "Feb 2026". |
| `src/publications.py` | `publication_item` returns `Li` instead of `Card`. Drop the `labels` parameter and chip rendering. Underline "Junichiro Iwasawa" inside the authors string. Wrap items in one `Ul`. |
| `src/talks.py` | `presentation_item` returns `Li` instead of `Card`. Drop the calendar icon. Each subsection's items wrapped in its own `Ul`. Japanese title (when present) on its own line under the English title. |
| `src/sidebar.py` | Update affiliation: "Researcher at Preferred Networks Inc." → "Solutions Architect at NVIDIA". Remove the email line entirely. Icon-prefixed social links stay as-is. |
| `src/research.py` | **No change.** Already uses plain markup. |
| `main.py`, `build_static.py` | **No change.** |

## Component shapes

**CV entry** — `cv_entry(period, title, institution)`:
```
<li><strong>{period}.</strong> {title}, {institution}.</li>
```

**Publication entry** — `publication_item(authors, title, journal, link)`:
```
<li>
  {authors with own name <u>underlined</u>}.
  <strong>{title}.</strong>
  <em>{journal}.</em>
  <a href="{link}">[link]</a>
</li>
```

**Talk entry** — `presentation_item(title, title_jp, venue, date, location, venue_link)`:
```
<li>
  <strong>{title}</strong>
  [<br>{title_jp}]
  <br>{venue}, {date}[, {location}].
  [<a href="{venue_link}">[link]</a>]
</li>
```

All lists use `<ul class="list-disc pl-5 space-y-2">` for consistent rhythm.

## Cross-page polish

1. Every top-level `Section` uses `mb-12` (currently mixed `mb-8`/`mb-12`).
2. Section `H2` headings use `mb-4` consistently; subsection `H3` uses `mb-4` as well.
3. No new colors, fonts, dark mode, or layout changes. Blue accent, profile photo, container width, navbar all unchanged.

## Out of scope

- Replatform (stays FastHTML + MonsterUI)
- Dark mode
- New pages or content rewrites (About paragraphs unchanged; CV gets a single NVIDIA entry + PFN end-date fix, nothing else)
- Sidebar restructure (icons stay)
- Research page layout (already plain)

## Testing

Run `python build_static.py` to confirm all five routes (`/`, `/publications`, `/research`, `/talks`, `/blog`) generate without errors. Spot-check the generated HTML in `_site/` and load the dev server (`python main.py`) to view each page in the browser.
