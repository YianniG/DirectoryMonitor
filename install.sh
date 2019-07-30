#!/usr/bin/env bash

chmod +x change.pl
cp change.pl /usr/local/bin/change.pl

crontab monitor.cron
