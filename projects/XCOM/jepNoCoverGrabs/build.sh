#!/bin/bash
# Build jepNoCoverGrabs with the WOTC SDK, no ModBuddy. Staging path has no spaces
# (XComGame.com relaunches XComGame.exe and loses quoting).
set -u
S="/c/Program Files (x86)/Steam/steamapps/common/XCOM 2 War of the Chosen SDK"
M="/c/Users/jep/.claude/jobs/d60d4ae0/tmp/jepNoCoverGrabs"
T="/c/Users/jep/.claude/jobs/d60d4ae0/tmp"
rm -rf "$S/Development/Src/jepNoCoverGrabs"
cp -r "$M/Src/jepNoCoverGrabs" "$S/Development/Src/"
rm -rf "$T/stage"
mkdir -p "$T/stage"
cp -r "$M" "$T/stage/jepNoCoverGrabs"
STAGE_WIN='C:\Users\jep\.claude\jobs\d60d4ae0\tmp\stage\jepNoCoverGrabs'
cd "$S/Binaries/Win64"
./XComGame.com make -nopause -mods jepNoCoverGrabs "$STAGE_WIN" > "$T/make.log" 2>&1
echo "exit $?"
grep -v "Invalid property value\|Unresolved reference" "$T/make.log" | tail -n 12
grep -n "jepNoCoverGrabs" "$T/make.log" | head
ls -l "$S/XComGame/Script/" | grep -i jep
