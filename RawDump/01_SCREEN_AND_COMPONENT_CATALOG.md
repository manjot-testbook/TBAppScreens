# Testbook Android: Complete Screen & Component Catalog (Wireframe Teardown)

**Target App Version:** 9.11.2 (Branch: `appVersion/9.11.x`)  
**Package Name:** `com.testbook.tbapp`  
**Test Account Authenticated:** `+91 6333123456` (Test OTP: `859536`)  
**Date:** September 23, 2026  
**Author:** Product & Analytics Core Team  

---

## 1. Executive Architecture Overview

The Testbook Android client is a multi-module architecture comprising over 40 distinct Gradle modules (`app`, `legacy`, `login-module`, `onboarding-module`, `tb-super`, `base-pass-module`, `test-module`, `payment-module`, `analytics-module`, `ca-module`, `saved-module`, etc.).

The UI layer is a hybrid consisting of:
1. **Jetpack Compose Screens & Micro-Components:** Home Feed (`HomeFragment.kt`), Doubt Solver FAB, Coachmarks, Target Exam Selection Bottom Sheet.
2. **Traditional Android ViewBinding & XML:** Test Attempt Interface (`TestAttemptActivity`), Test Analysis (`TestAnalysis2Activity`), Navigation Drawer, Payment Gateway (`AllPaymentsActivity`).
3. **Dynamic Remote-Configured Views:** Firebase Remote Config and WebEngage in-app personalization modules driving dynamic sales pitch cards and trial strips.

---

## 2. Complete User Journey Flow Diagram

```
[App Launch] ──▶ RouterActivity ──┬─ (First Install / Logged Out) ──▶ OTPLessLoginActivity (Phone Number)
                                  │                                           │
                                  │                                           ▼
                                  │                                  VerifyOTPDialogFragment (OTP: 859536)
                                  │                                           │
                                  │                                           ▼
                                  │                                  Notification Permission Gate
                                  │                                           │
                                  │                                           ▼
                                  │                                  OnboardingActivity (Goal Selection)
                                  │                                           │
                                  └─ (Logged In) ─────────────────────────────┴─▶ DashboardActivity (Home)
                                                                                        │
         ┌──────────────────────────────┬──────────────────────────────┬────────────────┴──────────────────────────────┐
         ▼                              ▼                              ▼                                               ▼
   [Home Feed]                   [Tests Explorer]               [SuperCoaching]                                   [Pass Paywall]
  (Compose Feed)             (TestSeriesSections)             (TbSuperLanding)                                (PassOnePurchase)
         │                              │                              │                                               │
         │ (Click Test Card)            │ (Click Start Test)           │ (Claim Offer)                                 │ (Buy Pass)
         ▼                              ▼                              ▼                                               ▼
   Test Details               Pre-Instructions               Plan Selection / Coupon                        Pass Plan Selection
         │                              │                              │                                               │
         │                              ▼                              ▼                                               ▼
         │                      TestAttemptActivity             Checkout / Payment                          UPI QR / Payment
         │                      (Questions / Pallet)           (AllPaymentsActivity)                     (PassPaymentFailure)
         │                              │                              │
         │                              ▼                              ▼
         └────────────────────▶ TestAnalysis2Activity          Payment Status
                                (Score / Solutions)
```

---

## 3. Screen-by-Screen Wireframe & Component Breakdown

### 3.1. Authentication & Onboarding Flow

#### Screen 01: Splash & Routing Router
* **Technical Component:** `com.testbook.tbapp.android.router.RouterActivity`
* **Visual Attachment:** `screenshots/01_launch.png`
* **Role:** Determines authentication status (`MySharedPreferences.isLoggedIn()`), evaluates Branch deferred deeplinks, checks remote config parameters, and routes to either `OTPLessLoginActivity` or `DashboardActivity`.
* **Wireframe Components:**
  * Background image container (`com.testbook.tbapp:id/bg_image_view`)
  * Splash animation container (`com.testbook.tbapp:id/image_container`)

#### Screen 02: Login / Phone Number Input
* **Technical Component:** `com.testbook.tbapp.ui.otpless.OTPLessLoginActivity` / `EnterMobileNumberComposable`
* **Visual Attachment:** `screenshots/02_login_screen.png`, `screenshots/03_phone_entered.png`
* **Role:** Captures 10-digit mobile number, integrates Google Play Services `PhoneNumberHintActivity` assisted sign-in, and initiates OTP dispatch.
* **Wireframe Components:**
  1. **Header Label:** `"Start your preparation"` (Typography: Heading 1)
  2. **Subtitle:** `"Enter your mobile number"`
  3. **Country Code Selector:** Prefix `+91`
  4. **Mobile Input Field:** `EditText` (`bounds: [78,497][298,553]`) with placeholder `"Phone Number"`
  5. **Legal Disclaimer:** `"By entering your phone number, you agree to our T&C and Privacy Policy"`
  6. **Assisted Sign-in Sheet:** Google Phone Number Picker Modal (`bounds: [0,200][320,640]`)

