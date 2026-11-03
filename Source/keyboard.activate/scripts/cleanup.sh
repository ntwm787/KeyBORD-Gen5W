#!/system/bin/sh
# Copyright (C) 2026 ntwm787 and contributors
# SPDX-License-Identifier: GPL-3.0-only
# Self-contained: NEMESIS can copy this hook outside the package tree.
export PATH=/sbin:/vendor/bin:/system/sbin:/system/bin:/system/xbin
umask 077
STATE=/data/nemesis/backup/keyboard.activate
for PHASE in before after; do
 for KEY in default_input_method enabled_input_methods selected_input_method_subtype; do
  if [ -f "$STATE/$PHASE/$KEY" ]; then
   rm "$STATE/$PHASE/$KEY" || { echo 'ERROR: Snapshot cleanup failed.'; exit 1; }
  fi
 done
 if [ -d "$STATE/$PHASE" ]; then rmdir "$STATE/$PHASE" || exit 1; fi
done
for FLAG in before.ready after.ready; do
 if [ -f "$STATE/$FLAG" ]; then rm "$STATE/$FLAG" || exit 1; fi
done
if [ -d "$STATE" ]; then rmdir "$STATE" || exit 1; fi
exit 0
