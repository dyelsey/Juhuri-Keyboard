#!/usr/bin/env bash
#Installs jdt-cyr keyboard in linux

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd /usr/share/X11/xkb
mv $DIR/jdt-cyr symbols
mv $DIR/jdt-cyr-russian symbols
cd rules
sudo python $DIR/add_rule.py
