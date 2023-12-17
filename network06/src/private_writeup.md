# Tartaruga as a Service

## Goal

The challenge aims at teaching scraping data from captures using scripts.

## Context

The capture is about a simple REST api (pen up, pen down, forward) that controls a turtle robot. The flag is written in morse code.

## Solution

A solution script is provided at `src/verify.py`

1. Open the capture (with scapy or wireshark)
2. Extract the relevant data (`http and tcp.dstport == 5000`)
3. Plot the data:
   - dot: `down fwd10 up fwd10`
   - dash: `down fwd10 up fwd10`
   - sep: `up fwd30 down`
4. Convert from morse code
