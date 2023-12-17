#!/bin/bash

set -ex

./pylsb.py -i original.png -f ../flags.txt -w
mv original-lsb.png lsb.png
