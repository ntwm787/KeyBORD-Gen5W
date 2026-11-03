# KeyBORD

Three keyboard packages for Hyundai IONIQ 5 Gen5W, updated for NEMESIS descriptor 1.1 and the Package Store. Package release 2.0.1. NEMESIS is required separately and is not bundled.

## Downloads

There are three package types. Each has a USB wrapper for testing and an inner package for portal upload:

| Package | USB download | Portal upload |
| --- | --- | --- |
| Hacker's Keyboard | [Hacker Keyboard USB v2.zip](USB/Hacker%20Keyboard%20USB%20v2.zip) | [keyboard.hackers.zip](Store/keyboard.hackers.zip) |
| KeyBridge | [KeyBridge USB v2.zip](USB/KeyBridge%20USB%20v2.zip) | [keyboard.activate.zip](Store/keyboard.activate.zip) |
| Hyundai Keyboard Restore | [Hyundai Keyboard Restore USB v2.zip](USB/Hyundai%20Keyboard%20Restore%20USB%20v2.zip) | [keyboard.restore.zip](Store/keyboard.restore.zip) |

The Store directory holds the three corresponding installable packages, not additional tools. **Upload a Store ZIP to the portal, never a USB wrapper or the project bundle.** The older USB v1 files at the repository root remain available for the original NEMESIS workflow.

## Requirements and test status

- A working NEMESIS 1.16+ installation on Android-based Gen5W with API 19; Android must be fully started.
- Factory Hyundai IME `com.android.inputmethod.diopen/.DioInputMethodService` present.
- Keep the car parked throughout install, selection, uninstall and verification.

Legacy v1 keyboard installation, KeyBridge activation and factory restore were reported working on a 2023 Hyundai IONIQ 5 SEL, Gen5W Android 4.4/API 19, in SmartTube. Hacker's Keyboard remains version 1.41.1 and its APK is byte-identical to that release.

Compatibility metadata uses `os=NEEV*` and `models=neev*`, covering the IONIQ 5 family without a fixed firmware revision, date, region or model year. NEMESIS supports these wildcard patterns. Its `os` value matches the software identifier, not Android's `4.4` version string. No particular firmware release is required.

The actual runtime checks require Android API 19, root, Android fully started and the needed keyboard IMEs. No firmware identifier, build date or binary hash is checked by these keyboard packages. ccNC and S5W_L are outside scope.

## Install from USB

Use one USB wrapper at a time. Preserve existing USB files before replacing them.

### 1. Install Hacker's Keyboard

1. Extract `Hacker Keyboard USB v2.zip` directly to the USB root, without an extra enclosing directory.
2. **Keep the inner ZIP intact in the supplied `packages` folder.** Do not extract it, rename it or move it out of that folder.
3. Safely eject the drive, connect it while parked and confirm installation through NEMESIS.
4. In NEMESIS Manager, check **My Packages** for **Hacker's Keyboard** before continuing.

The keyboard package installs the APK; selecting it is a separate step. The package refuses to take ownership of an existing Hacker's Keyboard installed outside the same NEMESIS package ID. Preserve that installation and its settings before deciding whether to remove it manually.

### 2. Activate with KeyBridge

1. Extract `KeyBridge USB v2.zip` directly to USB root.
2. **Keep the inner ZIP intact in the supplied `packages` folder.**
3. Connect the drive while parked and confirm installation. KeyBridge depends on `keyboard.hackers` package version 2.0.1 or later.
4. Open a text-entry field in SmartTube and verify Hacker's Keyboard appears and accepts input.

Installation selects the IME. You can later select it again using **My Packages -> KeyBridge -> Launch**. This selects the Android input method system-wide. Keyboard behavior can vary by app.

### 3. Restore the Hyundai keyboard

1. Extract `Hyundai Keyboard Restore USB v2.zip` directly to USB root.
2. **Keep the inner ZIP intact in the supplied `packages` folder.**
3. Connect the drive while parked and confirm installation, or use **Launch** if this package is already installed.
4. Open a text-entry field in SmartTube. Verify the Hyundai keyboard is the default and Hacker's Keyboard no longer pops up.

