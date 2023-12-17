# Negozio Segreto - lvl 2

## Goal

The challenge aims at showing that `network` is often a precursor to other challenge types (e.g. `reversing`).

## Context

The capture contains some noise. The relevant parts are the HTTP requests to `192.168.32.225`.

## Solution

1. Open the capture
2. Find and explore relevant HTTP traffic (from packet 1004)
3. Find `script.js` and "reverse" it (more like replay it)
   - message -> reverse(message) -> b64decode(reverse(message))
