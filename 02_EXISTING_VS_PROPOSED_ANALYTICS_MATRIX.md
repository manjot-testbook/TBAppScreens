# Testbook Android: Legacy vs Proposed Clean Analytics Event Matrix

**Author:** Product & Analytics Core Team  
**Scope:** Testbook Android Client v9.11.x  
**Reference Discussion:** Analytics Event Strategy (Unified Taxonomy)  
**Location:** `/Users/manjotsingh/DataspellProjects/OFFICE/OpenCode/2. Events Planning/`  

---

## 1. Context & Architectural Motivation

In the existing `appVersion/9.11.x` codebase:
* The `analytics-module/src/main/java/.../analytics_events/` directory contains **428 separate event classes** (e.g. `passpro_only_screen_visited`, `passpromax_only_screen_visited`, `CANewsReadEvent`, `CompletePendingPaymentClickedEvent`, `BannerClickedEvent`, `AddToCartNewEvent`, `CourseCurriculumClickedEvent`).
* `AllEventsNameSchemes.java` contains over 930 lines of one-off string constants.
* Every time engineering built a new button, banner, or screen, a new bespoke event was created. This caused severe data fragmentation, broken funnels, huge payload duplication across 6 downstream analytics services (`WEB_ENGAGE`, `FIREBASE`, `BRANCH`, `INTERCOM`, `MIX_PANEL`, `FB`), and exorbitant analytics tracking costs.

### The Modern Unified Taxonomy

Instead of creating hundreds of event names, we consolidate all client tracking into **6 core UI events** and **Domain/Conversion events**, with rich, standardized metadata properties:

| Event Name | Type | Trigger Condition | Example Real-world Use Case |
|---|---|---|---|
| `screen_view` | UI Event | Screen or Fragment completes transition and renders | User lands on `home`, `test_instructions`, `all_payments`, `super_landing` |
| `screen_duration` | UI Event | Screen pauses, stops, or transitions away | User spends 45,200 ms on `test_solutions` |
| `component_view` | UI Event | High-value, critical component is exposed in viewport | Expiry warning banner, paywall card, ₹1 trial strip, offer popup |
| `component_click` | UI Event | User interacts with any clickable UI element | Clicks `"Start Test"`, `"Claim Offer"`, `"Got It"`, Tab item, Bookmark |
| `user_action` | UI Event | Non-navigation interaction or complex input | Search text submitted, filter applied, exam level selected |
| `state_change` | UI Event | UI state toggled without screen change | Question marked for review, language changed, dark mode toggled |
| `conversion` / Domain Events | Business Event | Critical business milestones decoupled from UI | `test_started`, `test_submitted`, `checkout_started`, `payment_success`, `payment_failed` |

---

## 2. Common Analytics Context (Auto-Appended to Every Event)

Every event dispatched by the client MUST automatically inherit the following contextual block, eliminating repetitive manual parameters:

```json
{
  "context": {
    "app_version": "9.11.2",
    "app_build": 5262,
    "platform": "android",
    "os_version": "14",
    "device_model": "Pixel 6",
    "device_id": "83b0abe2-...",
    "session_id": "sess_1774349182",
    "user_id": "62382e83514cf6cd3b9e466b",
    "user_type": "free", 
    "has_active_pass": false,
    "has_super_subscription": false,
    "current_screen": "test_interface",
    "screen_instance_id": "sc_7182a9d",
    "previous_screen": "test_instructions",
    "target_goals": ["5e6189da5f66e94f14a21f64", "5e6189da5f66e94f14a21f54"],
    "network_type": "wifi",
    "timestamp": 1774349182359
  }
}
```

---

## 3. End-to-End Screen & Component Mapping Matrix