#### Screen 03: OTP Verification
* **Technical Component:** `com.testbook.tbapp.ui.otpless.VerifyOTPDialogFragment` / `VerifyOTPComposable`
* **Visual Attachment:** `screenshots/04_after_otp.png`
* **Role:** Validates 6-digit OTP code, supports SMS auto-detection (`SmsBroadcastReceiver`), displays countdown timer, and offers Resend CTA.
* **Wireframe Components:**
  1. **Header Label:** `"Verify with OTP"`
  2. **Recipient Subtitle:** `"Please enter 6 digit OTP sent to +91 6333******"`
  3. **Edit Number Link:** `"change"` CTA
  4. **Detection Pill:** `"Auto-detecting OTP ..."`
  5. **6-Digit Input Boxes:** 6 distinct focusable views (`bounds: [20,321][320,377]`)
  6. **Resend Timer:** `"Resend In 43s"`

#### Screen 04: Goal Selection & Exam Onboarding
* **Technical Component:** `com.testbook.tbapp.onboarding.versionC.OnboardingActivity` / `ExamCategoriesFragment`
* **Visual Attachment:** `screenshots/57_onboarding_goal_selection.png`, `screenshots/58_onboarding_categories_scrolled.png`
* **Role:** Enables free users to select target exams (SSC, Banking, Railways, State Exams, Teaching, Engineering).
* **Wireframe Components:**
  1. **Prep Mode Toggle Pill:** `"Govt. Exams Prep."` vs `"Private Jobs Prep."`
  2. **Category Switcher Tabs:**
     * Card A: `"All Exams (19 Categories)"` (Selected)
     * Card B: `"State Exams (32 States & UTs)"`
  3. **Popular Exam Chips Rail:**
     * `[+ MPSC Group C]`, `[+ Maharashtra Police Constable]`, `[✕ SSC CGL]`, `[✕ RRB NTPC]`, `[+ SSC CHSL]`
  4. **Search Target Exams Input:** Search bar (`"🔍 Search Target Exams"`)
  5. **Category List Cards:**
     * `Teaching Exams >`
     * `Civil Services Exam >`
     * `Railways Exams >`
     * `Engineering Recruitment Exams >`
     * `Defence Exams >`
  6. **Sticky Action Bar:**
     * Exam Counter: `"2 Exams Selected"`
     * Expandable Preview: `"^ View All"`
     * Primary CTA Button: `"Save"` (`bounds: [16,582][304,618]`)

---

### 3.2. Main Navigation Shell (`DashboardActivity`)

#### Screen 05: Home Feed (Pre-Purchase / Free User View)
* **Technical Component:** `com.testbook.tbapp.android.DashboardActivity` + `legacy/src/main/java/.../HomeFragment.kt` (Jetpack Compose)
* **Visual Attachment:** `screenshots/06_home_feed.png`, `screenshots/07_home_feed_scrolled.png`, `screenshots/08_home_feed_scrolled_more.png`, `screenshots/55_home_tab.png`
* **Role:** Primary hub for test series, recommended coaching goals, free resources, and upsell touchpoints.
* **Wireframe Components:**
  1. **Top Application Bar:**
     * Drawer Toggle (`≡` hamburger menu): `[0,24][48,64]`
     * Goal Selector Chip: `"My Exams: 3 ⌵"` (`[56,42][160,61]`)
     * Search Action Icon: `[220,35][260,65]`
     * User Profile Avatar / Notification Bell: `[270,30][310,65]`
  2. **Quick Action Bar (QAB):**
     * Item 1: `"Live Classes"` (with `"FREE"` pill)
     * Item 2: `"Free Quizzes"`
     * Item 3: `"Free Tests"`
     * Item 4: `"Free Notes"`
     * Item 5: `"Free Practice"`
  3. **Promotional Carousel / Banners:** `AppBannersPagerUI` (5-sec auto-scroll, deeplink router)
  4. **Free Trial Strip:** `"2 Days trial @ just ₹ 1 /- | Renews at ₹ 799/- Valid for 90 Days"`
  5. **Exam Coverage Pill:** `"Include Exams like LIC AAO, SSC CHSL… +400 other exams"`
  6. **Coaching Recommendations:** `"Coachings handpicked for you"` / `"More Coachings for you"`
     * SuperCoaching Card: Discount badge `"54% OFF"`, Price `"₹ 69/- (Valid for 6 months)"`, `"Join Now"` CTA button
  7. **AI Doubt Solver FAB:** Floating circle button at `(275, 530)`
  8. **Bottom Navigation Bar (`content.bottomTabs`):**
     * Tab 1: `Home` (`main_button_home`)
     * Tab 2: `Tests` (`main_button_tests`)
     * Tab 3: `Super` (`main_button_super`)
     * Tab 4: `Pass` (`main_button_pass`)
     * Tab 5: `Super Pass` (`main_button_super_pass`)
     * Tab 6: `News` (`main_button_custom`)

