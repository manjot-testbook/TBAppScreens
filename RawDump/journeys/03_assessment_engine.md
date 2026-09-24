# Product Journey 03: Core Assessment, Live Testing & Performance Analytics

**Owner:** Product & Assessment Pod  
**Target Platform:** Testbook Android App  

---

## 1. Journey Overview & Wireflow

This journey covers the core student assessment funnel: discovering test series, reviewing test instructions, taking a timed live exam, navigating question pallets, sectional and final submission, and reviewing comprehensive performance analytics.

```
[Tests Tab] ──▶ Test Series Sections ──▶ Pre-Instructions ──▶ Live Test Engine ──▶ Pallet Drawer ──▶ Submit Modal ──▶ Test Analysis ──┬──▶ Solutions
                                                                                                                                       └──▶ Leaderboard
```

---

## 2. Screen Specifications & Event Contracts

### Screen 09: Test Series Overview (`SCR_TEST_SERIES_OVERVIEW`)
* **Visual Reference:** `../screenshots/13_tests_landing.png`, `../screenshots/14_test_list.png`
* **Came From:** Tests Tab OR Search Results
* **Leads To:** Pre-Instructions (`SCR_PRE_INSTRUCTIONS`) or Exam Level Filter (`SCR_TEST_LEVEL_SHEET`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "test_series_overview", "series_title": "SSC Selection Post", "total_tests": 609, "free_tests": 9}`
  * **`component_click` (Start Test CTA)**
    * *Properties:* `{"screen_name": "test_series_overview", "component_name": "start_test_cta", "component_type": "button", "test_id": "6aaa6742...", "is_free": true, "destination": "test_instructions"}`

---

### Screen 10: Test Pre-Instructions (`SCR_PRE_INSTRUCTIONS`)
* **Visual Reference:** `../screenshots/15_test_instructions.png`, `../screenshots/17_lang_selected.png`
* **Came From:** Test Series Overview
* **Leads To:** Live Test Engine (`SCR_TEST_INTERFACE`) or Pass Paywall (`SCR_PASS_PAYWALL`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "test_instructions", "test_id": "6aaa6742...", "duration_mins": 60, "total_marks": 200.0}`
  * **`component_view` (Pass Upsell Strip)**
    * *Properties:* `{"screen_name": "test_instructions", "component_name": "instructions_pass_upsell", "component_type": "banner"}`
  * **`conversion` (Test Started)**
    * *Trigger:* Tapping "Agree and Continue" CTA to initialize live exam session.
    * *Properties:*
      ```json
      {
        "conversion_name": "test_started",
        "test_id": "6aaa6742...",
        "test_name": "SSC Selection Post Day-01",
        "attempt_no": 1,
        "is_free": true,
        "language": "English",
        "max_time_secs": 3600
      }
      ```

---

### Screen 11: Live Test Taking Engine (`SCR_TEST_INTERFACE`)
* **Visual Reference:** `../screenshots/18_test_interface.png`, `../screenshots/23_question_answered.png`
* **Came From:** Test Pre-Instructions
* **Leads To:** Question Pallet (`SCR_QUESTION_PALLET`), Section/Test Submit Modals
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "test_interface", "test_id": "6aaa6742...", "active_section": "General Intelligence"}`
  * **`component_click` (Save & Next CTA)**
    * *Properties:* `{"screen_name": "test_interface", "component_name": "save_and_next", "component_type": "button", "question_id": "q_102", "time_spent_secs": 15}`
  * **`state_change` (Mark for Review)**
    * *Properties:* `{"screen_name": "test_interface", "state_name": "mark_for_review", "to_state": "marked | unmarked", "question_id": "q_102"}`
  * **`component_click` (Question Pallet Drawer Toggle)**
    * *Properties:* `{"screen_name": "test_interface", "component_name": "pallet_toggle", "component_type": "icon_button", "action": "open"}`

---

### Screen 12: Question Pallet & Submission Modal (`SCR_QUESTION_PALLET` & `SCR_SUBMIT_CONFIRM`)
* **Visual Reference:** `../screenshots/19_question_pallet.png`, `../screenshots/29_test_submit_confirmation.png`
* **Came From:** Live Test Taking Engine
* **Leads To:** Test Performance Analysis (`SCR_TEST_ANALYSIS`)
* **Events to Track:**
  * **`conversion` (Test Submitted)**
    * *Trigger:* Final confirmation dialog submitted by user or automatic timer expiry.
    * *Properties:*
      ```json
      {
        "conversion_name": "test_submitted",
        "test_id": "6aaa6742...",
        "marks_obtained": 2.0,
        "total_marks": 200.0,
        "accuracy": 1.0,
        "rank": 19993,
        "total_students": 22112,
        "questions_attempted": 1,
        "questions_unattempted": 99,
        "method": "manual | auto_timer"
      }
      ```

---

### Screen 13: Test Performance Analysis Dashboard (`SCR_TEST_ANALYSIS`)
* **Visual Reference:** `../screenshots/31_test_analysis.png`, `../screenshots/32_test_analysis_metrics.png`, `../screenshots/33_test_analysis_score.png`
* **Came From:** Test Submission Confirmation
* **Leads To:** Question Solutions (`SCR_TEST_SOLUTIONS`), Leaderboard (`SCR_TEST_LEADERBOARD`), Pass Paywall (`SCR_PASS_PAYWALL`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "test_analysis", "test_id": "6aaa6742...", "score": 2.0, "rank": 19993, "percentile": 9.59}`
  * **`component_view` (Subscription Expiry Paywall Card)**
    * *Properties:* `{"screen_name": "test_analysis", "component_name": "analysis_paywall_card", "component_type": "banner", "renewal_price": 749}`
  * **`component_click` (Unlock Reattempt Mode CTA)**
    * *Properties:* `{"screen_name": "test_analysis", "component_name": "unlock_reattempt_cta", "component_type": "button", "destination": "pass_plans"}`

---

### Screen 14: Question Solutions Screen (`SCR_TEST_SOLUTIONS`)
* **Visual Reference:** `../screenshots/34_test_solutions.png`
* **Came From:** Test Performance Analysis ("Solutions" tab)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "test_solutions", "test_id": "6aaa6742..."}`
  * **`user_action` (Solution Filter Changed)**
    * *Properties:* `{"screen_name": "test_solutions", "action_name": "filter_solutions", "filter_type": "all | overtime | unattempted | correct | incorrect"}`

---

### Screen 15: Test Leaderboard Podium (`SCR_TEST_LEADERBOARD`)
* **Visual Reference:** `../screenshots/35_test_leaderboard.png`
* **Came From:** Test Performance Analysis ("Leaderboard" tab)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "test_leaderboard", "user_rank": 19993, "topper_score": 200.0}`
