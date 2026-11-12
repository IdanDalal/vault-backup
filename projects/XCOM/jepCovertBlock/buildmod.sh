#!/bin/bash
# Build a jep script mod with the WOTC SDK (recipe 09-26). Usage: buildmod.sh <ModName>
set -u
N="$1"
S="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2 War of the Chosen SDK"
T="/c/Users/jep/.claude/jobs/0815ca4d/tmp"
M="$T/$N"
rm -rf "$S/Development/Src/$N"
cp -r "$M/Src/$N" "$S/Development/Src/"
rm -rf "$T/stage"
mkdir -p "$T/stage"
cp -r "$M" "$T/stage/$N"
STAGE_WIN="C:\\Users\\jep\\.claude\\jobs\\0815ca4d\\tmp\\stage\\$N"
rm -f "$S/XComGame/Script/$N.u"
cd "$S/Binaries/Win64"
./XComGame.com make -nopause -mods "$N" "$STAGE_WIN" > "$T/make-$N.log" 2>&1
echo "exit $?"
grep -n -A4 -e "-- $N - Release" "$T/make-$N.log"
grep -E "Error|error\(s\)|Warning" "$T/make-$N.log" | grep -v "Warning/Error Summary" | tail -12
ls -l "$S/XComGame/Script/$N.u"