#### Screen 06: Navigation Drawer
* **Technical Component:** `com.testbook.tbapp.android.home.MenuDrawerLayout` / `DrawerAdapter.java`
* **Visual Attachment:** `screenshots/09_nav_drawer.png`, `screenshots/10_nav_drawer_bottom.png`, `screenshots/46_drawer_open.png`
* **Role:** Global secondary navigation and account management.
* **Wireframe Components:**
  1. **User Header Card:** Initial Avatar (`"SK"`), User Name (`"Santhosh Kumar"`), Email (`"akashmegha@gmail.com"`), Phone (`"916333123456"`), `"User Settings >"` CTA
  2. **Primary Navigation List:**
     * `Home`
     * `Pass` (with prominent `"Renew Now"` badge)
     * `Previous Year Papers`
     * `Test Series`
     * `Study Notes`
     * `Super Pass`
     * `Books` (with `"NEW"` badge)
     * `Your Exams`
     * `Notification`
  3. **Secondary Utilities List:**
     * `Library` (Saved notes, bookmarked questions, offline downloads)
     * `Doubts` (with `"Ask a Doubt"` badge)
     * `Daily Current Affairs`
     * `News`
     * `Refer & Earn` (with `"Start Earning!"` label)
     * `Dark Theme Toggle` (`ON / OFF`)
     * `Language` (`English`)
     * `Promo`

#### Screen 07: Enrolled Exams Filter Bottom Sheet
* **Technical Component:** `com.testbook.tbapp.onboarding.versionC.bottomsheet.OnboardingTargetRvBottomSheetFragment`
* **Visual Attachment:** `screenshots/56_my_exams_sheet.png`
* **Role:** Quick modal allowing users to filter their home feed by active target exams or launch full exam management.
* **Wireframe Components:**
  1. Sheet Draggable Handle
  2. Title: `"Your Enrolled Exams"`
  3. Header Action Link: `"+ Add More Exams"` (opens `OnboardingActivity`)
  4. Checkbox List Items:
     * `[x] DSSSB Junior Assistant` (3-dots options menu)
     * `[x] UPSC Civil Services` (3-dots options menu)
     * `[x] SSC CHSL` (3-dots options menu)
  5. Primary CTA Button: `"Apply Filter"` (`bounds: [16,576][304,624]`)

---

### 3.3. Test Series & Examination Module (`test-module`)

#### Screen 08: Test Series Section Explorer
* **Technical Component:** `com.testbook.tbapp.android.ui.activities.testSeriesSections.TestSeriesSectionsActivity`
* **Visual Attachment:** `screenshots/13_tests_landing.png`, `screenshots/14_test_list.png`
* **Role:** Exploration of test series bundles, breakdown into test types (Mock Tests, PYPs, Subject Tests), and test attempt triggering.
* **Wireframe Components:**
  1. **Top Bar:** Back Navigation Icon, Share Icon
  2. **Exam Series Header:** `"SSC Selection Post (Phase 14) 2026 Mock Test Series"`
  3. **Count Badges:** `"609 Total Tests"`, `"9 Free Tests"`
  4. **Filter Pill:** `"Level: All ⌵"` (opens `LevelSelectionBottomSheet`)
  5. **Language Support Text:** `"Available in English, Hindi"`
  6. **Feature Badge:** `"Get your AIR, Leaderboard and more!"`
  7. **Type Selector Tabs:**
     * Tab 1: `Mock Tests` (Active)
     * Tab 2: `PYPs` (Previous Year Papers)
     * Tab 3: `Study Notes`
  8. **Section Groups Accordion:**
     * Group A: `"6 Exam Day Special"` (Pill: `"6 Free Tests"`)
     * Group B: `"32 Most Saved Qs Subject Test"`
     * Group C: `"1 Live Test"` (Pill: `"1 Free Tests"`)
  9. **Individual Test Card:**
     * Free Badge: `"FREE"`
     * Test Title: `"SSC Selection Post (Phase 14): Practice Test Day - 01"`
     * Test Meta: `"100 Qs . 60 mins . 200.0 Marks"`
     * CTA Button: `"Start Test"` (`com.testbook.tbapp:id/test_series_test_cta_tv`)
     * Footer Info: `"English, Hindi +4 more"` | `"Share"`

