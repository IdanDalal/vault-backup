# Pay Attention v5: build waves (lead jep, 2026-11-18)

| wave | plates (brief) | builder | depends on |
|---|---|---|---|
| 1 | `_v5-film.ts` kit, then chorus1 (05) | v5-t1 | none |
| 1 | verse1 (02) | v5-t2 | kit for meter/context (add when the lead pings) |
| 1 | games (07) | v5-t3 | kit for meter/context |
| 2 | open (01) + outro (13): the receipt bookends | new builder | kit |
| 2 | class (03) + late (04) | new builder | kit; chorus1 for the ember seam |
| 2 | fact (06) | new builder | kit |
| 3 | chorus2 (08), chorus3 (12) | builder of chorus1 or a new one | kit diagram exports |
| 3 | kitchen (09) | new builder | kit |
| 3 | exam (10) + verse4 (11) | new builder | kit diagram exports, `_pa-fx.ts` fractal |

Gate per plate: sync check, deadarea, the builder's own sweeps, the lead's 8 fps read, a blind panel (stills among 40 reference stills), one fix round, then Idi on the decision page. Whole-film render with `VITE_PA_V5=1` after each wave (v3 plates fill the gaps).
Switch: engine commit 72f6455 (`timeline.ts`): `VITE_PA_V5=1` plays `scenes/v5-<module>.ts` where it exists.
