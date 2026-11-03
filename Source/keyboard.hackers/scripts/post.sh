#!/system/bin/sh
# Copyright (C) 2026 ntwm787 and contributors
# SPDX-License-Identifier: GPL-3.0-only
. ./scripts/common.sh
require_android
ime_exists "$HACKER" || fail 'Keyboard APK installation could not be confirmed.'
echo 'Hacker keyboard installed. Install or launch KeyBridge to activate it.'