### 3.1. Authentication & Onboarding

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **Splash Screen (`RouterActivity`)** | `first_app_open`, `AppLaunchEvent` | `screen_view` | `screen_name: "splash"`, `entry_source: "cold_start"` |
| **Login Screen (`OTPLessLoginActivity`)** | `OnBoardingLogin`, `USER_SIGNIN` | `screen_view` | `screen_name: "login_mobile_input"` |
| **Phone Input Field** | Manual tracking / None | `user_action` | `action: "phone_number_entered"`, `phone_length: 10`, `method: "manual" \| "google_hint"` |
| **OTP Verification Screen** | `verify_otp_impression` | `screen_view` | `screen_name: "login_otp_verification"`, `otp_method: "sms"` |
| **OTP Verification Success** | `logged_in`, `signIn`, `user_update` | `conversion` (`login_success`) | `method: "otp"`, `user_id: "62382e83514cf6cd3b9e466b"`, `is_new_user: false` |
| **OTP Resend Button** | `resend_otp_clicked` | `component_click` | `component_name: "resend_otp"`, `component_type: "button"`, `resend_count: 1` |
| **Goal Selection (`OnboardingActivity`)** | `onboarding_goal_screen_visited` | `screen_view` | `screen_name: "onboarding_goal_selection"`, `source: "login" \| "feed_switcher"` |
| **Exam Chip Tap** | `ExamAddedRvEvent`, `ExamRemovedRvEvent` | `component_click` | `component_name: "exam_chip"`, `component_id: "ssc_cgl"`, `action: "select" \| "deselect"` |
| **Save Goals Button** | `self_selected_targets_saved` | `component_click` | `component_name: "save_goals"`, `component_type: "button"`, `selected_count: 2`, `goals: ["ssc_cgl", "rrb_ntpc"]` |

---

### 3.2. Home Dashboard & Navigation Shell

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **Home Feed (`HomeFragment.kt`)** | `LANDED_HOME`, `HomeFragment_visited` | `screen_view` | `screen_name: "home_feed"`, `tab_name: "home"`, `is_paid_user: false` |
| **Home Screen Duration** | Unmeasured / Disconnected | `screen_duration` | `screen_name: "home_feed"`, `duration_ms: 38200` |
| **Feature Coachmark Modal** | `revamp_ui_coachmark_shown` | `component_view` | `component_name: "exam_filter_coachmark"`, `component_type: "modal"` |
| **Coachmark "Got It" CTA** | `revamp_ui_coachmark_dismissed` | `component_click` | `component_name: "got_it"`, `component_type: "button"`, `destination: "home_feed"` |
| **Top Promotional Banner Carousel** | `BannerClickedEvent.EVENT_NAME_BANNER_IMPRESSION` | `component_view` | `component_name: "home_top_banner"`, `component_id: "creators_lab"`, `position: 0` |
| **Banner Click** | `BannerClickedEvent` (with manual params) | `component_click` | `component_name: "home_top_banner"`, `component_id: "creators_lab"`, `action: "open_deeplink"`, `destination: "https://..."` |
| **Pass Elite Trial Strip (`₹1/-`)** | `pass_elite_trial_strip_viewed` | `component_view` | `component_name: "pass_trial_strip"`, `component_type: "card"`, `trial_price: 1`, `renew_price: 799` |
| **Trial Strip CTA Click** | `pass_elite_trial_strip_clicked` | `component_click` | `component_name: "start_trial"`, `component_type: "button"`, `destination: "super_pass_plans"` |
| **Coaching Card ("Join Now")** | `RecommendedGoalCardClicked` | `component_click` | `component_name: "join_coaching_now"`, `component_type: "card"`, `product_id: "685e851a...", discount_pct: 54` |
| **Quick Action Bar (QAB) Buttons** | `qab_item_clicked` | `component_click` | `component_name: "qab_item"`, `item_title: "Live Classes" \| "Free Tests" \| "Free Quizzes"` |
| **AI Doubt Solver FAB** | `doubt_fab_clicked` | `component_click` | `component_name: "ai_doubt_solver_fab"`, `component_type: "fab"`, `destination: "ai_doubt_webview"` |
| **Navigation Drawer Open** | `nav_drawer_opened` | `user_action` | `action: "drawer_opened"`, `method: "hamburger_icon" \| "edge_swipe"` |
| **Navigation Drawer Item Click** | `CategoryVisitedEvent` (one per drawer item) | `component_click` | `component_name: "drawer_item"`, `item_title: "Pass" \| "Library" \| "Doubts" \| "Settings"` |
| **Bottom Navigation Tab Switch** | `BottomNavigation_clicked` | `component_click` | `component_name: "bottom_nav_tab"`, `tab_name: "tests" \| "super" \| "pass" \| "news"` |

