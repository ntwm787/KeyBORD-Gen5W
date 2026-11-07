KeyBORD keyboard.hackers, package release 2.0.2

Prepared for NEMESIS 1.16+ / descriptor 1.1. Reported legacy working setup: 2023 IONIQ 5 SEL Gen5W,
Android 4.4/API 19, SmartTube. Gen5W across vehicle makes/models; no year, region or firmware revision lock.
The runtime requires S5W_M software, Android API 19 and the required keyboard IMEs.
Install and uninstall while parked. Full instructions and source:
https://github.com/ntwm787/KeyBORD-Gen5W

Hacker's Keyboard is a standalone, open-source Android keyboard app, similar in purpose to Gboard or Microsoft SwiftKey. It is distributed as a normal keyboard APK and does not require Google Play Services. KeyBORD packages it for text entry in third-party apps installed through NEMESIS, where the factory Hyundai keyboard is unavailable. Install the APK first, then use KeyBridge to select it as the Android input method.
This package refuses taking over an existing unmanaged keyboard installation.
Before APK removal, an active Hacker keyboard is replaced by the factory IME.
NEMESIS dependencies can require uninstalling KeyBridge first. APK updates may
reset app preferences because the manager removes the old managed APK.
Update this package first, then KeyBridge; confirm Update instead of uninstalling.

Licenses remain respective; see LICENSES-AND-CREDITS.txt and licenses/. NEMESIS is not bundled.