#### Screen 09: Test Pre-Instructions Screen
* **Technical Component:** `com.testbook.tbapp.test.testInstructions.preInstructions.PreInstructionsFragment`
* **Visual Attachment:** `screenshots/15_test_instructions.png`, `screenshots/16_choose_lang_sheet.png`, `screenshots/17_lang_selected.png`
* **Role:** Pre-flight check before opening test taking engine. Displays duration, marks, marking scheme, rules, language selection, and pass upsell.
* **Wireframe Components:**
  1. **Pass Upsell Banner Strip:** `"Get Unlimited Mock Tests, PYPs & more"` + `"Get Pass"` button (`com.testbook.tbapp:id/btn_get_pass`)
  2. **Test Title:** `"SSC Selection Post (Phase 14): Practice Test Day - 01"`
  3. **Exam Metadata:** `"Duration: 60 Mins."` | `"Maximum Marks: 200.0"`
  4. **Instruction Bullet Points:**
     * Bullet 1: 100 questions total
     * Bullet 2: 4 options, single choice
     * Bullet 3: 60 minutes overall limit
     * Bullet 4: Sectional timer rules (25 Qs in 15 mins per section)
     * Bullet 5: Marking scheme (+2.0 marks correct, -0.5 marks negative)
  5. **Default Language Selector Dropdown:** `"Choose your Default Language"` (`com.testbook.tbapp:id/select_language_cv`) -> opens `ChooseLanguageBottomSheet` (English, Hindi, Telugu, Marathi, Bengali, Tamil)
  6. **Launch CTA Button:** `"Agree and Continue"` (`com.testbook.tbapp:id/agree_and_continue_mb`)

#### Screen 10: Live Test Attempt Interface
* **Technical Component:** `com.testbook.tbapp.revampedTest.TestAttemptActivity` / `ASMTestQuestionActivity`
* **Visual Attachment:** `screenshots/18_test_interface.png`, `screenshots/22_section_b.png`, `screenshots/23_question_answered.png`
* **Role:** Core test-taking experience with question navigation, timer countdown, sectional navigation, question answering, and marking for review.
* **Wireframe Components:**
  1. **Top Header Control Bar:**
     * Pause Button: `(||)`
     * Section Countdown Clock: `00:14:12`
     * Truncated Test Title: `SSC Selection Post (Phase ...)`
     * On-the-fly Question Language Toggle: `[E / अ]`
     * Question Pallet Drawer Toggle: `[≡]` (`bounds: [280,30][315,65]`)
  2. **Section Tabs Rail:**
     * Tab A: `General Intelligence` (Active)
     * Tab B: `General Awareness`
     * Tab C: `Quantitative Aptitude`
     * Tab D: `English Language`
  3. **Status Banner:**
     * Questions Answered Pill: `"Total Questions Answered: 0"`
     * Time Alert Pill: `"Last 15 Mins"`
  4. **Question Card Header:**
     * Question Number Badge: `1`
     * Question-Level Elapsed Timer: `00:47`
     * Bookmark Question Icon: `[Bookmark]`
     * Report / Star Icon: `[Star]`
  5. **Question Body Container:**
     * Formatted question statement (HTML / MathJax support)
  6. **Option Selector Radio Cards:**
     * Option 1 Card: `"1. 481"`
     * Option 2 Card: `"2. 409"`
     * Option 3 Card: `"3. 524"`
     * Option 4 Card: `"4. ..."`
  7. **Bottom Action Footer Bar:**
     * `Previous` Button (appears on Q2+)
     * `Mark For Review` / `Unmark Review` Button
     * `Save & Next` Primary Action Button

#### Screen 11: Question Pallet & Submission Drawer
* **Technical Component:** `com.testbook.tbapp.test.asm.asmDrawerNavigation.fragment.ASMTestQuestionNavigationFragment`
* **Visual Attachment:** `screenshots/19_question_pallet.png`, `screenshots/26_final_section_pallet.png`, `screenshots/28_section_d_pallet.png`
* **Role:** Overview of entire test progress across sections, jumping directly to any question, and triggering sectional or final submission.
* **Wireframe Components:**
  1. **Utility Bar:** `? Symbols` (opens symbol guide) | `i Instructions` (opens full instructions modal)
  2. **Section Filter Pills:** `[PART - A]`, `[PART - B]`, `[PART - C]`, `[PART - D]`
  3. **Section Header:** Section Name (`"General Intelligence"`)
  4. **Status Legend Box:**
     * Green indicator: `"Answered Qs: 0"`
     * Blue indicator: `"Unanswered Qs: 25"`
  5. **Question Grid (5x5):** Matrix of circular/square question buttons (1 to 25) with current question pointer arrow
  6. **Submission Controls:**
     * `SUBMIT SECTION` Button (Active on intermediate sections)
     * `SUBMIT TEST` Button (Active on final section or full-test mode)

#### Screen 12: Section & Test Submission Dialogs
* **Technical Component:** `com.testbook.tbapp.test.asm.sectionSummary.fragment.ASMTestSectionsSummaryDialogFragment` / `ASMTestSubmitDialogFragment`
* **Visual Attachment:** `screenshots/21_submit_section_dialog.png`, `screenshots/29_test_submit_confirmation.png`
* **Role:** Modal confirming user intent before irreversibly closing a section or submitting the test.
* **Wireframe Components:**
  1. Modal Dialog Container
  2. Stat Row 1: Time Left (`00:13:14`)
  3. Stat Row 2: Attempted count (`0`)
  4. Stat Row 3: Unattempted count (`25`)
  5. Stat Row 4: Marked count (`1`)
  6. Prompt Text: `"Are you sure you want to submit the section?"` / `"Are you sure you want to submit the test?"`
  7. Buttons: `[Yes]` (Primary Blue) | `[No]` (Secondary Grey)

