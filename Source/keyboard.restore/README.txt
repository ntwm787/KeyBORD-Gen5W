KeyBORD keyboard.restore, package release 2.0.2

Prepared for NEMESIS 1.16+ / descriptor 1.1. Reported legacy working setup: 2023 IONIQ 5 SEL Gen5W,
Android 4.4/API 19, SmartTube. Gen5W across vehicle makes/models; no year, region or firmware revision lock.
The runtime requires S5W_M software, Android API 19 and the required keyboard IMEs.
Install and uninstall while parked. Full instructions and source:
https://github.com/ntwm787/KeyBORD-Gen5W

Installation selects the keyboard. Launch in My Packages selects it again.
The original default, enabled IME list and subtype are saved under
/data/nemesis/backup/keyboard.restore. Uninstall restores them when current settings
still match this package's applied state. Later changes are preserved; a missing
previous keyboard blocks restoration and retains the snapshot. Uninstall the
Restore package before KeyBridge for a controlled reverse-order round trip.
A failed postinstall can leave a registered package; retain logs before retrying.

Licenses remain respective; see LICENSES-AND-CREDITS.txt and licenses/. NEMESIS is not bundled.
