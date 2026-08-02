#!/bin/bash
echo "User: $(whoami) Host: $(hostname)"
ps aux --sort=-%cpu | head -5
ss -tulpn 2>/dev/null | grep LISTEN
find /usr/bin -perm -4000 2>/dev/null
