# Dominio Non Sospetto

## Goal

The challenge aims at teaching the concept of DNS exfiltration.

## Context

The capture contains some noise. The relevant parts are the DNS queries to `?.snakectf.org`.

## Solution

A solution script is provided at `src/verify.py`

1. Open the capture
2. Filter for the relevant data (`dns.qry.name contains "snakectf" and udp.dstport eq 53`)
3. Reorder the data based on the subdomain prefix (`17-_` < `20-t`)