#### Screen 13: Test Analysis & Performance Report
* **Technical Component:** `com.testbook.tbapp.test.analysis2.TestAnalysis2Activity` / `TestProficiencyAnalysisFragment`
* **Visual Attachment:** `screenshots/31_test_analysis.png`, `screenshots/32_test_analysis_metrics.png`, `screenshots/33_test_analysis_score.png`
* **Role:** Comprehensive post-test performance breakdown, comparative benchmarking, and pass/reattempt conversion triggers.
* **Wireframe Components:**
  1. **Top Bar:** Back Arrow, Test Name, Language Switcher, Drawer Action Toggle
  2. **Ad / Promotional Carousel:** Testbook Creators Lab Banner (`"Your Story Their Inspiration - Earn ₹50"`)
  3. **Report Tabs:**
     * Tab 1: `Analysis` (Active)
     * Tab 2: `Solutions`
     * Tab 3: `Leaderboard`
  4. **Subscription Paywall & Expiry Warning Component:**
     * Banner: `"Your subscription has Expired ⚠️"`
     * Pricing: `"Your Renewal Price ₹749 (struck through ₹949)"`
     * Urgency Timer: `"Price Increasing to ₹849 in 09:59:11"`
     * Action CTA: `"Restore Now at ₹749 for 1 year"`
  5. **Reattempt Upsell Card:**
     * Headline: `"Want to become a Top Ranker? Reattempt. Improve. Achieve"`
     * Feature: `"Get Unlimited Reattempts for All Tests"`
     * CTA: `"Unlock Reattempt Mode"`
  6. **Core Metrics Scorecard:**
     * **Rank:** `19993 / 22112`
     * **Score:** `2 / 200` (Average: `69.07`, Best: `200`)
     * **Percentile:** `9.59 %`
     * **Accuracy:** `100 %`
     * **Attempt Distribution:** `Qs. Attempted: 1 / 100` (`Correct: 1`, `Incorrect: 0`, `Unattempted: 99`)

#### Screen 14: Test Solutions Screen
* **Technical Component:** `com.testbook.tbapp.test.solutions.TestSolutionsFragment`
* **Visual Attachment:** `screenshots/34_test_solutions.png`
* **Role:** Question-by-question review with explanations, answer keys, bookmarking, and reporting.
* **Wireframe Components:**
  1. **Filter Chips Rail:** `[All (100)]` (Selected), `[Overtime (3)]`, `[Unattempted (99)]`, `[Correct]`, `[Incorrect]`
  2. **Section Header:** `"GENERAL INTELLIGENCE / 25 Questions"`
  3. **Question Solution Card:**
     * Question Number (`1`)
     * Time spent tag (`1:52`)
     * Global Accuracy Benchmark (`65% got it right`)
     * Bookmark Icon
     * Question text snippet
  4. **Floating Action Button:** `"Sections"` bottom picker

#### Screen 15: Test Leaderboard Screen
* **Technical Component:** `com.testbook.tbapp.test.leaderboard.TestLeaderBoardFragment`
* **Visual Attachment:** `screenshots/35_test_leaderboard.png`
* **Role:** Social comparison and rank visualization against the test population.
* **Wireframe Components:**
  1. **Top Rankers Podium:**
     * Rank 1 Avatar: "Raja" (`200 / 200`)
     * Rank 2 Avatar: "Hemant" (`195 / 200`)
     * Rank 3 Avatar: "Vivek" (`193.5 / 200`)
  2. **Sticky User Rank Bottom Bar:**
     * Rank Badge: `19993`
     * User Avatar + Label: `"Santhosh Kumar (You)"`
     * Score: `2.0 / 200.0 Marks`

---

### 3.4. SuperCoaching Module (`tb-super`)

