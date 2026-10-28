# KeyBORD

USB-ready packages for installing Hacker's Keyboard, activating it as the Android input method (IME), and restoring the factory keyboard on the tested Hyundai Gen5W infotainment system.

KeyBORD uses an existing NEMESIS setup to run its installation and keyboard-selection scripts. **NEMESIS software is not bundled.** Obtain it separately and follow the [upstream NEMESIS documentation](https://github.com/xwtk/hmg_nemesis) for setup, compatibility, and execution instructions.

## Confirmed setup and test status

The reported working setup is a **2023 Hyundai IONIQ 5 SEL**, with **Gen5W infotainment running Android 4.4 (API 19)**, used with **SmartTube**.

| Component | Reported result |
| --- | --- |
| Hacker's Keyboard 1.41.1 APK installation | Worked on the confirmed setup. |
| KeyBridge activation script | Worked on the confirmed setup. |
| Packaged `Hyundai Keyboard Restore USB v1.zip` | Worked on the confirmed setup. |

These results are specific to the setup above. Other vehicles, trims, regions, firmware versions, Android versions, and applications are untested. SmartTube is the reported application context; this is not a claim that every SmartTube version or text field has been tested. KeyBORD does not install SmartTube.

Because KeyBridge selects the Android input method system-wide, Hacker's Keyboard is expected to work in other apps installed on Gen5W head units through NEMESIS. **Use with apps other than SmartTube is untested**, and keyboard behavior may vary by app.

## Packages

Download the following three USB-ready ZIPs from this repository's published files or releases:

| Download | Purpose |
| --- | --- |
| `Hacker Keyboard USB v1.zip` | Installs the Hacker's Keyboard **1.41.1 APK**. |
| `KeyBridge USB v1.zip` | Activates Hacker's Keyboard as the Android IME. Run after installing the APK. |
| `Hyundai Keyboard Restore USB v1.zip` | Restores the factory Hyundai IME. |

Use one package at a time. Installing the APK and activating the IME are separate steps.

## Before you start

- Keep the car **parked** throughout installation, activation, restoration, and testing.
- Have a working NEMESIS setup appropriate for your infotainment system. Review its upstream requirements before proceeding.
- Use a USB drive prepared according to the NEMESIS instructions and the vehicle's supported USB requirements.
- Keep a backup of the USB drive's existing `NEMESIS.data` and any files you will replace.

These packages change infotainment software or input-method settings. Use them at your own risk; compatibility and recovery are not guaranteed.

## Installation

### 1. Install Hacker's Keyboard

1. On your computer, open `Hacker Keyboard USB v1.zip` and **extract the outer ZIP directly to the USB drive's root**. Do not leave the extracted contents inside an extra folder.
2. **Keep the inner ZIP intact in the NEMESIS `Packages` folder.** Do not extract it, rename it, or move it out of that folder.
3. Safely eject the USB drive and connect it to the infotainment system while the car is parked.
4. Run the package using your working NEMESIS execution procedure. Allow the operation to finish before removing the drive.
5. Check **Packages** in NEMESIS for the **Hacker's Keyboard** package to confirm the APK installation completed before continuing.

The intended layout is the outer archive's contents at the USB root, including `NEMESIS.data` and the unchanged inner ZIP in its supplied location. Copying the unopened outer ZIP to the drive is not sufficient.

### 2. Activate the keyboard with KeyBridge

1. On your computer, open `KeyBridge USB v1.zip` and **extract the outer ZIP directly to the USB drive's root**. Do not leave the extracted contents inside an extra folder.
2. **Keep the inner ZIP intact in the NEMESIS `Packages` folder.** Do not extract it, rename it, or move it out of that folder.
3. Safely eject the USB drive and connect it to the infotainment system while the car is parked.
4. Run the package using your working NEMESIS execution procedure. Allow the operation to finish before removing the drive.
5. Open a text-entry field in SmartTube and verify that Hacker's Keyboard appears and accepts input.

If activation does not work, confirm that Hacker's Keyboard appears under **Packages** in NEMESIS and review the KeyBridge execution result before trying again.

## Restore the factory keyboard

The restore package was tested on the confirmed setup above.

1. On your computer, open `Hyundai Keyboard Restore USB v1.zip` and **extract the outer ZIP directly to the USB drive's root**. Do not leave the extracted contents inside an extra folder.
2. **Keep the inner ZIP intact in the NEMESIS `Packages` folder.** Do not extract it, rename it, or move it out of that folder.
3. Safely eject the USB drive and connect it to the infotainment system while the car is parked.
4. Run the package using your working NEMESIS execution procedure. Allow the operation to finish before removing the drive.
5. Open a text-entry field in SmartTube and verify that the factory Hyundai keyboard opens by default and accepts input. Hacker's Keyboard should no longer pop up.

Verify the active keyboard after restoration. This package restores the factory IME selection; it is not a full infotainment rollback or factory reset.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Nothing happens when the USB is connected | Confirm that NEMESIS is already working on this system and that you followed its execution procedure. Connecting the drive alone is not proof of execution. |
| The wrong operation runs | Confirm that the USB-root `NEMESIS.data` was replaced with the copy from the package you intend to run. Check for mixed package files. |
| A payload cannot be found | Check for an extra enclosing folder. Extract the outer ZIP to the USB root and leave the inner ZIP intact, with its original name and supplied location. |
| Hacker's Keyboard is installed but does not appear | APK installation does not select the IME. Run KeyBridge after confirming installation succeeded, then reopen the text-entry field. |
| KeyBridge does not activate the keyboard | Review available NEMESIS output or logs. Confirm the APK installed successfully and that the vehicle matches the tested setup. Do not assume a different firmware uses the same IME configuration. |
| The factory keyboard does not return | Inspect the execution result before repeating it. Confirm that the restore package's matching files are on the USB drive, then report any failure with the vehicle and firmware details. |
| Behavior differs on another system | Record the vehicle model/year/trim, region, infotainment firmware, Android version if known, package used, and observed result. Compatibility outside the confirmed setup remains unverified. |

When reporting a problem, include the exact ZIP filename, which steps completed, and relevant logs with personal information removed.

## Credits

- **KeyBORD's original author and contributors** — original installation, activation, and restore scripts; USB package preparation; and vehicle testing.
- **Klaus Weidner and the Hacker's Keyboard contributors** — [Hacker's Keyboard](https://github.com/klausw/hackerskeyboard), the keyboard application included as a 1.41.1 APK.
- **xwtk and the NEMESIS contributors** — [hmg_nemesis](https://github.com/xwtk/hmg_nemesis), the separately obtained execution software used by this workflow.

This is an independent community project. Product names identify the relevant software and vehicle; they do not imply endorsement by Hyundai or the upstream projects.

## Licensing and redistribution

Each component retains its respective license. Packaging components together does not relicense them under a single project-wide license.

| Component | License | Scope |
| --- | --- | --- |
| Original KeyBORD scripts | **GPL-3.0** | The original scripts authored for KeyBORD. |
| Hacker's Keyboard | **Apache-2.0** | The third-party keyboard application, including the bundled APK; see the [upstream repository](https://github.com/klausw/hackerskeyboard). |
| NEMESIS | **AGPL-3.0** | The separately obtained NEMESIS software; see the [upstream repository](https://github.com/xwtk/hmg_nemesis). **NEMESIS software is not bundled with KeyBORD.** |

### Original KeyBORD scripts

The original KeyBORD scripts are released under the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.html). Anyone may use, study, modify, redistribute, and continue this work subject to that license. Redistributed versions must retain applicable notices and meet the GPL's source-code and licensing requirements.

Distributions of the scripts must include the full GPL-3.0 license text, preserve the author's copyright notices, and provide the corresponding script source as required by the license. This README is not a replacement for the license text.

### Bundled Hacker's Keyboard APK

Hacker's Keyboard remains under **Apache-2.0**. Redistributing its APK requires including a copy of the Apache-2.0 license and preserving the applicable copyright, license, and attribution notices. Preserve and include any applicable upstream **NOTICE** material supplied with the distributed version. Mark modified files if distributing changes. See the [Apache-2.0 redistribution terms](https://www.apache.org/licenses/LICENSE-2.0) for the full requirements.

Keep those materials with the APK distribution, including in the downloadable keyboard package; an upstream link alone does not replace the required license copy or notices. The KeyBORD GPL-3.0 designation does not replace the APK's license or any applicable third-party notices within it.

### NEMESIS

NEMESIS retains its **AGPL-3.0** license. Obtain its software, source, license, and instructions from [xwtk/hmg_nemesis](https://github.com/xwtk/hmg_nemesis). Using NEMESIS to execute KeyBORD scripts does not change the stated licenses of the separate components. Any redistribution or modification of NEMESIS must follow its own license terms.

### Contributions

Improvements, documentation corrections, and clearly identified compatibility reports are welcome. Contributions to the original KeyBORD scripts must be compatible with their GPL-3.0 licensing. Preserve third-party ownership and license notices, and distinguish confirmed vehicle tests from untested changes.

Software is provided without warranty, subject to the terms of the applicable licenses.
