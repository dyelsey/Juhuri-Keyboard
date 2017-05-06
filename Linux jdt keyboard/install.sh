#!/usr/bin/env bash
cd /usr/share/X11/xkb
mv "jdt-cyr" symbols
cd rules
sudo python add_rule.py
