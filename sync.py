#!/usr/bin/env python3
"""
Testbook App Screens — Catalog & Tracking Specification Sync Tool
-----------------------------------------------------------------
Usage:
    python3 sync.py

This script:
1. Validates screens_data.json (unique IDs, unique screenNames, required fields).
2. Verifies that every referenced screenshot exists in screenshots/.
3. Checks for any unreferenced/orphan screenshots in screenshots/.
4. Automatically regenerates event_tracking_spec.csv to keep the spreadsheet in sync.
5. Updates the offline embedded fallback data in index.html.
"""

import json
import os
import csv
import re
import sys

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(REPO_DIR, "screens_data.json")
CSV_PATH = os.path.join(REPO_DIR, "event_tracking_spec.csv")
HTML_PATH = os.path.join(REPO_DIR, "index.html")
SCREENSHOTS_DIR = os.path.join(REPO_DIR, "screenshots")

def main():
    print("=" * 60)
    print("Testbook Screen Bible — Sync & Validation Tool")
    print("=" * 60)

    # 1. Load screens_data.json
    if not os.path.exists(JSON_PATH):
        print(f"❌ Error: {JSON_PATH} not found!")
        sys.exit(1)

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        screens = json.load(f)

    print(f"✔ Loaded {len(screens)} screens from screens_data.json")

    # 2. Validation
    errors = []
    warnings = []
    seen_ids = set()
    seen_names = set()
    referenced_images = set()

    for i, s in enumerate(screens):
        sid = s.get("id")
        sname = s.get("screenName")
        screenshot = s.get("screenshot")
        flow = s.get("flow")

        # Check ID
        if not sid:
            errors.append(f"Screen index {i} is missing 'id'")
        elif sid in seen_ids:
            errors.append(f"Duplicate id '{sid}' at screen '{sname}'")
        seen_ids.add(sid)

        # Check screenName
        if not sname:
            errors.append(f"Screen index {i} is missing 'screenName'")
        elif sname in seen_names:
            errors.append(f"Duplicate screenName '{sname}'")
        seen_names.add(sname)

        # Check screenshot
        if not screenshot:
            errors.append(f"Screen '{sname}' has no 'screenshot' defined")
        else:
            referenced_images.add(screenshot)
            img_path = os.path.join(SCREENSHOTS_DIR, screenshot)
            if not os.path.exists(img_path):
                errors.append(f"Screenshot file missing: screenshots/{screenshot} for screen '{sname}'")
            elif os.path.getsize(img_path) < 1000:
                warnings.append(f"Screenshot file screenshots/{screenshot} seems very small ({os.path.getsize(img_path)} bytes)")

    # Check for orphan files in screenshots/
    if os.path.exists(SCREENSHOTS_DIR):
        existing_images = set(os.listdir(SCREENSHOTS_DIR))
        orphan_images = [img for img in existing_images if img.endswith(".png") and img not in referenced_images]
        if orphan_images:
            warnings.append(f"{len(orphan_images)} unreferenced PNG files in screenshots/ (e.g. {orphan_images[:5]})")

    if errors:
        print("\n❌ Validation Failed with errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    if warnings:
        print("\n⚠ Warnings:")
        for w in warnings:
            print(f"  - {w}")

    print("✔ Validation passed successfully!")

    # 3. Regenerate event_tracking_spec.csv
    fieldnames = [
        "Screen_ID",
        "Screen_Name",
        "Referrer_Screen_Name",
        "Flow_Group",
        "Event_Type",
        "Properties_JSON_Schema",
        "Outbound_Navigation_Paths",
        "Screenshot_Repository_URL"
    ]

    csv_rows = []
    for s in screens:
        out_items = []
        for p in s.get("outboundPaths", []):
            act = p.get("action", "")
            tgt = p.get("target", "")
            out_items.append(f"{act} -> {tgt}")
        outbound_str = " | ".join(out_items)

        schema_dict = {
            "event": "screen_view",
            "screen_name": s["screenName"],
            "referrer_screen_name": s.get("referrerScreenName", "UNKNOWN")
        }
        schema_str = json.dumps(schema_dict)
        sc_file = s.get("screenshot", "")
        screenshot_url = f"https://github.com/manjot-testbook/TBAppScreens/blob/main/screenshots/{sc_file}"

        csv_rows.append({
            "Screen_ID": s["id"],
            "Screen_Name": s["screenName"],
            "Referrer_Screen_Name": s.get("referrerScreenName", ""),
            "Flow_Group": s.get("flow", ""),
            "Event_Type": "screen_view",
            "Properties_JSON_Schema": schema_str,
            "Outbound_Navigation_Paths": outbound_str,
            "Screenshot_Repository_URL": screenshot_url
        })

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"✔ Generated event_tracking_spec.csv ({len(csv_rows)} rows)")

    # 4. Sync offline fallback data in index.html
    if os.path.exists(HTML_PATH):
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html = f.read()

        # Update inline fallback screens array using lambda to avoid regex escape issues
        screens_json = json.dumps(screens)
        new_html = re.sub(
            r"(const|let)\s+screens\s*=\s*\[.*?\];",
            lambda m: f"let screens = {screens_json};",
            html,
            count=1,
            flags=re.DOTALL
        )
        if new_html != html:
            with open(HTML_PATH, "w", encoding="utf-8") as f:
                f.write(new_html)
            print("✔ Updated inline fallback in index.html")

    print("\n🎉 Sync Complete! The repo is clean and ready.")
    print("=" * 60)

if __name__ == "__main__":
    main()
