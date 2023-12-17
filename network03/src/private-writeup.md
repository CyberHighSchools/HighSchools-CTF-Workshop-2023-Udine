# Negozio Segreto - lvl 3

## Goal

The challenge aims at showing how Wireshark can decode TLS if provided with the keys.

## Context

The capture contains some noise. The relevant parts are the HTTPS requests to `192.168.32.225`.

## Solution

1. Open the capture
2. Apply the TLS keys (Edit -> Preferences -> Protocols -> TLS -> Pre Master Secrets Log Filename)
3. Find and explore relevant HTTPS traffic (from packet 3401)