---

### 3.3. Test Series & Test Taking Engine (`test-module`)

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **Test Series Sections (`TestSeriesSectionsActivity`)** | `test_series_sections_visited` | `screen_view` | `screen_name: "test_series_overview"`, `test_series_id: "6aaa674...", total_tests: 609, free_tests: 9` |
| **Level Filter Selector** | `branch_level_selected` | `user_action` | `action: "filter_level"`, `level: "All" \| "Matriculation" \| "Graduation"` |
| **Test Tab Switch** | `test_series_tab_changed` | `component_click` | `component_name: "test_type_tab"`, `tab_name: "mock_tests" \| "pyps" \| "study_notes"` |
| **Test Card "Start Test" CTA** | `start_test_cta_clicked` | `component_click` | `component_name: "start_test"`, `component_type: "button"`, `test_id: "6aaa6742...", is_free: true` |
| **Test Pre-Instructions Screen** | `test_pre_instructions_visited` | `screen_view` | `screen_name: "test_instructions"`, `test_id: "6aaa6742...", duration_mins: 60, total_marks: 200` |
| **Pass Upsell Banner Strip** | `pass_strip_viewed` | `component_view` | `component_name: "instructions_pass_upsell_strip"`, `component_type: "banner"` |
| **"Get Pass" CTA on Instructions** | `btn_get_pass_clicked` | `component_click` | `component_name: "get_pass"`, `component_type: "button"`, `destination: "pass_plans"` |
| **Instruction Language Selector** | `instructions_language_changed` | `user_action` | `action: "select_default_language"`, `language: "English" \| "Hindi"` |
| **"Agree and Continue" CTA** | `agree_and_continue_clicked` | `component_click` | `component_name: "agree_and_continue"`, `component_type: "button"`, `destination: "test_interface"` |
| **Test Attempt Start** | **`test_started`** (legacy 25+ parameters) | `conversion` (`test_started`) | `test_id: "6aaa6742...", test_name: "SSC Selection Post Day-01", target: "SSC Selection Post", attempt_no: 1, is_free: true, duration_secs: 3600` |
| **Live Test Taking Interface** | `TestInterface_visited` | `screen_view` | `screen_name: "test_interface"`, `test_id: "6aaa6742...", section: "General Intelligence"` |
| **Section Tab Switch** | `test_section_switched` | `component_click` | `component_name: "section_tab"`, `section_name: "General Awareness"` |
| **Question Option Selected** | None / local state | `user_action` | `action: "select_option"`, `question_id: "q_102", option_index: 3` |
| **"Save & Next" CTA** | `save_and_next_clicked` | `component_click` | `component_name: "save_and_next"`, `question_id: "q_102", time_spent_secs: 14` |
| **"Mark for Review" CTA** | `mark_for_review_clicked` | `state_change` | `component_name: "mark_for_review"`, `question_id: "q_102", state: "marked"` |
| **Bookmark Question Icon** | `bookmark_question_clicked` | `state_change` | `component_name: "bookmark_question"`, `question_id: "q_102", state: "bookmarked"` |
| **Question Pallet Open** | `pallet_opened` | `component_click` | `component_name: "question_pallet_toggle"`, `action: "open"` |
| **Pallet Question Grid Tap** | `pallet_question_number_clicked` | `component_click` | `component_name: "pallet_question_chip"`, `target_question_index: 14` |
| **Section Submit CTA** | `submit_section_clicked` | `component_click` | `component_name: "submit_section"`, `section_name: "General Intelligence"` |
| **Section Submit Confirmation** | `submit_section_dialog_confirmed` | `user_action` | `action: "confirm_section_submit"`, `section_name: "General Intelligence", attempted: 1, unattempted: 24` |
| **Final Test Submit CTA** | `submit_test_clicked` | `component_click` | `component_name: "submit_test"`, `attempted: 1, unattempted: 99` |
| **Test Attempt Completed** | **`test_submitted`** (legacy 30+ parameters) | `conversion` (`test_submitted`) | `test_id: "6aaa6742...", marks_obtained: 2.0, total_marks: 200.0, accuracy: 1.0, time_taken_secs: 205, rank: 19993, total_students: 22112, method: "manual"` |

