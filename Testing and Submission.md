# Vehicle testing and Package Store submission

This guide covers installation checks, uninstall checks and portal submission.

## Vehicle test sequence

Record the NEMESIS version, vehicle, software version, initial default keyboard and any keyboard customizations. If migrating from legacy packages, use their Restore tool first and verify the factory keyboard, then follow the migration section in README.

1. Install Hacker Keyboard USB v2. Confirm Hacker's Keyboard appears in My Packages.
2. Install KeyBridge USB v2. Open a SmartTube text field and verify Hacker's Keyboard accepts input.
3. Install Hyundai Keyboard Restore USB v2. Verify SmartTube now opens the factory Hyundai keyboard.
4. Uninstall Restore through My Packages. Verify the previous Hacker's Keyboard selection returns.
5. Uninstall KeyBridge. Verify the original factory selection returns.
6. Uninstall Hacker's Keyboard. Confirm the factory keyboard still accepts input and all three project packages are removed.
7. Compare the initial and final keyboard/default/enabled/subtype settings. Keep install and uninstall logs. Confirm later intentional keyboard changes are preserved as documented in a separate test if practical.

If an operation fails, retain logs and `/data/nemesis/backup/keyboard.activate` or `keyboard.restore`. A failed postinstall may leave the package registered. Do not force uninstall or erase backups. Stop the sequence and report the exact result.

These are manual tests for the head-unit owner. The local test harness simulates settings, IME selection, rollback, reverse-order cleanup and failures; it does not run Android's package manager or prove on-car behavior.

## Publication layout

Upload README.md, LICENSE, Source/, Store/ and the three USB/ wrappers to the GitHub repository. Keep Validation/ if useful to reviewers. Do not publish work/ analysis binaries or unrelated OTA experiments. The Source tree is editable and matches the Store payloads.

The three existing IDs are preserved for migration:

| Portal upload | ID | Package version | Dependency |
| --- | --- | --- | --- |
| Store/keyboard.hackers.zip | keyboard.hackers | 2.0.2 | none |
| Store/keyboard.activate.zip | keyboard.activate | 2.0.2 | keyboard.hackers >= 2.0.1 |
| Store/keyboard.restore.zip | keyboard.restore | 2.0.2 | none |

Public catalog availability does not prove that an ID is unreserved: pending submissions can also reserve IDs. If the portal says an ID belongs to someone else, do not submit under that ID. Report the collision so all descriptors, dependencies, state paths and migration instructions can be revised together. No account credentials are needed to prepare or locally validate these files.

## Submit after successful head-unit tests

1. Create/sign into your xwtk.Account, then open https://portal.xwtk.cloud/nemesis/.
2. Choose Submit a new package (or Submit new version if your account already owns that ID).
3. Upload **Store/keyboard.hackers.zip**, not its USB wrapper. Enter repository https://github.com/ntwm787/KeyBORD-Gen5W.
4. Check the parsed descriptor: format 1.1, ID keyboard.hackers, package version 2.0.2, OS/model restrictions and license information.
5. Include truthful install/uninstall test details, then submit for approval.
6. Repeat separately for keyboard.activate and keyboard.restore. KeyBridge requires the keyboard dependency to be listed/available; submit the keyboard first and resolve its approval before claiming one-click dependency availability.
7. Keep the current release available while review is pending. Once approved, verify the store listing and NEMESIS Manager metadata.

Portal approval and publication are managed through your xwtk.Account.

## Upstream references

- https://github.com/xwtk/hmg_nemesis/blob/main/04-Packages.md
- https://github.com/xwtk/hmg_nemesis/blob/main/07-Submit-a-Package.md
