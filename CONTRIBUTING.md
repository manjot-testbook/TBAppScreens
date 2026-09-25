# How to Add or Update Screens in Testbook Screen Bible

This repository powers the live interactive [Testbook Screen Bible & Wireflow Tree](https://manjot-testbook.github.io/TBAppScreens/).

Whenever you commit or push changes to branch `main` (either via terminal or directly in your browser on GitHub.com), **GitHub automatically rebuilds and updates the live deployed page within ~30 seconds.**

---

## 📁 Repository Structure Overview

```text
TBAppScreens/
├── screens_data.json         <-- ⭐ SINGLE SOURCE OF TRUTH (All screens, descriptions, paths)
├── screenshots/              <-- ⭐ Active production screenshots (.png only)
├── index.html                <-- Interactive Figma wireflow canvas & inspector hub
├── event_tracking_spec.csv   <-- Generated tracking spreadsheet for tech/analytics
├── sync.py                   <-- One-command sync & validation tool
├── README.md                 <-- Executive documentation & architecture
└── RawDump/                  <-- Historical archive (legacy docs, matrices, past screenshots)
```

---

## 🚀 How to Add a New Screen (3 Steps)

### Step 1: Save your Screenshot
Capture or save your phone screenshot into the `screenshots/` directory using an uppercase descriptive name:
```text
screenshots/MY_NEW_SCREEN_NAME.png
```
*(Recommended: uncropped portrait PNG format).*

---

### Step 2: Add an Entry to `screens_data.json`
Open `screens_data.json` and add a JSON block for your screen under the appropriate flow:

```json
{
  "id": "SCR_72",
  "screenName": "MY_NEW_SCREEN_NAME",
  "referrerScreenName": "HOME_FEED_DASHBOARD_SCREEN",
  "flow": "2. Home Hub & Navigation",
  "screenshot": "MY_NEW_SCREEN_NAME.png",
  "description": "Clear explanation of what this screen does.",
  "outboundPaths": [
    {
      "action": "Tap primary action button",
      "target": "NEXT_DESTINATION_SCREEN"
    },
    {
      "action": "Press back arrow",
      "target": "HOME_FEED_DASHBOARD_SCREEN"
    }
  ],
  "keyComponents": [
    {
      "name": "Header Bar",
      "type": "header",
      "detail": "Screen title, navigation back icon, and search"
    },
    {
      "name": "Main Action CTA",
      "type": "button",
      "detail": "Primary button that navigates to the next step"
    }
  ]
}
```

#### Field Explanations:
* **`id`**: Unique sequential ID (e.g. `SCR_72`).
* **`screenName`**: Unique name in `UPPERCASE_WITH_UNDERSCORE` (e.g. `MY_NEW_SCREEN_NAME`).
* **`referrerScreenName`**: The name of the previous screen the user came from.
* **`flow`**: Must match one of the 12 flow groups listed below.
* **`screenshot`**: Exact filename inside the `screenshots/` folder.
* **`description`**: 1–2 sentences explaining user intent and screen purpose.
* **`outboundPaths`**: List of clickable CTAs and their target screens (renders clickable flow badges on the canvas).
* **`keyComponents`**: List of key interactive elements (buttons, inputs, cards, banners).

---

### Step 3: Sync & Push to GitHub

Run the automated sync tool:
```bash
python3 sync.py
```
This tool automatically:
1. Validates that the screenshot exists.
2. Checks for duplicates or broken links.
3. Automatically updates `event_tracking_spec.csv`.
4. Syncs the offline fallback in `index.html`.

Then commit and push:
```bash
git add .
git commit -m "feat: add MY_NEW_SCREEN_NAME"
git push origin main
```

**Done!** GitHub Pages will build and deploy the update live in ~30 seconds.

---

## 🔄 How to Update an Existing Screen

### Case A: You took a better / updated screenshot
1. Replace the existing image in `screenshots/` with the new file (keep the same filename, e.g. `screenshots/EXAM_PAGE_OVERVIEW_SCREEN.png`).
2. Run `python3 sync.py` (optional, to verify).
3. Commit and push:
   ```bash
   git add screenshots/
   git commit -m "update: refresh screenshot for EXAM_PAGE_OVERVIEW_SCREEN"
   git push origin main
   ```

### Case B: You want to edit screen details, referrers, or CTAs
1. Open `screens_data.json` and find the `screenName`.
2. Edit `description`, `referrerScreenName`, `outboundPaths`, or `keyComponents`.
3. Run `python3 sync.py` to regenerate the companion CSV.
4. Commit and push:
   ```bash
   git add screens_data.json event_tracking_spec.csv
   git commit -m "update: revise outbound paths for EXAM_PAGE_OVERVIEW_SCREEN"
   git push origin main
   ```

---

## 🌐 Updating Directly on GitHub.com (No Terminal Needed!)

You don't even need terminal access or Git installed:
1. Go to `https://github.com/manjot-testbook/TBAppScreens`.
2. To upload a new screenshot: Click **`screenshots/`** ➔ **Add file** ➔ **Upload files** ➔ Commit.
3. To update details: Click **`screens_data.json`** ➔ Click the **✎ Edit** pencil icon ➔ Update text/JSON ➔ Commit changes.
4. The live site automatically reloads with the new data!

---

## 🎨 12 Standard Flow Groups

Assign your screen to one of these predefined flow groups:
1. `1. Acquisition, Auth & Onboarding` (Royal Blue `#2563eb`)
2. `2. Home Hub & Navigation` (Emerald `#059669`)
3. `3. Discovery & Search Sections` (Sky Cyan `#0284c7`)
4. `4. Exam Portals & Preparation` (Violet `#7c3aed`)
5. `5. Assessment & Live Testing Funnel` (Purple `#9333ea`)
6. `6. Practice & Free Quizzes` (Amber `#d97706`)
7. `7. Courses & Masterclasses` (Sunset Orange `#ea580c`)
8. `8. SmartBooks Store` (Teal `#0d9488`)
9. `9. SuperCoaching Pre-Purchase` (Rose `#e11d48`)
10. `10. Pass Paywalls & QR Checkout` (Crimson `#dc2626`)
11. `11. Post-Purchase Super Pass Live Ecosystem` (Indigo `#4f46e5`)
12. `12. Daily Retention & Utilities` (Slate `#475569`)
