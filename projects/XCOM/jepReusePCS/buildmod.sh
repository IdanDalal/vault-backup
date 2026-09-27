#!/bin/bash
# Build a jep script mod with the WOTC SDK, no ModBuddy.  Usage: buildmod.sh <ModName>
# Recipe (09-26): Development/Src = SrcOrig backdated; staging path without spaces;
# mod ships Config/XComEditor.ini +ModPackages and XComEngine.ini +NonNativePackages; no -unattended.
set -u
N="$1"
S="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2 War of the Chosen SDK"
T="/c/Users/jep/.claude/jobs/d60d4ae0/tmp"
M="$T/$N"
rm -rf "$S/Development/Src/$N"
cp -r "$M/Src/$N" "$S/Development/Src/"
rm -rf "$T/stage"
mkdir -p "$T/stage"
cp -r "$M" "$T/stage/$N"
STAGE_WIN="C:\\Users\\jep\\.claude\\jobs\\d60d4ae0\\tmp\\stage\\$N"
cd "$S/Binaries/Win64"
./XComGame.com make -nopause -mods "$N" "$STAGE_WIN" > "$T/make-$N.log" 2>&1
echo "exit $?"
grep -n -A4 -e "-- $N - Release" "$T/make-$N.log"
grep -E "Error|error\(s\)" "$T/make-$N.log" | grep -v "Warning/Error Summary" | tail -5
ls -l "$S/XComGame/Script/$N.u"
