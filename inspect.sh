#!/bin/bash
D=${1:-example.com}
echo "DNS A records for $D:"
dig +short "$D" A 
echo "TLS cert for $D:" 
echo | openssl s_client -connect "$D":443 2>/dev/null | openssl x509 -noout -issuer -dates
