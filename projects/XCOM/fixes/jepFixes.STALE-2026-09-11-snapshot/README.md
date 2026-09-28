---
type: reference
created: 2026-09-11
author: jep
---

# jepFixes: config-only fix mod

Install: copy the `jepFixes` folder to `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\jepFixes\` (create `Mods` if absent).
Launcher: the local Mods path must be listed under the launcher's mod paths (it was until March 2026; the August database lists the workshop path only). jep re-adds it in `settings.json` on the word, with the launcher closed.
Verify: after the next launch, `Launch.log` should drop from about 1,912 redscreen lines to about 720, and the six Mandalorian helmets plus two Demolisher leg decos should appear in the customizer.

## Entries fixed

- Mandalorians of the Old Republic 2376020557
  - before: `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_MercilessSeeker_M", ArchetypeName="...`
  - after:  `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_MercilessSeeker_M", ArchetypeName="...`
- Mandalorians of the Old Republic 2376020557
  - before: `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_MercilessSeeker_F", ArchetypeName="...`
  - after:  `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_MercilessSeeker_F", ArchetypeName="...`
- Mandalorians of the Old Republic 2376020557
  - before: `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_Shae_M", ArchetypeName="MotOR_Asset...`
  - after:  `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_Shae_M", ArchetypeName="MotOR_Asset...`
- Mandalorians of the Old Republic 2376020557
  - before: `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_ShaeCommander_M", ArchetypeName="Mo...`
  - after:  `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_ShaeCommander_M", ArchetypeName="Mo...`
- Mandalorians of the Old Republic 2376020557
  - before: `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_Shae_F", ArchetypeName="MotOR_Asset...`
  - after:  `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_Shae_F", ArchetypeName="MotOR_Asset...`
- Mandalorians of the Old Republic 2376020557
  - before: `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_ShaeCommander_F", ArchetypeName="Mo...`
  - after:  `+BodyPartTemplateConfig=(DLCName="OldRepublic_MandalorianArmor", PartType="Helmets", TemplateName="ORMandos_Helmet_ShaeCommander_F", ArchetypeName="Mo...`
- Mass Effect Multiplayer Armour Pack 2010492838
  - before: `+BodyPartTemplateConfig=(PartType="Thighs",DLCName="MassEffectMultiplayerPack",TemplateName="HPT_DemolisherLegsDeco", ArchetypeName="Demolisher.ARC_Le...`
  - after:  `+BodyPartTemplateConfig=(PartType="Thighs",DLCName="MassEffectMultiplayerPack",TemplateName="HPT_DemolisherLegsDeco", ArchetypeName="Demolisher.ARC_Le...`
- Mass Effect Multiplayer Armour Pack 2010492838
  - before: `+BodyPartTemplateConfig=(PartType="Thighs",DLCName="MassEffectMultiplayerPack",TemplateName="HPT_DemolisherLegsDeco_M", ArchetypeName="Demolisher.ARC_...`
  - after:  `+BodyPartTemplateConfig=(PartType="Thighs",DLCName="MassEffectMultiplayerPack",TemplateName="HPT_DemolisherLegsDeco_M", ArchetypeName="Demolisher.ARC_...`
