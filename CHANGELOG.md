# 2.0.2 - 2026-11-06 (KeyBORD 2.02)

- Broaden all three packages from IONIQ 5 to Android Gen5W across vehicle makes/models: `os=*S5W_M*`, `models=any`.
- Retain the Gen5W software-family, Android API 19, root, boot-complete and required IME checks; no firmware-revision/year/region lock.
- Preserve package IDs and KeyBridge's `keyboard.hackers >= 2.0.1` dependency for updates over 2.01.
- Document Update-in-place order: keyboard first, KeyBridge second; Restore only when factory selection is wanted.
- Keep the Hacker's Keyboard 1.41.1 APK unchanged and retain licenses/notices.
- Fit all package detail descriptions within NEMESIS's 256-character limit.

# 2.0.1 - prepared 2026-11-02

- Migrate installable packages to descriptor version 1.1, with distinct package-version, type, descriptions and compatibility/dependency metadata.
- Preserve keyboard.hackers, keyboard.activate and keyboard.restore IDs.
- Keep the Hacker's Keyboard 1.41.1 APK unchanged.
- Include licenses/notices within the actual store-upload packages.
- Add repeatable Launch actions and reversible IME-selection hooks; preserve later changes and refuse restoration when the original IME is missing.
- Guard APK removal by selecting the factory keyboard first; refuse taking over an unmanaged existing APK.
- Provide three USB wrappers and three corresponding store packages, editable source and a test/submission guide.

Local package and lifecycle checks passed.

## Compatibility correction

- Replace the exact observed software revision with os=NEEV* and models=neev*; no model-year, region, firmware date or revision restriction.
- Retain runtime API 19 / root / IME availability checks and the KeyBridge package dependency.
- Make postuninstall cleanup self-contained so it does not rely on sibling package files after NEMESIS copies the hook.
