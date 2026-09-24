# Testbook Android — Product Analytics Specification & Wireflow Hub

**Repository:** `manjot-testbook/TBAppScreens`  
**Application Version:** 9.11.x  
**Author:** Product & Analytics Core Team  
**Deliverables:** Interactive Visual Hub, Journey Specifications, Master Tracking CSV  

---

## 1. Executive Summary

This repository serves as the single source of truth for the **Testbook Android App Analytics Modernization Project**.

Historically, event tracking was implemented on an ad-hoc basis, resulting in over **400 bespoke event names** and fragmented parameters across WebEngage and Firebase. 

This specification establishes a **Unified 6-Event Taxonomy** and maps every interactive screen and component across the user journey with:
1. **Interactive Visual Hub (`index.html`):** Side-by-side view of actual app screenshots, numbered pins, and event contracts.
2. **Master Tracking CSV (`event_tracking_spec.csv`):** Companion spreadsheet linking every UI component directly to repository assets and property schemas.
3. **Structured Journey Specifications (`journeys/`):** Clean product specifications for each pod.

---

## 2. Master Navigation & Companion CSV

* 📥 **[Download Master Tracking CSV (`event_tracking_spec.csv`)](./event_tracking_spec.csv):** Formatted for Jira sprint imports, Google Sheets, or Excel.
* 🌐 **[Open Interactive Visual Hub (`index.html`)](./index.html):** Filter screens by journey, inspect screenshots, and copy JSON schemas.

### Product Journeys:
* 🚀 **[Journey 01: User Acquisition, Auth & Onboarding](./journeys/01_auth_onboarding.md)** (`SCR_SPLASH` ➔ `SCR_AUTH_LOGIN` ➔ `SCR_AUTH_OTP` ➔ `SCR_GOAL_ONBOARDING`)
* 🏠 **[Journey 02: Home Feed, Discovery & Global Search](./journeys/02_home_discovery.md)** (`SCR_HOME_FEED` ➔ `SCR_ENROLLED_EXAMS_SHEET` ➔ `SCR_GLOBAL_SEARCH` ➔ `SCR_SEARCH_RESULTS`)
* 📝 **[Journey 03: Assessment, Live Testing & Performance Analytics](./journeys/03_assessment_engine.md)** (`SCR_TESTS_TAB` ➔ `SCR_TEST_SERIES_OVERVIEW` ➔ `SCR_PRE_INSTRUCTIONS` ➔ `SCR_TEST_INTERFACE` ➔ `SCR_TEST_ANALYSIS`)
* 💰 **[Journey 04: Monetization, Pass Subscriptions & SuperCoaching](./journeys/04_super_pass_monetization.md)** (`SCR_SUPER_LANDING` ➔ `SCR_SUPER_PLANS` ➔ `SCR_PASS_PAYWALL` ➔ `SCR_DYNAMIC_QR` ➔ `SCR_PAYMENT_GATEWAY`)
* 📰 **[Journey 05: Daily News, Study Material, Account & Utilities](./journeys/05_account_utilities.md)** (`SCR_CURRENT_AFFAIRS` ➔ `SCR_STUDY_NOTES` ➔ `SCR_REFER_AND_EARN` ➔ `SCR_TRANSACTIONS` ➔ `SCR_APP_LANGUAGE`)

---

## 3. The Unified Event Taxonomy

Rather than inventing bespoke event names for every button and screen, client instrumentation must follow this **6-category schema**:

| Event Name | Category | Trigger Condition | Mandatory Payload Keys |
|---|---|---|---|
| `screen_view` | UI Lifecycle | Screen or modal renders in foreground | `screen_name`, `entry_source`, `previous_screen` |
| `screen_duration` | UI Lifecycle | Screen pauses or user navigates away | `screen_name`, `duration_ms` |
| `component_view` | Exposure | High-value component exposed in viewport | `screen_name`, `component_name`, `component_type` |
| `component_click` | Interaction | User taps interactive button, card, or tab | `screen_name`, `component_name`, `action`, `destination` |
| `user_action` | Input / Non-click | Search submitted, filter changed, level picked | `screen_name`, `action_name`, `action_value` |
| `state_change` | State Toggle | In-place state change (toggle, review, bookmark) | `screen_name`, `state_name`, `from_state`, `to_state` |
| `conversion` | Domain Milestone | Critical business milestones decoupled from UI | E.g. `test_started`, `test_submitted`, `checkout_started`, `payment_success`, `payment_failed` |

