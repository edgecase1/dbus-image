#!/usr/bin/env bash

export DBUS_SESSION_BUS_ADDRESS=`dbus-daemon --fork --config-file=/etc/dbus-1/system.conf --print-address`

exec python3 /app/service.py
