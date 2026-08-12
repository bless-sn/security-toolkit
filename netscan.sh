#!/bin/bash
TARGET=${1:-127.0.0.1}
echo "Scanning $TARGET (own hosts only!)..."
nmap -sV -T4 "$TARGET" | tee scan-$TARGET.txt
