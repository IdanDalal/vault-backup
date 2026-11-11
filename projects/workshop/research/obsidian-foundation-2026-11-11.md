---
type: research
created: 2026-11-11
author: jep
project: workshop
---

# Idi's hand-made Obsidian look: where it is and what it is

Read-only sweep of every Obsidian config folder jep can reach, 2026-11-11. Idi's words: "custom hand-made layouts/workspaces/themes with a true/pure black background... and pixel-perfect 'tabs'/'rectangles'/'parts'".

## 1. Found

Ten config folders under `D:\work`. Four hold saved workspaces; three of those are the same setup copied between vaults.

| Config folder (under `D:\work\laptop-archive\CORPUS-June-2026\`) | Workspaces | Theme | Plugins | Note |
|---|--:|---|--:|---|
| `Vaults BACKUPS\Idiverse` | 3 | Minimal, black | 32 | **The foundation.** Same workspaces and colours as the next two |
| `NEXUS BACKUP` | 3 | Minimal, black | 31 | Copy of the Idiverse setup |
| `Vaults BACKUPS\Curtains` | 3 | Minimal, black | 38 | Copy, plus one snippet `properties-layout.css` and font size 15 |
| `Vaults BACKUPS\TemporarilyTitleless` | 2 | Minimal, black | 15 | A variant: narrower line width, an `h1` colour |
| `Vaults BACKUPS\jep`, `_forks\NEXUS-Idiverse` | 0 | Minimal | 3, 2 | Theme only |
| three others, `D:\work\captures`, `D:\work\vault` | 0 | default | 0 to 3 | Bare |

Not readable by jep: `C:\Users\Idi` and the closed `D:\` folders. If a newer hand-made layout lives there, it is not in this file.

## 2. The three workspaces

Names carry their own measurements: `400 Width 500 Height 1317 Notes`, `500 Width 500 Height 2333 Note`, `1417 Notes`.

- **`1417 Notes`**: two note columns of 42.5 % each, then a 15 % column of four small panels stacked top to bottom: graph, local graph, bookmarks beside all-properties, calendar. Left sidebar 251 px with files, recent files, search, tags. Right sidebar collapsed.
- **`400 Width 500 Height 1317 Notes`**: two note columns of 38.4 % each, then a 23.3 % column of eight small panels in a grid: local graph and graph; outgoing links and backlinks; all-properties and bookmarks; outline and calendar. Left sidebar 200 px.
- **`500 Width 500 Height 2333 Note`**: one note column, the same panel grid.

Two panel kinds come from plugins: `calendar` (Calendar) and `recent-files` (Recent Files). Everything else is core Obsidian.

## 3. The look

Minimal theme (`themes\Minimal\theme.css`, 274 KB of CSS), dark scheme `minimal-dark-black`, set through two plugins: Minimal Theme Settings and Style Settings (about 90 values). The ones that define it:

| What | Value |
|---|---|
| Base, frame, background | `#000000` |
| Accent, tags, checkboxes, row hover | `#623DB7` |
| Links, titles | `#8B5CF6` |
| Body text | `#727272`; bold, H2, highlights `#CACACA`; H1 `#FEFEFE` |
| UI lines | `#272727` |
| External links | `#00FFFF`; unresolved links `#FF0000` at half opacity |
| Tabs | underline style, active tab text `#FFFFFF`, header height 40 px |
| Tables | row, column and outer lines on; tabular numbers; hover row in accent |
| Text | 13 px (15 px in two variants), line height 1.5, line numbers on |
| Sidebar | tab names off, underline tabs, ribbon expands vertically |

## 4. Rebuilding it in `D:\work\vault`, once Obsidian's config opens to jep

Nothing here needs plugin code.

1. Copy the Minimal theme (two files, CSS and a manifest) into the vault's config.
2. One CSS snippet that sets the black scheme and the values of section 3 directly, in place of the two settings plugins.
3. `workspaces.json`: his three layouts with today's files in the note columns, plus `Workshop` (Board.canvas beside the Whiteboard). The calendar and recent-files panels are left out unless he installs those two plugins himself.
4. Core plugin Workspaces switched on; `appearance.json` pointed at the theme and the snippet.
5. Idi reloads Obsidian and sends a screenshot; jep measures it against section 3 and corrects.

Step 2 is a translation of 90 settings into CSS and will need at least one screenshot round. The exact alternative is his hand: install Minimal Theme Settings and Style Settings from Obsidian's own plugin browser and import his old values.

## 5. Built, 2026-11-11 (after Idi opened the config to jep, plugin code excepted)

**Unverified:** nothing of this has been seen rendered.

| Installed in `D:\work\vault\.obsidian\` | What it is |
|---|---|
| `themes\Minimal\theme.css`, `manifest.json` | Minimal 9.1.4, fetched from the official repository (kepano/obsidian-minimal on GitHub). The archived copy was 7.7.7 from 2024; 9.1.4 asks for Obsidian 1.14.0 or later |
| `snippets\idi-black.css` | 28 KB, generated. Part 1: 113 theme rules his two settings plugins used to switch on, rewritten to apply always. Part 2: 61 variables, his colours and sizes. Part 3: two theme defaults the plugins used to switch off |
| `snippets\properties-layout.css` | His own snippet from the Curtains config, unchanged |
| `appearance.json` | Theme Minimal, accent `#8a5cf4`, text 15 px, view header hidden, both snippets on (his Curtains values). Before: `{"theme": "obsidian"}` |
| `workspaces.json` | His three layouts plus `Workshop` |

What the translation did with his 90 stored values:

- 88 found in Minimal 9.1.4. Two dropped: `styled-scrollbars` (retired upstream) and a size for the Note Toolbar plugin.
- 44 switches reproduced (pure black scheme, underline tabs in main area and sidebars, table lines, row hover, coloured headings, focus mode, normal status bar, and the rest). 13 of them have no rule in this theme version and do nothing.
- 41 theme selectors apply only when one of his switches is absent. Each was read; two made a visible difference and are overridden in part 3 (finished checklist items, the active tab in Settings). The others resolve to black either way or belong to schemes he never used.
- In his three layouts, the calendar panel became backlinks or tags and the recent-files tab became bookmarks, because those two panels come from plugins.

Checks done: the snippet parses with 0 errors; all four layouts use core panels only and every file they open exists; installed files hash-identical to the staged ones; `plugins\` and `community-plugins.json` untouched.

**Rebuild or change it:** `projects/workshop/tools/obsidian-look/build_black.py` (snippet) and `build_layouts.py` (layouts). Inputs are the archived Curtains values and a fresh `theme.css`.

**Roll back:** Settings → Appearance → Themes → Default, and switch the two snippets off. Or jep restores `appearance.json` to `{"theme": "obsidian"}`.

**Known gaps:** fidelity to the old look is unmeasured until a screenshot exists; the canvas zoom in `Workshop` (stored as -0.66) was computed for a 2194 px wide window at 175 % scaling and may need Shift+1 once.
