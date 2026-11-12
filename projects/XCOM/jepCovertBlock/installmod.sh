#!/bin/bash
# Install a built jep script mod into the game's local Mods dir and register it in AML. Usage: installmod.sh <ModName> "<description>"
set -eu
N="$1"; D="$2"
G="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/$N"
S="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2 War of the Chosen SDK"
T="/c/Users/jep/.claude/jobs/0815ca4d/tmp"
if tasklist | grep -qi "XCom2\|AlternativeModLauncher\|XCOM2 Mod Launcher"; then echo "game or launcher running, stop"; exit 1; fi
[ -e "$G" ] && { echo "target exists, stop"; exit 1; }
mkdir -p "$G/Script"
cp -r "$T/$N/Config" "$T/$N/Src" "$T/$N/$N.XComMod" "$G/"
cp "$S/XComGame/Script/$N.u" "$G/Script/"
find "$G" -type f | sed "s#$G/##"
cp "/c/XCOM2 AML 1.6.0-beta/settings.json" "$T/settings.json.bak-$N"
cp "/c/XCOM2 AML 1.6.0-beta/settings.json" "/d/work/aml-settings-2026-11-12.json"
python "D:/work/vault/projects/XCOM/jepReusePCS/aml_add.py" "$N" "$D"
python "D:/work/vault/projects/XCOM/jepClassWeights/amlverify.py" "$T/settings.json.bak-$N" "$N"
