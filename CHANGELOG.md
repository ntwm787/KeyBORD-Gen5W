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
