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

**Screenshot round 1** (`D:\work\screens\Workshop.png`, 15:57):

- Seen working: pure black background, purple accent and links, underline sidebar tabs, vault name on top, normal status bar, hidden ribbon and folded tab bar (his focus-mode and ribbon settings), the re-laid canvas with all 7 paused cards and all 14 Morning rows.
- The `Workshop` layout was not loaded: Obsidian was still on the earlier layout, board and Whiteboard as two tabs in one group, file sidebar open. The ribbon icon that loads layouts is hidden by his own ribbon style until hovered. jep tried writing the `Workshop` layout into the live `workspace.json` at 16:01:58; the running app saved its own layout back over it at 16:02:00. That file belongs to the running app and is left alone from here on (the earlier layout is also kept as `projects/workshop/tools/obsidian-look/workspace-before-2026-11-11.json`). The route that works: Ctrl+P → "Load workspace layout" → `Workshop`.
- The canvas controls sat on the window's close button, because the folded tab bar lets the canvas reach the top edge. Fixed in part 4 of the snippet.
- The check card showed its properties block. Part 4 hides properties and the repeated title on canvas note cards.
- Unseen still: the `Workshop` layout itself, the two part 4 rules, his three older layouts.

**Screenshot round 2** (`D:\work\screens\Layout.png`, 16:15), after Idi loaded `Workshop` and stretched the cards by hand to fill the pane:

- Seen working: the `Workshop` layout (board 76 %, Whiteboard 24 %, sidebars folded); the canvas controls clear of the window buttons; the repeated title gone from the check card.
- Not working: the properties block still showed on the check card. A plain `display: none` loses to Obsidian's own rule. Part 4 now sets Obsidian's two properties-display variables on canvas cards and forces the rule.
- Measured: the canvas pane shows 2634 by 1905 canvas units at his zoom, aspect 1.382, taller than the shape jep had designed for. His stretched version left the lower third of the Board empty and cut the last Morning row.
- Canvas layout v3 (`tools/obsidian-look/canvas_v3.py`), built for that shape: the three tables stacked on the left (Now 270, Matrix 410, Morning 570 units tall), check and jar side by side under them, the Board down the right edge at full height. Canvas 2032 by 1470 units; zoom-to-fit comes to about 0.80 against 0.63 before, so text is about 27 % larger.
- The price: the canvas Board shows two columns, active and paused. The empty done and archived columns took half its width. All four columns remain on `Workshop.md`.
- The check note's verdict is one line shorter.
- Unseen: layout v3 and the properties fix.

**Known gaps:** fidelity to the old look is unmeasured against a picture of the old look (none exists here); the canvas zoom in `Workshop` (stored as -0.66) was computed for a 2194 px wide window at 175 % scaling and may need Shift+1 once.
