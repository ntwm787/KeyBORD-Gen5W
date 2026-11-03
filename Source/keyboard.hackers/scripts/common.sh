#!/system/bin/sh
# Copyright (C) 2026 ntwm787 and contributors
# SPDX-License-Identifier: GPL-3.0-only
export PATH=/sbin:/vendor/bin:/system/sbin:/system/bin:/system/xbin
umask 077
set -f
HACKER=org.pocketworkstation.pckeyboard/.LatinIME
OEM=com.android.inputmethod.diopen/.DioInputMethodService
KEYS='default_input_method enabled_input_methods selected_input_method_subtype'
fail() { echo "ERROR: $*"; exit 1; }
require_android() {
 IDENTITY=$(id 2>&1) || fail 'Cannot determine execution identity.'
 case "$IDENTITY" in uid=0\(*|'uid=0 '*) ;; *) fail 'Root required.' ;; esac
 [ "$(getprop sys.boot_completed)" = 1 ] || fail 'Wait for Android to finish starting.'
 [ "$(getprop ro.build.version.sdk)" = 19 ] || fail 'This build targets Android API 19 Gen5W.'
}
ime_exists() {
 AVAILABLE=$(ime list -a -s) || return 1
 for ITEM in $AVAILABLE; do [ "$ITEM" != "$1" ] || return 0; done
 return 1
}
capture() {
 mkdir -p "$STATE/$1" || return 1
 for KEY in $KEYS; do
  VALUE=$(settings get secure "$KEY") || return 1
  echo "$VALUE" > "$STATE/$1/$KEY" || return 1
 done
}
restore_before() {
 BEFORE=$(cat "$STATE/before/default_input_method") || return 1
 ime_exists "$BEFORE" || { echo "Previous keyboard unavailable: $BEFORE"; return 1; }
 ime enable "$BEFORE" || return 1
 ime set "$BEFORE" || return 1
 for KEY in $KEYS; do
  VALUE=$(cat "$STATE/before/$KEY") || return 1
  if [ "$VALUE" = null ]; then
   settings delete secure "$KEY" || return 1
  else
   settings put secure "$KEY" "$VALUE" || return 1
  fi
 done
 for KEY in $KEYS; do
  VALUE=$(settings get secure "$KEY") || return 1
  [ "$VALUE" = "$(cat "$STATE/before/$KEY")" ] || return 1
 done
}
select_target() {
 require_android
 ime_exists "$TARGET" || fail "Keyboard not installed: $TARGET"
 CURRENT=$(settings get secure default_input_method) || fail 'Cannot read current keyboard.'
 ime_exists "$CURRENT" || fail 'Current keyboard is unknown; refusing to snapshot it.'
 # Preserve the first baseline until the package has been uninstalled.
 if [ ! -f "$STATE/before.ready" ]; then
  capture before || fail 'Cannot save previous keyboard settings.'
  echo ready > "$STATE/before.ready" || fail 'Cannot finalize keyboard snapshot.'
 fi
 if ime enable "$TARGET" && ime set "$TARGET" &&
    [ "$(settings get secure default_input_method)" = "$TARGET" ] && capture after; then
  echo ready > "$STATE/after.ready" || fail 'Cannot finalize applied-state record.'
  echo "SUCCESS: active keyboard is $TARGET"
 else
  if restore_before; then
   echo 'Selection failed; previous keyboard settings restored.'
   cleanup_state || echo "Completed rollback snapshot retained at $STATE"
  else
   echo "Selection failed and rollback could not be verified. Keep $STATE for recovery."
  fi
  fail 'Keyboard selection did not complete.'
 fi
}
undo_selection() {
 require_android
 [ -f "$STATE/before.ready" ] || { echo 'No saved selection to undo (legacy install or never applied).'; return 0; }
 if [ -f "$STATE/after.ready" ]; then
  # Respect a keyboard change made after this package's last selection.
  for KEY in $KEYS; do
   VALUE=$(settings get secure "$KEY") || fail 'Cannot read current keyboard settings.'
   if [ "$VALUE" != "$(cat "$STATE/after/$KEY")" ]; then
    echo 'Keyboard settings changed afterward; preserving the current settings.'
    return 0
   fi
  done
 fi
 restore_before || fail "Cannot restore previous keyboard. Keep $STATE and restore its missing IME first."
 echo 'Previous keyboard settings restored and verified.'
}
cleanup_state() {
 # Only known snapshot files are removed; no recursive delete.
 for PHASE in before after; do
  for KEY in $KEYS; do
   [ ! -f "$STATE/$PHASE/$KEY" ] || rm "$STATE/$PHASE/$KEY" || return 1
  done
  [ ! -d "$STATE/$PHASE" ] || rmdir "$STATE/$PHASE" || return 1
 done
 for FLAG in before.ready after.ready; do
  [ ! -f "$STATE/$FLAG" ] || rm "$STATE/$FLAG" || return 1
 done
 [ ! -d "$STATE" ] || rmdir "$STATE" || return 1
}