---

### 3.4. Test Analysis & Solutions (`test-module`)

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **Test Analysis Dashboard** | `Solution & Analysis - Analysis`, `test_analysis_visited` | `screen_view` | `screen_name: "test_analysis"`, `test_id: "6aaa6742...", rank: 19993, score: 2.0, percentile: 9.59` |
| **Test Analysis Duration** | Unmeasured | `screen_duration` | `screen_name: "test_analysis"`, `duration_ms: 24300` |
| **Subscription Paywall Warning** | `AnalysisCutOffPitchEvent` | `component_view` | `component_name: "subscription_expiry_paywall"`, `component_type: "card"`, `renewal_price: 749, orig_price: 949` |
| **"Restore Now" CTA Button** | `analysis_paywall_restore_clicked` | `component_click` | `component_name: "restore_subscription"`, `component_type: "button"`, `destination: "pass_plans", price: 749` |
| **Reattempt Mode Upsell Card** | `unlock_reattempt_pitch_viewed` | `component_view` | `component_name: "unlock_reattempt_pitch"`, `component_type: "card"` |
| **"Unlock Reattempt Mode" CTA** | `unlock_reattempt_clicked` | `component_click` | `component_name: "unlock_reattempt_mode"`, `component_type: "button"`, `destination: "pass_plans"` |
| **Analysis Tab Switch** | `analysis_tab_switched` | `component_click` | `component_name: "analysis_tab"`, `tab_name: "solutions" \| "leaderboard"` |
| **Test Solutions Screen** | `Solution & Analysis - Solutions`, `test_solutions_visited` | `screen_view` | `screen_name: "test_solutions"`, `test_id: "6aaa6742..."` |
| **Solution Filter Chips** | `solutions_filter_selected` | `user_action` | `action: "filter_solutions"`, `filter_type: "all" \| "overtime" \| "unattempted" \| "incorrect"` |
| **Test Leaderboard Screen** | `test_leaderboard_visited` | `screen_view` | `screen_name: "test_leaderboard"`, `user_rank: 19993, topper_score: 200.0` |

---

### 3.5. SuperCoaching Subscriptions (`tb-super`)

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **SuperCoaching Landing Page** | **`supercoaching_goal_page_visited`** | `screen_view` | `screen_name: "super_landing"`, `goal_id: "685e851a...", goal_name: "UPSC EPFO APFC 2026", is_paid: false` |
| **Offer Expiration Banner** | None | `component_view` | `component_name: "offer_closing_banner"`, `component_type: "banner"`, `time_left_secs: 1798` |
| **"Claim Offer Now" Sticky CTA** | **`supercoaching_enroll_now`** | `component_click` | `component_name: "claim_offer_now"`, `component_type: "button"`, `destination: "super_plan_selection"` |
| **Plan Selection & Pricing Screen** | **`supercoaching_purchase_screen_visited`** | `screen_view` | `screen_name: "super_plan_selection"`, `goal_id: "685e851a...", subscription_type: "new_user", is_emi: false` |
| **Celebratory Coupon Modal** | `coupon_applied_popup_shown` | `component_view` | `component_name: "coupon_applied_dialog"`, `coupon_code: "EPF026", discount_pct: 16` |
| **EMI Plans Switcher** | `emi_toggle_changed` | `state_change` | `component_name: "emi_toggle"`, `is_enabled: true \| false` |
| **"Proceed to Payment" CTA** | `PROCEEDED_TO_PAYMENT`, `supercoaching_proceed_to_payment` | `conversion` (`checkout_started`) | `product_id: "685e851a...", product_type: "super_coaching", plan_duration: "6_months", amount: 3000, discount_amount: 1500, coupon: "EPF026"` |

---

