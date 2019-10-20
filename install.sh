#!/usr/bin/env bash

chmod +x change.py
cp change.py /usr/local/bin/change.py

touch /usr/local/etc/track.csv

crontab monitor.cron
