#!/bin/bash
echo "Failed SSH logins, by IP:"
grep -i "failed password" /var/log/auth.log 2>/dev/null \
  | grep -oE "([0-9]+\.){3}[0-9]+" | sort | uniq -c | sort -rn | head
