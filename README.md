# Testbook Android — Screen Wireflows & Analytics Specification

**Repository:** `manjot-testbook/TBAppScreens`  
**Application Version:** 9.11.x  
**Author:** Product & Analytics Core Team  
**Deliverables:** Figma-Style Wireflow Tree Canvas (`index.html`), Master Tracking CSV (`event_tracking_spec.csv`), Historical Archive (`RawDump/`)  

---

## 1. Executive Overview

This repository provides an interactive, visual screen wireflow and event tracking specification for the **Testbook Android App (v9.11.x)**.

### What Tech Needs for `screen_view`:
Every screen is identified by a unique, standardized **`UPPERCASE_WITH_UNDERSCORE`** name:
* **`screen_name`**: The unique identifier for the rendered screen.
* **`referrer_screen_name`**: The origin screen the user transitioned from.
* **Outbound Paths**: The exact destination screens triggered by key user actions.

---

## 2. Interactive Deliverables

* 🌐 **[Open Interactive Figma Wireflow Hub (`index.html`)](https://manjot-testbook.github.io/TBAppScreens/):**
  * **Tree Canvas Mode:** High-level Figma-like visual canvas showing hierarchical branching and connected screen cards.
  * **Screen Inspector Mode:** Side-by-side view with phone screenshot on the left, copyable JSON payload, and clickable outbound navigation pills to walk through the app.
* 📥 **[Download Companion Tracking CSV (`event_tracking_spec.csv`)](./event_tracking_spec.csv):**
  * 36 rows matching every production screen with direct links to screenshot assets and `screen_view` JSON schemas.
* 📦 **[Historical Archive (`RawDump/`)](./RawDump/):**
  * Preserved initial code audits, legacy event matrices, and journey documents for reference.

---

## 3. Master Screen & Referrer Navigation Catalog

| # | Unique Screen Name (`screen_name`) | Default Referrer (`referrer_screen_name`) | Flow Group | Screenshot Asset |
|---|---|---|---|---|
| 01 | `LAUNCH_SPLASH_SCREEN` | `OS_LAUNCHER` | Acquisition & Auth | [`screenshots/01_launch.png`](./screenshots/01_launch.png) |
| 02 | `AUTH_MOBILE_LOGIN_SCREEN` | `LAUNCH_SPLASH_SCREEN` | Acquisition & Auth | [`screenshots/02_login_screen.png`](./screenshots/02_login_screen.png) |
| 03 | `AUTH_OTP_VERIFICATION_SCREEN` | `AUTH_MOBILE_LOGIN_SCREEN` | Acquisition & Auth | [`screenshots/04_after_otp.png`](./screenshots/04_after_otp.png) |
| 04 | `ONBOARDING_GOAL_SELECTION_SCREEN` | `AUTH_OTP_VERIFICATION_SCREEN` | Acquisition & Auth | [`screenshots/57_onboarding_goal_selection.png`](./screenshots/57_onboarding_goal_selection.png) |
| 05 | `HOME_FEED_DASHBOARD_SCREEN` | `ONBOARDING_GOAL_SELECTION_SCREEN` | Home & Discovery | [`screenshots/06_home_feed.png`](./screenshots/06_home_feed.png) |
| 06 | `GLOBAL_SEARCH_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Home & Discovery | [`screenshots/SCR_GLOBAL_SEARCH.png`](./screenshots/SCR_GLOBAL_SEARCH.png) |
| 07 | `SEARCH_RESULTS_SCREEN` | `GLOBAL_SEARCH_SCREEN` | Home & Discovery | [`screenshots/SCR_SEARCH_RESULTS.png`](./screenshots/SCR_SEARCH_RESULTS.png) |
| 08 | `ENROLLED_EXAMS_MODAL` | `HOME_FEED_DASHBOARD_SCREEN` | Home & Discovery | [`screenshots/56_my_exams_sheet.png`](./screenshots/56_my_exams_sheet.png) |
| 09 | `TESTS_EXPLORER_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Assessment & Testing | [`screenshots/SCR_TESTS_EXPLORE_SCROLLED.png`](./screenshots/SCR_TESTS_EXPLORE_SCROLLED.png) |
| 10 | `TEST_SERIES_OVERVIEW_SCREEN` | `TESTS_EXPLORER_SCREEN` | Assessment & Testing | [`screenshots/13_tests_landing.png`](./screenshots/13_tests_landing.png) |
| 11 | `EXAM_LEVEL_MODAL` | `TEST_SERIES_OVERVIEW_SCREEN` | Assessment & Testing | [`screenshots/12_tests_tab.png`](./screenshots/12_tests_tab.png) |
| 12 | `TEST_PRE_INSTRUCTIONS_SCREEN` | `TEST_SERIES_OVERVIEW_SCREEN` | Assessment & Testing | [`screenshots/15_test_instructions.png`](./screenshots/15_test_instructions.png) |
| 13 | `LIVE_TEST_TAKING_INTERFACE` | `TEST_PRE_INSTRUCTIONS_SCREEN` | Assessment & Testing | [`screenshots/18_test_interface.png`](./screenshots/18_test_interface.png) |
| 14 | `QUESTION_PALLET_DRAWER` | `LIVE_TEST_TAKING_INTERFACE` | Assessment & Testing | [`screenshots/19_question_pallet.png`](./screenshots/19_question_pallet.png) |
| 15 | `TEST_SUBMIT_CONFIRMATION_MODAL` | `QUESTION_PALLET_DRAWER` | Assessment & Testing | [`screenshots/29_test_submit_confirmation.png`](./screenshots/29_test_submit_confirmation.png) |
| 16 | `TEST_ANALYSIS_SCREEN` | `TEST_SUBMIT_CONFIRMATION_MODAL` | Assessment & Testing | [`screenshots/31_test_analysis.png`](./screenshots/31_test_analysis.png) |
| 17 | `QUESTION_SOLUTIONS_SCREEN` | `TEST_ANALYSIS_SCREEN` | Assessment & Testing | [`screenshots/34_test_solutions.png`](./screenshots/34_test_solutions.png) |
| 18 | `TEST_LEADERBOARD_PODIUM_SCREEN` | `TEST_ANALYSIS_SCREEN` | Assessment & Testing | [`screenshots/35_test_leaderboard.png`](./screenshots/35_test_leaderboard.png) |
| 19 | `SUPERCOACHING_LANDING_PAGE` | `HOME_FEED_DASHBOARD_SCREEN` | Monetization & Plans | [`screenshots/38_super_coaching_tab.png`](./screenshots/38_super_coaching_tab.png) |
| 20 | `SUPERCOACHING_PLAN_SELECTION_SCREEN`| `SUPERCOACHING_LANDING_PAGE` | Monetization & Plans | [`screenshots/41_super_plan_selection_full.png`](./screenshots/41_super_plan_selection_full.png) |
| 21 | `TESTBOOK_PASS_LANDING_PAYWALL` | `HOME_FEED_DASHBOARD_SCREEN` | Monetization & Plans | [`screenshots/48_pass_landing.png`](./screenshots/48_pass_landing.png) |
| 22 | `TESTBOOK_PASS_PLANS_SCREEN` | `TESTBOOK_PASS_LANDING_PAYWALL` | Monetization & Plans | [`screenshots/50_pass_plan_durations.png`](./screenshots/50_pass_plan_durations.png) |
| 23 | `DYNAMIC_UPI_QR_MODAL` | `TESTBOOK_PASS_LANDING_PAYWALL` | Monetization & Plans | [`screenshots/53_pass_checkout.png`](./screenshots/53_pass_checkout.png) |
| 24 | `PAYMENT_GATEWAY_SCREEN` | `SUPERCOACHING_PLAN_SELECTION_SCREEN`| Monetization & Plans | [`screenshots/42_make_payment_screen.png`](./screenshots/42_make_payment_screen.png) |
| 25 | `PAYMENT_FAILURE_RECOVERY_SCREEN` | `DYNAMIC_UPI_QR_MODAL` | Monetization & Plans | [`screenshots/54_pass_payment_failure.png`](./screenshots/54_pass_payment_failure.png) |
| 26 | `CURRENT_AFFAIRS_DIGEST_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Content & Utilities | [`screenshots/SCR_CURRENT_AFFAIRS.png`](./screenshots/SCR_CURRENT_AFFAIRS.png) |
| 27 | `SAVED_NEWS_BOOKMARKS_SCREEN` | `CURRENT_AFFAIRS_DIGEST_SCREEN` | Content & Utilities | [`screenshots/SCR_CA_BOOKMARKS.png`](./screenshots/SCR_CA_BOOKMARKS.png) |
| 28 | `STUDY_NOTES_OVERVIEW_SCREEN` | `TESTS_EXPLORER_SCREEN` | Content & Utilities | [`screenshots/SCR_STUDY_NOTES.png`](./screenshots/SCR_STUDY_NOTES.png) |
| 29 | `CHAPTER_PDF_NOTES_SCREEN` | `STUDY_NOTES_OVERVIEW_SCREEN` | Content & Utilities | [`screenshots/SCR_CHAPTER_NOTES.png`](./screenshots/SCR_CHAPTER_NOTES.png) |
| 30 | `NOTES_LOCKED_PAYWALL_MODAL` | `CHAPTER_PDF_NOTES_SCREEN` | Content & Utilities | [`screenshots/SCR_NOTES_LOCKED_PAYWALL.png`](./screenshots/SCR_NOTES_LOCKED_PAYWALL.png) |
| 31 | `REFER_AND_EARN_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Content & Utilities | [`screenshots/SCR_REFER_AND_EARN.png`](./screenshots/SCR_REFER_AND_EARN.png) |
| 32 | `TRANSACTIONS_LIST_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Content & Utilities | [`screenshots/SCR_TRANSACTIONS.png`](./screenshots/SCR_TRANSACTIONS.png) |
| 33 | `ORDER_RECEIPT_SCREEN` | `TRANSACTIONS_LIST_SCREEN` | Content & Utilities | [`screenshots/SCR_TRANSACTION_RECEIPT.png`](./screenshots/SCR_TRANSACTION_RECEIPT.png) |
| 34 | `USER_SETTINGS_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Content & Utilities | [`screenshots/SCR_USER_SETTINGS.png`](./screenshots/SCR_USER_SETTINGS.png) |
| 35 | `APP_LANGUAGE_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Content & Utilities | [`screenshots/SCR_APP_LANGUAGE.png`](./screenshots/SCR_APP_LANGUAGE.png) |
| 36 | `SAMADHAN_AI_DOUBT_SOLVER_SCREEN` | `HOME_FEED_DASHBOARD_SCREEN` | Content & Utilities | [`screenshots/SCR_NOTIFICATIONS.png`](./screenshots/SCR_NOTIFICATIONS.png) |

---

## 4. Standard `screen_view` Payload Contract

```json
{
  "event": "screen_view",
  "screen_name": "TEST_PRE_INSTRUCTIONS_SCREEN",
  "referrer_screen_name": "TEST_SERIES_OVERVIEW_SCREEN"
}
```
