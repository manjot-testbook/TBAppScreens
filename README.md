# Testbook Android — Screen Wireflows & Analytics Specification

**Repository:** `manjot-testbook/TBAppScreens`  
**Application Version:** 9.11.x  
**Author:** Product & Analytics Core Team  
**Live Interactive Hub:** [https://manjot-testbook.github.io/TBAppScreens/](https://manjot-testbook.github.io/TBAppScreens/)  
**Specification Spreadsheet:** [`event_tracking_spec.csv`](./event_tracking_spec.csv) (94 screens)  
**Single Source of Truth Catalog:** [`screens_data.json`](./screens_data.json)  
**How to Add/Update Screens:** [See CONTRIBUTING.md](./CONTRIBUTING.md)  

---

## 1. Executive Overview

This repository provides an authoritative, interactive visual screen wireflow tree and event tracking specification for the **Testbook Android App (v9.11.x)**.

It organizes **94 unique production screens** into **12 structured product flow lanes**, standardizing all bottom navigation destinations under the **`*_DASHBOARD_SCREEN`** convention and fully mapping the Tests Quick Access Bar (QAB) features:
1. **Acquisition, Auth & Onboarding (4)** — Launch splash, phone login, OTP verification, goal onboarding.
2. **Home Hub & Navigation (6)** — `HOME_FEED_DASHBOARD_SCREEN` (verified real Home feed with active Home tab indicator, incomplete payment card, and enrolled exam goals), `NOTIFICATIONS_CENTER_SCREEN`, `HAMBURGER_DRAWER_NAVIGATION_SCREEN` (16 destinations), `ENROLLED_EXAMS_MODAL`, `ENROLLED_EXAMS_MANAGEMENT_SCREEN`, and `SAMADHAN_AI_DOUBT_SOLVER_SCREEN`.
3. **Discovery & Search Sections (5)** — Global search input, multi-category results, and dedicated filtered category tabs (Exams, Courses, Test Series).
4. **Exam Portals & Preparation (6)** — SSC CGL / RRB NTPC hubs (`EXAM_PAGE_OVERVIEW_SCREEN`), top action buttons (`Exam Info`, `Previous Year Papers`, `Free Test`, `Tricky Test`), section tabs (`Test Series`, `testbook LIVE`, `Study Notes`, `Quizzes`), and official notification updates.
5. **Assessment & Live Testing Funnel (15)** — `TESTS_DASHBOARD_SCREEN` (Tests bottom navigation tab with enrolled test series and QAB rail), `LIVE_TESTS_DIRECTORY_SCREEN` (Live Panel ongoing/attempted tests), `LIVE_QUIZZES_DIRECTORY_SCREEN` (Daily live quizzes directory), `WEAK_AREAS_IMPROVEMENT_SCREEN` (AI-powered weak areas improvement portal), `ATTEMPTED_TESTS_HISTORY_SCREEN` (Attempted mock test log with marks and rank), `RANK_PREDICTOR_SCREEN` (Answer key URL analyzer and rank calculator), test series overview, difficulty modal, pre-test instructions, live exam engine, question pallet drawer, submit confirmation, comprehensive analysis, question solutions, and rank podium leaderboard.
6. **Practice & Free Quizzes (8)** — Daily quizzes directory, adaptive practice hub (`FREE_PRACTICE_SCREEN`), active question interface, answered feedback states, study notes overview, chapter PDF viewer, and Pass paywall.
7. **Courses & Masterclasses (5)** — `COURSES_EXPLORE_SCREEN`, `SKILL_ACADEMY_DASHBOARD_SCREEN` (Skill Academy bottom tab), masterclass timeline (`DAILY_LIVE_CLASSES_SCREEN`), educators directory, and individual teacher profile.
8. **SmartBooks Store (3)** — Physical printed smart books storefront, product details page (5000+ PYQs & MCQs SmartBook, savings badge, 5.0 rating), and shipping delivery address checkout form (`SMARTBOOK_DELIVERY_ADDRESS_SCREEN`).
9. **SuperCoaching Pre-Purchase (3)** — `SUPER_COACHING_DASHBOARD_SCREEN` (Super bottom navigation tab with 375+ govt exams coaching and pricing), multi-tier plan picker, and coupon discount engine.
10. **Pass Paywalls & QR Checkout (6)** — `PASS_DASHBOARD_SCREEN` (Pass bottom navigation tab paywall), `PASS_ELITE_DASHBOARD_SCREEN` (Pass Elite catalogue and FAQs), plan duration switcher, dynamic UPI QR modal, payment gateway, and failure recovery.
11. **Post-Purchase Super Pass Live Ecosystem (23)** — `SUPER_PASS_DASHBOARD_SCREEN` (Super Pass bottom navigation tab: active subscriber dashboard), Explore Courses (`SUPER_PASS_EXPLORE_COURSES_SCREEN`), Manage Exams switcher, Course Language & Tier Selector, Enrolled Course Study Hub (`ENROLLED_COURSE_STUDY_DASHBOARD_SCREEN`), Course In-Module Search, Lessons & Activities Timeline, Upcoming Live Class Reminder, Interactive Video Lecture Player, Synchronized Chat Replay Sheet, Lesson Progress Leaving Modal, Study Plan Daily date-wise schedule, Study Plan Subjectwise curriculum, Study Plan Weekly Timetable calendar, Offline Downloads storage manager, Course Doubt Discussion forum, Ask a Doubt Editor, Batch Announcements bulletin, post-purchase test series, study notes, practice, and faculty directory.
12. **Daily Retention & Utilities (10)** — `NEWS_DASHBOARD_SCREEN` (News bottom navigation tab: daily news digest, date switcher, exam tips), saved news bookmarks, blog reader, refer & earn cashback, transactions list, order receipt, app settings, Pass settings tab, user settings, and app language selector.

---

## 2. Interactive Deliverables

* 🌐 **[Live Interactive Wireflow Tree Hub](https://manjot-testbook.github.io/TBAppScreens/):**
  * **Tree Canvas Mode:** Pan & zoom across all 12 color-themed flow lanes with hierarchical card layout.
  * **Pinch-to-Zoom:** Native support for Mac trackpad two-finger pinch (`ctrlKey + wheel`) and mobile multi-touch pinch gestures with focal-point scaling (20% – 250%).
  * **Screen Inspector Mode:** Select any screen to open the slide-out inspector displaying the phone screenshot, copyable `SV_` contract JSON, dedicated tables for **Global Attributes** (6 standard fields) and **Event Attributes** (mapped parameters), and clickable outbound flow pills.
* 📥 **[Download Companion Tracking CSV (`event_tracking_spec.csv`)](./event_tracking_spec.csv):**
  * 89 rows matching every production screen with direct links to screenshot assets and `SV_` JSON schemas.
* 📋 **[Single Source of Truth Catalog (`screens_data.json`)](./screens_data.json):**
  * Clean JSON catalog containing all screen metadata, referrers, descriptions, components, and outbound transitions.

---

## 3. How to Add or Update a Screen

Whenever you make changes to `screens_data.json` or screenshots and push to `main` (or edit directly on GitHub), **GitHub automatically rebuilds and deploys the live page within ~30 seconds.**

1. **Drop your screenshot**: Save image as `screenshots/MY_SCREEN_NAME.png`.
2. **Add entry in `screens_data.json`**:
   ```json
   {
     "id": "SCR_72",
     "screenName": "MY_NEW_SCREEN",
     "referrerScreenName": "HOME_FEED_DASHBOARD_SCREEN",
     "flow": "2. Home Hub & Navigation",
     "screenshot": "MY_NEW_SCREEN.png",
     "description": "Explanation of screen purpose.",
     "outboundPaths": [
       { "action": "Tap primary button", "target": "DESTINATION_SCREEN" }
     ],
     "keyComponents": [
       { "name": "Primary CTA", "type": "button", "detail": "Navigates forward" }
     ]
   }
   ```
3. **Run sync & push**:
   ```bash
   python3 sync.py
   git add . && git commit -m "feat: add MY_NEW_SCREEN" && git push origin main
   ```
   *(For full details and browser-only workflows, see [CONTRIBUTING.md](./CONTRIBUTING.md)).*

---

## 4. Standard `screen_view` Contract

Every screen implements this standard payload contract for analytics instrumentation:

```json
{
  "event": "screen_view",
  "screen_name": "EXAM_PAGE_OVERVIEW_SCREEN",
  "referrer_screen_name": "HOME_FEED_DASHBOARD_SCREEN"
}
```

---

## 5. Repository File Structure

```text
TBAppScreens/
├── index.html                # Interactive viewer canvas & inspector hub (GitHub Pages)
├── screens_data.json         # Master catalog of all 71 screens (Single Source of Truth)
├── screenshots/              # Production mobile screenshots (.png only)
├── event_tracking_spec.csv   # Companion tracking spec spreadsheet
├── sync.py                   # Verification & CSV regeneration script
├── CONTRIBUTING.md           # Step-by-step guide to add/update screens
├── README.md                 # Executive documentation
├── .nojekyll                 # GitHub Pages configuration
└── RawDump/                  # Historical archive (past PRDs, matrices, screenshots)
```