Restoration changes IME selection; it does not remove the Hacker's Keyboard APK or roll back infotainment firmware.

## Uninstall and updates

KeyBridge and Restore save the prior default IME, enabled IME list and selected subtype under `/data/nemesis/backup/<package-id>/`. On uninstall they restore that snapshot if the current values still match their recorded applied state. Later changes are preserved rather than overwritten. If a required previous IME is missing, uninstall refuses and retains the snapshot; reinstall that IME first. Snapshot files are removed only by the post-uninstall cleanup hook after successful removal.

For an exact controlled round trip, uninstall in reverse order: **Hyundai Keyboard Restore -> KeyBridge -> Hacker's Keyboard**. Restore removal may temporarily reactivate Hacker's Keyboard; KeyBridge removal then returns to the original IME. NEMESIS prevents removing the Hacker's Keyboard package while KeyBridge depends on it. Before removing a currently active Hacker's Keyboard APK, its uninstall hook selects and verifies the factory IME.

NEMESIS runs old uninstall hooks when updating a package, so updates can restore its baseline and then apply the new version. APK replacement can reset app preferences. Do not force uninstall or remove the snapshot directory to bypass a failure.

When migrating from v1, first use the existing Restore tool and verify the factory keyboard in SmartTube. Remove old Restore and KeyBridge entries from My Packages, then update or reinstall Hacker's Keyboard with the new wrapper. Install the new KeyBridge afterward. Old helper packages have no saved baseline; their uninstall cannot reconstruct one retroactively. Record your current keyboard settings before migration.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Old compatibility warning | Check the inner package has `version=1.1`, and that you used this release's ZIP. |
| Dependency missing | Install Hacker's Keyboard package 2.0.1 first; a manually installed APK does not satisfy this NEMESIS dependency. |
| Package refused as incompatible | Record software/model and `nemesis compat` output. Check the Android version and required keyboard availability. |
| Nothing happens or wrong operation | Check USB-root NEMESIS.data and keep the intended inner package intact in `packages`. Avoid mixed descriptors. |
| Selection fails | Review package output/logs and confirm the IME exists. Send the exact package/version and relevant logs. |
| Uninstall refuses | Restore the missing original IME or resolve the dependency; preserve the snapshot. Do not force removal. |
| New build installation reports failure | A failed postinstall can leave a package registered. Inspect My Packages and logs before retrying or removing it. |
| Keyboard stays selected after helper removal | A later setting change may have caused the hook to preserve current values. Use the Restore tool and verify SmartTube. |

## Source code

Browse [Source/](Source/) for the editable package descriptors and shell scripts, or download [KeyBORD 2.01 Source.zip](KeyBORD%202.01%20Source.zip). Hacker's Keyboard source is maintained separately upstream, as linked in the licensing section. Run `python build.py` to rebuild the Store packages and existing USB wrappers from Source/.

## Store submission

See [Testing and Submission](Testing%20and%20Submission.md). Install and uninstall all revised packages on the head unit before submitting. Submit the three Store ZIPs separately, using repository `https://github.com/ntwm787/KeyBORD-Gen5W`. Local builds and simulations do not establish portal acceptance, package-ID ownership or vehicle compatibility.

## Credits and licenses

- Original KeyBORD scripts: ntwm787 and contributors, GPL-3.0-only. Complete editable sources are under Source and inside the packages.
- Hacker's Keyboard 1.41.1: Klaus Weidner and contributors, Apache-2.0; [upstream source](https://github.com/klausw/hackerskeyboard/tree/1.41.1). The keyboard Store ZIP carries the Apache license and collected upstream copyright notices. No standalone NOTICE was present in the inspected upstream tag. Retain any applicable NOTICE if replacing the APK in future.
- [NEMESIS](https://github.com/xwtk/hmg_nemesis): xwtk and contributors, AGPL-3.0, obtained separately and not bundled.

Licenses remain respective; packaging does not relicense the APK or NEMESIS. This is an independent community project, without implied endorsement by Hyundai or the upstream projects.
