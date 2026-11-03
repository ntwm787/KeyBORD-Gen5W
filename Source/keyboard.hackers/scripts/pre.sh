#!/system/bin/sh
# Copyright (C) 2026 ntwm787 and contributors
# SPDX-License-Identifier: GPL-3.0-only
. ./scripts/common.sh
require_android
ime_exists "$OEM" || fail 'Factory Hyundai keyboard is unavailable.'
EXISTING=$(pm path org.pocketworkstation.pckeyboard)
if [ -n "$EXISTING" ] && [ ! -f /data/nemesis/apps/keyboard.hackers/NEMESIS.data ]; then
 fail 'Hacker keyboard is already installed outside this managed package. Keep your data; remove it yourself before testing this package.'
fi
