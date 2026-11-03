#!/system/bin/sh
# Copyright (C) 2026 ntwm787 and contributors
# SPDX-License-Identifier: GPL-3.0-only
. ./scripts/common.sh
require_android
CURRENT=$(settings get secure default_input_method) || fail 'Cannot read active keyboard.'
if [ "$CURRENT" = "$HACKER" ]; then
 ime_exists "$OEM" || fail 'Cannot remove the active keyboard without the factory keyboard.'
 ime enable "$OEM" && ime set "$OEM" || fail 'Cannot select factory keyboard before APK removal.'
 [ "$(settings get secure default_input_method)" = "$OEM" ] || fail 'Factory keyboard selection failed.'
fi