#### Screen 16: SuperCoaching Pre-Purchase Landing Page
* **Technical Component:** `com.testbook.tbapp.tb_super.landingScreen.TbSuperLandingActivity` / `TbSuperLandingFragment`
* **Visual Attachment:** `screenshots/38_super_coaching_tab.png`, `screenshots/39_super_coaching_scrolled.png`
* **Role:** Primary sales and value proposition page for goal coaching subscriptions.
* **Wireframe Components:**
  1. **Top Bar:** Navigation Drawer icon, SuperCoaching brand logo
  2. **Hero Banner:** Full-width promotional banner with goal title (`"UPSC EPFO APFC 2026"`), key stats (100+ Tests, 75+ Notes, 15+ Subjects, India's Top Teachers)
  3. **Offer Expiration Banner:** Red banner `"Offer Expires in 00:29:58 | Grab Now!"`
  4. **Personalization Card:** `"Hi Santhosh Kumar! 👋 Great offer for you, Grab now!"`
  5. **Urgency Pitch:** `"OFFER CLOSING SOON - On UPSC EPFO APFC 2026 SuperCoaching"`
  6. **Primary Sticky CTA:** `"Claim Offer Now"` (`bounds: [20,580][300,625]`)

#### Screen 17: SuperCoaching Plan Selection & Coupon Sheet
* **Technical Component:** `com.testbook.tbapp.tb_super.ui.goalsubscription.GoalSubscriptionActivity`
* **Visual Attachment:** `screenshots/40_super_plan_selection.png`, `screenshots/41_super_plan_selection_full.png`
* **Role:** Selection of subscription duration (6 Months, 12 Months), EMI options, and coupon management.
* **Wireframe Components:**
  1. **Coupon Applied Overlay Dialog:**
     * Confetti animation
     * Coupon Badge Graphic
     * Header: `"COUPON APPLIED"`
     * Discount Text: `"You got 16% Off with this coupon"`
  2. **Goal Header:** SuperCoaching Logo, `"UPSC EPFO APFC 2026"`
  3. **Goal Features Grid:**
     * `10+ Courses by Super Teachers`
     * `75+ Study Notes`
     * `100+ Mock Tests`
     * `70+ Practice Tests`
  4. **Coupon Card:** `"Offer Closing Soon - EPFO Complete Course - Now at ₹3,000 [Apply / Remove]"` | Action Link: `"Apply Coupon"`
  5. **EMI Switcher:** `"No Cost EMI available - View EMI Plans"` toggle switch
  6. **Plan Option Cards:** `"Recommended"`, `"Your total savings: ₹1,500"`, `"Pay in 2 EMIs of ₹1500"`
  7. **Sticky Checkout Bar:**
     * Struck-through Price: `₹4,500`
     * Final Payable Price: `₹3,000`
     * CTA Button: `"Proceed to Payment"` (`bounds: [120, 600][305, 635]`)

---

### 3.5. Pass & Super Pass Module (`base-pass-module`)

#### Screen 18: Testbook Pass Landing & Renewal Page
* **Technical Component:** `com.testbook.tbapp.base_pass.passOne.PassOnePurchaseActivity` / `PassOnePurchaseFragment`
* **Visual Attachment:** `screenshots/48_pass_landing.png`, `screenshots/49_pass_plans.png`, `screenshots/50_pass_plan_durations.png`, `screenshots/51_pass_vs_passpro.png`, `screenshots/52_pass_coupons_faq.png`
* **Role:** Comprehensive purchase page for Testbook Pass & Pass Pro subscriptions with feature matrices and pricing options.
* **Wireframe Components:**
  1. **Mission Officer Hero Graphic:** Testbook Pass phone mockup, `"900+ Exams, 1.5 Lakh+ Mock Tests, 30,000+ PYPs, 3,500+ Free Tests"`, `"Buy Now"` button
  2. **Subscription Expiry Alert:** Pink card: `"⚠️ Your Pass Subscription has expired!"`
  3. **Renewal Pricing Header:** `"Your Renewal Price ₹749 (struck through ₹949)"`
  4. **Urgency Countdown Bar:** Orange bar: `"Hurry ! Price increasing to ₹849 in 09:51:39"`
  5. **Feature Benefit Grid (2x3):**
     * `150,000+ Mock Tests with Re-attempt mode`
     * `30,000+ Previous Year papers`
     * `Rankers Test Series`
     * `10,000+ Study Notes`
     * `Realtime Doubt Support`
     * `Unlimited Practice Questions`
  6. **Plan Card:** `"Yearly Testbook Pass - ₹749"`
  7. **Social Proof:** `"Trusted by 3.6 Crore+ Students"`
  8. **Included Tests Preview Tabs:** `[Test Series]` | `[PYP Test]` | `[Study Notes]` with preview test cards (e.g. SSC CHSL, CA 2026 Mega Pack, SSC Maths PYP)
  9. **Sticky Purchase Bar:**
     * Payment Method Selector: `"Pay using QR Code [Change >]"`
     * Price: `₹749`
     * Primary CTA: `"Buy Yearly Testbook Pass"` (`bounds: [90, 595][305, 635]`)

#### Screen 19: Super Pass Live Trial & Plans Sheet
* **Technical Component:** `com.testbook.tbapp.base_pass.passOne.PassOneBottomSheetFragment` / `SuperPassOfferingActivity`
* **Visual Attachment:** `screenshots/59_super_pass_tab.png`, `screenshots/60_super_pass_plans.png`, `screenshots/61_news_tab.png`
* **Role:** Entry funnel for the new hybrid "Super Pass Live" tier combining live classes and test series.
* **Wireframe Components:**
  1. Modal Close Icon `(✕)`
  2. Banner: `"✨ Introducing ✨ testbook LIVE"`
  3. Video Explainer: Faculty introduction video
  4. Exam Coverage Badge: `"✨ Includes 497+ Exams like UPPCL Executive Assistant... +495 ✨"`
  5. Feature Matrix:
     * `Live Foundation for...`
     * `Free Pass`
     * `Crash Courses & Mock Test`
     * `24*7 AI Doubt Solver`
  6. Trial Pitch Card: `"Super Pass Live - Trial: Valid for 2 Days then ₹649 for 90 days"` | `₹1`
  7. Annual Plan Card: `"12 Months - Super Pass Live: ₹1,999 (struck through ₹2,499)"`
  8. Sticky CTA: `"Start 2 Days Trial | ₹1"`

---

### 3.6. Payment Gateway & Checkout (`payment-module`)

#### Screen 20: Make Payment & Payment Method Selection
* **Technical Component:** `com.testbook.tbapp.allPayments.activity.AllPaymentsActivity` / `AllPaymentFragment`
* **Visual Attachment:** `screenshots/42_make_payment_screen.png`
* **Role:** Consolidated payment gateway integrating Juspay, Razorpay, UPI intent, Cards, and Netbanking.
* **Wireframe Components:**
  1. **Toolbar:** Back Arrow, Title `"Make Payment"`
  2. **Order Summary Card:**
     * SuperCoaching / Pass Logo
     * Product Description: `"UPSC EPFO APFC 2026 - 6 Months"`
     * Price Breakdown: Original `₹4500`, Payable `₹3000`
     * Coupon Tag: `"Coupon Applied: [EPF026 ✕] - ₹ 1500"`
     * Price Accordion Dropdown: `"To Pay ⌵ ₹ 3000"`
  3. **UPI Payment Method Card:**
     * Item: `"Scan QR Code - Pay using any UPI app >"`
     * (Installed UPI Apps: Google Pay, PhonePe, Paytm, BHIM)
  4. **Card Payment Method Card:**
     * Item: `"Pay with Debit / Credit Card - Visa, Mastercard, Rupay & more >"`
  5. **Netbanking Method Card:**
     * Popular bank icons + Other Banks selector

#### Screen 21: Dynamic UPI QR Code Modal
* **Technical Component:** `com.testbook.tbapp.allPayments.fragment.AllPaymentFragment` (QR Sub-view)
* **Visual Attachment:** `screenshots/53_pass_checkout.png`
* **Role:** Displays on-screen dynamic BharatQR / UPI QR code for cross-device desktop/mobile payment.
* **Wireframe Components:**
  1. Top App Crest
  2. Title: `"Scan the QR Code"`
  3. Dynamic QR Image Container (`240x240 dp`)
  4. Expiry Countdown Clock: `"This QR code is valid for another 9:49 Minutes"`

#### Screen 22: Payment Failure & Drop-off Recovery
* **Technical Component:** `com.testbook.tbapp.payment_module.PaymentFailureActivity` / `PassPaymentFailureActivity`
* **Visual Attachment:** `screenshots/43_qr_payment.png`, `screenshots/54_pass_payment_failure.png`
* **Role:** Intercepts failed transactions, explains error cause, and immediately presents retries to minimize checkout abandonment.
* **Wireframe Components:**
  1. Alert Graphic: Red exclamation card icon
  2. Title: `"Transaction Failed!"` / `"Your Payment Failed"`
  3. Subtitle: `"Unfortunately something went wrong during payment. Please Retry or select a different payment method."`
  4. Value Props Reminder Card: 150,000+ Mock Tests, 30,000+ PYPs
  5. Recovery Buttons:
     * Button 1: `"Try Again"` (Secondary outline / white)
     * Button 2: `"Try different payment method"` (Primary blue)
     * Quick Checkout Bar: `"Pay using QR Code [Change >]"` + `"Buy Yearly Testbook Pass"`

---

## 4. Free User (Pre-Purchase) vs Paid User (Post-Purchase) Teardown

| Dimension | Pre-Purchase (Free User) | Post-Purchase (Paid User) |
|---|---|---|
| **Home Screen Feed** | Dominated by promotional carousels, incomplete payment cards, Pass sales pitches (`PassOnePitchCardData`), trial strips (`₹1 trial`), and recommended coaching goals. | Transformed into an active learning workspace: `"Continue Learning"` card, today's Live Classes schedule, active enrolled courses list (`PurchasedGoalsUIModel`), test series progress, and Pass validity badge. |
| **SuperCoaching Tab** | Sales landing page (`TbSuperLandingFragment`): Hero banners, urgency timers, demo videos, faculty credentials, curriculum overview, "Claim Offer" sticky CTA. | Learning dashboard (`SuperPurchasedActivity` / `SuperPurchasedDashboardFragment`): Course modules, subject-wise video lectures, downloaded classes, live doubt sessions, mentorship slots, and study notes. |
| **Test Series & Tests** | Only tests tagged `"FREE"` can be attempted. Locked tests trigger `TestSeriesLockedDialogFragment` or `PassOnePurchaseActivity` paywall. | All 600+ mock tests, previous year papers, and chapter tests are unlocked with unlimited reattempt mode enabled. |
| **Test Analysis & Report** | Displays basic score and rank, but injects an intrusive renewal/paywall banner (`"Your subscription has Expired ⚠️"`) and locks advanced percentile and reattempt analytics behind paywalls. | Displays comprehensive test analysis: detailed subject breakdown, speed vs accuracy charts, question-level time comparison against the topper, and full solution unlock. |
| **Drawer Navigation** | Displays prominent `"Renew Now"` tags on Pass and promotional badges on courses. | Shows active subscription status, `"My Purchases"`, and quick access to saved offline items in `Library`. |

---

## 5. Technical Wireframe Asset Index

All 30+ high-resolution screenshots generated in this teardown session are stored locally:
* **Location:** `/Users/manjotsingh/DataspellProjects/OFFICE/OpenCode/2. Events Planning/screenshots/`

| Filename | Screen Description |
|---|---|
| `01_launch.png` | Splash / RouterActivity loading |
| `02_login_screen.png` | Phone number input & Google Phone Hint |
| `03_phone_entered.png` | Mobile number populated |
| `04_after_otp.png` | 6-Digit OTP verification with countdown timer |
| `05_after_permission.png` | Android 14 notification permission dialog |
| `06_home_feed.png` | Home screen initial render with feature coachmark |
| `07_home_feed_scrolled.png` | Home feed scrolled: Pass Elite trial strip (₹1/-) |
| `08_home_feed_scrolled_more.png` | Home feed scrolled: Recommended coaching goals |
| `09_nav_drawer.png` | Navigation drawer top: User profile & Pass Renew tag |
| `10_nav_drawer_bottom.png` | Navigation drawer bottom: Library, Doubts, Refer & Earn |
| `11_tests_tab.png` | Test Series tab initial view |
| `12_tests_tab.png` | Exam level selection bottom sheet |
| `13_tests_landing.png` | Test series landing page with 609 total tests |
| `14_test_list.png` | Test list view with Free tests and "Start Test" CTA |
| `15_test_instructions.png` | Pre-instructions screen with Pass upsell banner |
| `16_choose_lang_sheet.png` | Instruction language selection bottom sheet |
| `17_lang_selected.png` | English selected on instructions screen |
| `18_test_interface.png` | Live test taking interface (Q1, Section A, Timer) |
| `19_question_pallet.png` | Question pallet drawer with 5x5 grid and section chips |
| `20_test_submit_dialog.png` | Submit section / test prompt |
| `21_submit_section_dialog.png` | Section submit confirmation with attempt counts |
| `22_section_b.png` | Section B (General Awareness) attempt view |
| `23_question_answered.png` | Question answered state with Previous / Next CTAs |
| `24_section_c.png` | Section C (Quantitative Aptitude) |
| `25_section_d.png` | Section D (English Language) |
| `26_final_section_pallet.png` | Pallet on Section C |
| `28_section_d_pallet.png` | Pallet on Section D with Submit Test active |
| `29_test_submit_confirmation.png` | Final test submission confirmation dialog |
| `30_test_submitted_loading.png` | Test submission processing |
| `31_test_analysis.png` | Test analysis report top view with renewal paywall |
| `32_test_analysis_metrics.png` | Reattempt mode upsell card |
| `33_test_analysis_score.png` | Core scorecard: Rank, Score, Percentile, Accuracy |
| `34_test_solutions.png` | Test solutions tab with question cards and filters |
| `35_test_leaderboard.png` | Test leaderboard podium (Top 3) and user rank |
| `38_super_coaching_tab.png` | SuperCoaching landing page (Hero, Urgency banner) |
| `39_super_coaching_scrolled.png` | SuperCoaching landing scrolled |
| `40_super_plan_selection.png` | SuperCoaching coupon applied celebratory dialog |
| `41_super_plan_selection_full.png`| SuperCoaching plan selection & EMI toggle |
| `42_make_payment_screen.png` | Consolidated checkout screen (UPI, Cards, Netbanking) |
| `43_qr_payment.png` | Payment failure bottom sheet with retry CTAs |
| `46_drawer_open.png` | Navigation drawer re-verified |
| `48_pass_landing.png` | Testbook Pass renewal landing page |
| `49_pass_plans.png` | Pass benefits grid and renewal pricing |
| `50_pass_plan_durations.png` | Yearly pass plan card and urgency banner |
| `51_pass_vs_passpro.png` | Pass included test series list |
| `52_pass_coupons_faq.png` | View All Test Series & Student social proof |
| `53_pass_checkout.png` | Dynamic UPI QR code modal |
| `54_pass_payment_failure.png` | Dedicated Pass payment failure recovery screen |
| `55_home_tab.png` | Home feed top bar & AI doubt solver FAB |
| `56_my_exams_sheet.png` | "My Exams" enrolled target bottom sheet |
| `57_onboarding_goal_selection.png` | Full onboarding target exam selection screen |
| `58_onboarding_categories_scrolled.png`| Exam categories list (Teaching, Civil, Railways) |
| `59_super_pass_tab.png` | Super Pass Live modal introduction |
| `60_super_pass_plans.png` | Super Pass Live trial pricing (₹1/-) |
| `61_news_tab.png` | Super Pass Live trial plan selection screen |
