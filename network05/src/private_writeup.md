# Ultra Up-to-date Encoding

## Goal

The challenge aims at showing how emails can encode binary files.

## Context

The capture contains a simple SMTP session.

## Solution

1. Open the capture
2. Follow the SMTP stream (`tcp.stream eq 0`)
3. Extract the uuencoded content (from `begin 644 flag.png` to `end`)
4. uudecode (e.g. https://www.webutils.pl/UUencode)
