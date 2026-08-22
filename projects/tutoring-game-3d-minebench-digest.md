---
type: reference
created: 2026-08-22
author: jep
project: tutoring
status: done
---

# MC-Bench / MineBench craft digest — voxel-scene composition for the island

Agent research 2026-08-22 (Idan's find, playtest-3 note 4). Companion: [[tutoring-game-3d-playtest1]].

**The benchmarks:** MC-Bench (mcbench.ai, Adi Singh + volunteers; models write Python executed by a mineflayer bot on a real MC server; blind pairwise Elo voting). MineBench (minebench.ai, Ammaar Alam; JSON/JS `voxel_exec` with only block/box/line/rng primitives; top board GPT-5 2150 / Claude 4.5 2108 / Gemini 3 Pro 2091). Meta FAIR VoxelCodeBench (arXiv 2604.02580) is the academic sibling. Scoring rewards prompt adherence + composition, never block count.

**Winning-craft laws** (mostly from MineBench's own system prompt, `lib/ai/prompts.ts`):
1. Hierarchical build order: primary mass/silhouette → secondary elements → tertiary detail/atmosphere.
2. Concentrate detail at focal areas (silhouette edges, openings, joints); calm interiors.
3. Three named failure modes: flat decoration (paint on a box), visible primitives (box-on-box reads instantly), static isolation (subject floats without environment/base/context).
4. Multi-angle legibility — judges rotate; blank backsides lose.
5. Environment + narrative valued: paths, docks, chimneys, tree framing (canonical winning scene: cabin + pond + dock + trees).
6. Material families with accent discipline: 2 family materials + 1 accent per structure, one global accent (glow) recurring everywhere; dither sister-blocks into faces >5×5.
7. Intentionality beats volume; plan first.
8. Depth over paint: recesses, overhangs, sills.
9. Light sources are compositional accents.

**APPLIED to island.html same day (sess-4 village redesign):** domain-warped coastline (crescent coves); lighthouse moved to its own SE headland (two verticals on a diagonal with the peak), rebuilt as compound mass (stone plinth → striped shaft → plank gallery → lamp room → keeper's hut with porch lamp); dock of planks on log piles with tip lamp; plaza = stone pavers with dithered path accents + low fence ring with 4 path gaps + 4 corner lamp posts; S-curved 2-wide paths plaza→cove/garden/lighthouse/cave; garden relocated to its own west zone with corner posts + lamps; story cove = fixed flattened sandy pad with 3 lamp posts at 120°; furniture spread (table west, board north, shelf east). New block ids 12 path / 13 plank. 4-angle+top render audit adopted as ritual.

**QUEUED:** foundation skirts under bench/board/shelf; switchback path up the peak with fence-lamp pairs; framed cave-mouth arch; terraced garden retaining walls; plaza center focal object (well/flag).