---

## 4. Master Screen & Asset Index

| Screen ID | Screen Display Name | Funnel Stage | Screenshot Reference |
|---|---|---|---|
| `SCR_SPLASH` | Splash & Routing Gate | App Launch | [`screenshots/01_launch.png`](./screenshots/01_launch.png) |
| `SCR_AUTH_LOGIN` | Mobile Login Entry | Authentication | [`screenshots/02_login_screen.png`](./screenshots/02_login_screen.png) |
| `SCR_AUTH_OTP` | OTP Verification | Authentication | [`screenshots/04_after_otp.png`](./screenshots/04_after_otp.png) |
| `SCR_GOAL_ONBOARDING` | Target Exam Selection | Onboarding | [`screenshots/57_onboarding_goal_selection.png`](./screenshots/57_onboarding_goal_selection.png) |
| `SCR_HOME_FEED` | Home Feed Dashboard | Core Hub | [`screenshots/06_home_feed.png`](./screenshots/06_home_feed.png) |
| `SCR_GLOBAL_SEARCH` | Global Search Screen | Discovery | [`screenshots/SCR_GLOBAL_SEARCH.png`](./screenshots/SCR_GLOBAL_SEARCH.png) |
| `SCR_SEARCH_RESULTS` | Search Results Screen | Discovery | [`screenshots/SCR_SEARCH_RESULTS.png`](./screenshots/SCR_SEARCH_RESULTS.png) |
| `SCR_ENROLLED_EXAMS_SHEET` | Enrolled Exams Filter | Personalization | [`screenshots/56_my_exams_sheet.png`](./screenshots/56_my_exams_sheet.png) |
| `SCR_NAV_DRAWER` | Side Navigation Drawer | Global Nav | [`screenshots/09_nav_drawer.png`](./screenshots/09_nav_drawer.png) |
| `SCR_TESTS_TAB` | Tests Explorer Tab | Assessment | [`screenshots/SCR_TESTS_EXPLORE_SCROLLED.png`](./screenshots/SCR_TESTS_EXPLORE_SCROLLED.png) |
| `SCR_TEST_SERIES_OVERVIEW` | Test Series Sections Detail | Assessment | [`screenshots/13_tests_landing.png`](./screenshots/13_tests_landing.png) |
| `SCR_PRE_INSTRUCTIONS` | Test Pre-Instructions & Rules | Assessment Gate | [`screenshots/15_test_instructions.png`](./screenshots/15_test_instructions.png) |
| `SCR_TEST_INTERFACE` | Live Test Taking Engine | Core Assessment | [`screenshots/18_test_interface.png`](./screenshots/18_test_interface.png) |
| `SCR_QUESTION_PALLET` | Question Pallet Drawer | Core Assessment | [`screenshots/19_question_pallet.png`](./screenshots/19_question_pallet.png) |
| `SCR_SUBMIT_CONFIRM` | Test Submit Confirmation | Assessment Gate | [`screenshots/29_test_submit_confirmation.png`](./screenshots/29_test_submit_confirmation.png) |
| `SCR_TEST_ANALYSIS` | Test Performance Scorecard | Analytics | [`screenshots/31_test_analysis.png`](./screenshots/31_test_analysis.png) |
| `SCR_TEST_SOLUTIONS` | Question Solutions Screen | Analytics Review | [`screenshots/34_test_solutions.png`](./screenshots/34_test_solutions.png) |
| `SCR_TEST_LEADERBOARD` | Test Leaderboard Podium | Social Ranking | [`screenshots/35_test_leaderboard.png`](./screenshots/35_test_leaderboard.png) |
| `SCR_SUPER_LANDING` | SuperCoaching Landing Page | Monetization | [`screenshots/38_super_coaching_tab.png`](./screenshots/38_super_coaching_tab.png) |
| `SCR_SUPER_PLANS` | SuperCoaching Plan Selection | Monetization | [`screenshots/41_super_plan_selection_full.png`](./screenshots/41_super_plan_selection_full.png) |
| `SCR_PASS_PAYWALL` | Testbook Pass Renewal & Paywall | Monetization | [`screenshots/48_pass_landing.png`](./screenshots/48_pass_landing.png) |
| `SCR_DYNAMIC_QR` | Dynamic UPI QR Code Modal | Payments | [`screenshots/53_pass_checkout.png`](./screenshots/53_pass_checkout.png) |
| `SCR_PASS_FAILURE_PAGE` | Pass Payment Failure Recovery | Payment Recovery | [`screenshots/54_pass_payment_failure.png`](./screenshots/54_pass_payment_failure.png) |
| `SCR_PAYMENT_GATEWAY` | Consolidated Payment Gateway | Payments | [`screenshots/42_make_payment_screen.png`](./screenshots/42_make_payment_screen.png) |
| `SCR_CURRENT_AFFAIRS` | Daily Current Affairs Feed | Daily Retention | [`screenshots/SCR_CURRENT_AFFAIRS.png`](./screenshots/SCR_CURRENT_AFFAIRS.png) |
| `SCR_CA_BOOKMARKS` | Saved News & Bookmarks | Daily Retention | [`screenshots/SCR_CA_BOOKMARKS.png`](./screenshots/SCR_CA_BOOKMARKS.png) |
| `SCR_STUDY_NOTES` | Study Notes Subject Overview | Study Material | [`screenshots/SCR_STUDY_NOTES.png`](./screenshots/SCR_STUDY_NOTES.png) |
| `SCR_CHAPTER_NOTES` | Chapter PDF Notes List | Study Material | [`screenshots/SCR_CHAPTER_NOTES.png`](./screenshots/SCR_CHAPTER_NOTES.png) |
| `SCR_REFER_AND_EARN` | Refer & Earn Dashboard | Growth & Rewards | [`screenshots/SCR_REFER_AND_EARN.png`](./screenshots/SCR_REFER_AND_EARN.png) |
| `SCR_TRANSACTIONS` | Transactions & Orders List | Account Billing | [`screenshots/SCR_TRANSACTIONS.png`](./screenshots/SCR_TRANSACTIONS.png) |
| `SCR_TRANSACTION_RECEIPT` | Order Invoice & Receipt | Account Billing | [`screenshots/SCR_TRANSACTION_RECEIPT.png`](./screenshots/SCR_TRANSACTION_RECEIPT.png) |
| `SCR_USER_SETTINGS` | User Account & Profile Settings| Account Settings | [`screenshots/SCR_USER_SETTINGS.png`](./screenshots/SCR_USER_SETTINGS.png) |
| `SCR_APP_LANGUAGE` | App Language Switcher | Settings | [`screenshots/SCR_APP_LANGUAGE.png`](./screenshots/SCR_APP_LANGUAGE.png) |
| `SCR_AI_DOUBT_SOLVER` | Samadhan AI Doubt Solver Chat | AI Feature | [`screenshots/SCR_NOTIFICATIONS.png`](./screenshots/SCR_NOTIFICATIONS.png) |

---

## 5. Engineering Handover Instructions

1. **Sprint Allocation:** Distribute tracking implementation by **Product Journey** (`journeys/*.md`).
2. **Auto-Injected Context:** Ensure the client-side analytics tracker auto-appends common context (`user_type`, `has_pass`, `session_id`, `screen_instance_id`) to every event.
3. **QA Verification:** Use the companion spreadsheet (`event_tracking_spec.csv`) to track validation against staging builds.
