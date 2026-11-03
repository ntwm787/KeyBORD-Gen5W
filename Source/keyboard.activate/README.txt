KeyBORD keyboard.activate, package release 2.0.1

Prepared for NEMESIS 1.16+ / descriptor 1.1. Reported legacy working setup: 2023 IONIQ 5 SEL Gen5W,
Android 4.4/API 19, SmartTube. Current declared OS/model hints are in NEMESIS.data.
Install and uninstall while parked. Full instructions and source:
https://github.com/ntwm787/KeyBORD-Gen5W

Installation selects the keyboard. Launch in My Packages selects it again.
The original default, enabled IME list and subtype are saved under
/data/nemesis/backup/keyboard.activate. Uninstall restores them when current settings
still match this package's applied state. Later changes are preserved; a missing
previous keyboard blocks restoration and retains the snapshot. Uninstall the
Restore package before KeyBridge for a controlled reverse-order round trip.
A failed postinstall can leave a registered package; retain logs before retrying.

Licenses remain respective; see LICENSES-AND-CREDITS.txt and licenses/. NEMESIS is not bundled.