### 3.6. Testbook Pass & Super Pass (`base-pass-module`)

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **Pass Landing / Renewal Page** | **`pass_screen_visited`**, `pass_tabbed_screen_visited` | `screen_view` | `screen_name: "pass_plans"`, `user_status: "expired", renewal_price: 749` |
| **Pass Expiry Warning Banner** | `pass_subscription_expired_card_viewed` | `component_view` | `component_name: "pass_expired_alert"`, `component_type: "banner"` |
| **Urgency Price Countdown Bar** | `pass_urgency_timer_seen` | `component_view` | `component_name: "pass_urgency_timer"`, `current_price: 749, next_price: 849` |
| **Included Test Preview Tab** | `pass_included_test_tab_clicked` | `component_click` | `component_name: "included_preview_tab"`, `tab_name: "test_series" \| "pyp_test" \| "study_notes"` |
| **Payment Method Quick Selector** | `pass_quick_payment_method_changed` | `user_action` | `action: "select_quick_payment_method"`, `method: "qr_code" \| "upi_intent"` |
| **"Buy Yearly Testbook Pass" CTA** | `pass_buy_now_clicked`, `PROCEEDED_TO_PAYMENT` | `conversion` (`checkout_started`) | `product_id: "yearly_pass", product_type: "pass", amount: 749, original_price: 949` |
| **Super Pass Live Modal** | `super_pass_live_modal_opened` | `screen_view` | `screen_name: "super_pass_live_modal"`, `modal_type: "intro"` |
| **"Start 2 Days Trial \| ₹1" CTA** | `super_pass_trial_clicked` | `conversion` (`trial_started`) | `product_id: "super_pass_live_trial", trial_amount: 1, recurring_amount: 649` |

---

### 3.7. Checkout & Payment Gateway (`payment-module`)

| Screen / Component | Legacy Event Intercepted / Existing Code | Proposed Unified Event | Event Payload Properties |
|---|---|---|---|
| **Payment Method Gateway Screen** | `AllPaymentsActivity_visited`, `all_payments_screen` | `screen_view` | `screen_name: "payment_gateway"`, `order_amount: 3000, product_name: "UPSC EPFO APFC"` |
| **Coupon Removal / Input** | `CouponUsedEvent`, `ApplyCouponEvent` | `user_action` | `action: "remove_coupon" \| "apply_coupon"`, `coupon_code: "EPF026"` |
| **Payment Method Selected** | **`PAYMENT_PARTNER_SELECTED_EVENT`** | `component_click` | `component_name: "payment_partner"`, `partner_type: "qr_code" \| "upi" \| "card" \| "netbanking"` |
| **Dynamic BharatQR Code Display** | `qr_code_rendered` | `component_view` | `component_name: "dynamic_upi_qr_modal"`, `expiry_seconds: 600` |
| **Payment Attempt Dispatched** | `payment_attempted` | `conversion` (`payment_attempted`) | `order_id: "ord_91823", method: "upi_qr", amount: 3000` |
| **Payment Failure Recovery Sheet** | **`PAYMENT_FAILED_EVENT`**, `PaymentFailureActivity` | `conversion` (`payment_failed`) | `order_id: "ord_91823", error_code: "USER_CANCELLED" \| "BANK_TIMEOUT", amount: 3000` |
| **Payment Failure "Try Again" CTA** | `payment_retry_clicked` | `component_click` | `component_name: "retry_payment"`, `component_type: "button"`, `retry_attempt: 2` |
| **Payment Success** | **`SUCCESS_PURCAHSE`**, `purchased`, `first_purchase` | `conversion` (`payment_success`) | `order_id: "ord_91823", transaction_id: "txn_81923", product_id: "685e851a...", product_type: "super_coaching", amount_paid: 3000, is_first_purchase: false` |

---

## 4. Summary of Benefits & Tech Pod Handover Impact

1. **Volume Reduction:** Collapsing 428 legacy classes down to 6 generic UI event types reduces client codebase maintenance by **>85%**.
2. **Deterministic Funnels:** Product funnels (e.g. `Home` ➔ `Test Overview` ➔ `Pre-Instructions` ➔ `Test Attempt` ➔ `Test Submit` ➔ `Test Analysis`) now rely on consistent `screen_view` and `conversion` definitions with `screen_name` filters, eliminating reliance on changing button IDs.
3. **Automated Component Wrappers:** Rather than requiring Android developers to write analytics lines on every button click, `component_click` is automatically issued by common design system widgets (`TrackedButton`, `TrackedCard`).
