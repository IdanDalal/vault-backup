#!/bin/bash
# Refresh an installed jep script mod from the job folder and the SDK build. Usage: updatemod.sh <ModName>
set -eu
N="$1"
G="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/$N"
S="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2 War of the Chosen SDK"
T="/c/Users/jep/.claude/jobs/0815ca4d/tmp"
if tasklist | grep -qi "XCom2"; then echo "game running, stop"; exit 1; fi
[ -d "$G" ] || { echo "mod not installed, stop"; exit 1; }
cp "$S/XComGame/Script/$N.u" "$G/Script/"
cp -r "$T/$N/Config/." "$G/Config/"
cp -r "$T/$N/Src/." "$G/Src/"
cmp "$S/XComGame/Script/$N.u" "$G/Script/$N.u" && echo "script identical to build"
cmp "$T/$N/Config/XCom$N.ini" "$G/Config/XCom$N.ini" && echo "config identical"
ls -l "$G/Script" "$G/Config"
