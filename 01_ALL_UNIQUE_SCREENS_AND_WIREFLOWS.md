# Testbook Android: Master Catalog of Unique Screens & Complete Wireflows

**App Version:** 9.11.2 (Branch: `appVersion/9.11.x`)  
**Package:** `com.testbook.tbapp`  
**Target Output Directory:** `/Users/manjotsingh/DataspellProjects/OFFICE/OpenCode/2. Events Planning/`  
**Screenshot Assets Directory:** `/Users/manjotsingh/DataspellProjects/OFFICE/OpenCode/2. Events Planning/screenshots/`  
**Total Unique Screens Cataloged:** 36 Core Production Screens & Modals  

---

## 1. Complete Wireflow Diagram (Navigation Graph)

```
                                      [APP LAUNCH]
                                           │
                                           ▼
                                    01. SCR_SPLASH
                                    (RouterActivity)
                                           │
                        ┌──────────────────┴──────────────────┐
                        │ (Logged Out / First Install)        │ (Logged In)
                        ▼                                     │
               02. SCR_AUTH_LOGIN                             │
             (OTPLessLoginActivity)                           │
                        │ (Submit Phone)                      │
                        ▼                                     │
                03. SCR_AUTH_OTP                              │
           (VerifyOTPDialogFragment)                          │
                        │ (Verify 859536)                     │
                        ▼                                     │
             04. SCR_GOAL_ONBOARDING                          │
              (OnboardingActivity)                            │
                        │ (Save Selected Goals)               │
                        └──────────────────┬──────────────────┘
                                           │
                                           ▼
                                   05. SCR_HOME_FEED ◀────────────────────────────────────────────────────────────────────────┐
                                   (DashboardActivity)                                                                        │
                                           │                                                                                  │
      ┌─────────────────────┬──────────────┴──────┬──────────────────────────┬────────────────────────────┐                   │
      ▼                     ▼                     ▼                          ▼                            ▼                   │
 [TOP BAR ACTIONS]     [DRAWER MENU]        [BOTTOM TABS]             [QUICK ACTION BAR]           [PROMO / UPSELL]           │
      │                     │                     │                          │                            │                   │
      ├──▶ 06. SEARCH       ├──▶ 09. SETTINGS     ├──▶ 18. TESTS_TAB         ├──▶ 14. FREE_QUIZZES        ├──▶ 27. PASS_PAYWALL
      │         │           │                     │         │                │                            │          │        │
      │         ▼           ├──▶ 10. CURRENT_     │         ▼                ├──▶ 15. FREE_PRACTICE       │          ▼        │
      │    07. SEARCH_      │        AFFAIRS      │    19. TEST_SERIES_      │                            │    28. PASS_PLANS │
      │        RESULTS      │         │           │        OVERVIEW          └──▶ 16. STUDY_NOTES         │          │        │
      │                     │         ▼           │         │                          │                  │          ▼        │
      ├──▶ 08. MY_EXAMS_    │    11. SAVED_NEWS   │         ├──▶ 20. LEVEL_SHEET       ▼                  │    29. DYNAMIC_QR │
      │        SHEET        │                     │         │                     17. CHAPTER_NOTES       │          │        │
      │         │           ├──▶ 12. REFER_EARN   │         ▼                          │                  │          ▼        │
      │         ▼           │                     │    21. PRE_INSTRUCTIONS            ▼                  │    30. PASS_FAILURE
      │    04. GOAL_        ├──▶ 13. TRANSACTIONS │         │                     27. PASS_PAYWALL        │          │        │
      │        ONBOARDING   │         │           │         ▼                                             │          ▼        │
      │                     │         ▼           │    22. TEST_INTERFACE                                 │    31. CHECKOUT   │
      └──▶ 36. AI_DOUBT_    │    34. TRANSACTION_ │         │                                             │                   │
               SOLVER       │        RECEIPT      │         ├──▶ 23. QUESTION_PALLET                      ├──▶ 25. SUPER_     │
                            │                     │         │         │                                   │        LANDING    │
                            └──▶ 35. APP_LANGUAGE │         │         ▼                                   │          │        │
                                                  │         │    24. SUBMIT_CONFIRM                       │          ▼        │
                                                  │         │         │                                   │    26. SUPER_PLANS│
                                                  │         │         ▼                                   │          │        │
                                                  │         └──▶ 32. TEST_ANALYSIS                        │          ▼        │
                                                  │                   │                                   └──▶ 31. CHECKOUT   │
                                                  │                   ├──▶ 33. TEST_SOLUTIONS                        │        │
                                                  │                   └──▶ 34. TEST_LEADERBOARD                      ├──▶ 29. QR
                                                  │                                                                  │
                                                  ├──▶ 25. SUPER_LANDING ────────────────────────────────────────────┤
                                                  │                                                                  │
                                                  ├──▶ 27. PASS_PAYWALL ─────────────────────────────────────────────┤
                                                  │                                                                  │
                                                  └──▶ 31. CHECKOUT ─────────────────────────────────────────────────┴────────┘
```

---

## 2. Master Catalog of Unique Screens

---

### Screen 01: Splash & Initial Routing
* **Screen ID:** `SCR_SPLASH`
* **Technical Entity:** `com.testbook.tbapp.android.router.RouterActivity`
* **Category:** System / Launch Gate
* **Visual Reference:** `screenshots/01_launch.png`
* **Wireflow Connections:**
  * **Incoming From:** OS App Launch (Cold Start / Launcher Icon / Branch DeepLink)
  * **Outgoing To:**
    * ➔ `SCR_AUTH_LOGIN` (If `MySharedPreferences.isLoggedIn() == false`)
    * ➔ `SCR_HOME_FEED` (If user is authenticated and onboarded)
    * ➔ `SCR_GOAL_ONBOARDING` (If user is authenticated but target goals are empty)
* **Wireframe Components:**
  * Background full-screen image (`bg_image_view`)
  * Animated Brand Logo container (`image_container`)
  * Headless Branch initialization & deferred deeplink resolution listener

---

### Screen 02: Mobile Login Entry
* **Screen ID:** `SCR_AUTH_LOGIN`
* **Technical Entity:** `com.testbook.tbapp.ui.otpless.OTPLessLoginActivity`
* **Category:** Authentication
* **Visual Reference:** `screenshots/02_login_screen.png`, `screenshots/03_phone_entered.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_SPLASH` (unauthenticated state)
  * **Outgoing To:**
    * ➔ `SCR_AUTH_OTP` (Upon entering 10-digit mobile number)
    * ➔ External Terms / Privacy browser
* **Wireframe Components:**
  * Header Title: `"Start your preparation"`
  * Subtitle: `"Enter your mobile number"`
  * Country Code Selector: `+91` prefix
  * Phone Input Field: `EditText` with hint `"Phone Number"`
  * Assisted Sign-in Dialog: Google Play Services phone hint modal (`PhoneNumberHintActivity`)
  * Disclaimer: `"By entering your phone number, you agree to our T&C and Privacy Policy"`

---

### Screen 03: OTP Verification
* **Screen ID:** `SCR_AUTH_OTP`
* **Technical Entity:** `com.testbook.tbapp.ui.otpless.VerifyOTPDialogFragment`
* **Category:** Authentication
* **Visual Reference:** `screenshots/04_after_otp.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_AUTH_LOGIN`
  * **Outgoing To:**
    * ➔ `SCR_GOAL_ONBOARDING` (First time user)
    * ➔ `SCR_HOME_FEED` (Returning user)
    * ➔ `SCR_AUTH_LOGIN` (Tapping `"change"` phone number)
* **Wireframe Components:**
  * Title: `"Verify with OTP"`
  * Subtitle: `"Please enter 6 digit OTP sent to +91 6333******"`
  * Action Link: `"change"` (edits mobile number)
  * Status Pill: `"Auto-detecting OTP ..."`
  * 6 Discrete Digit Boxes: Focusable input views for digits
  * Countdown Timer: `"Resend In 43s"`

---

### Screen 04: Goal Selection & Onboarding
* **Screen ID:** `SCR_GOAL_ONBOARDING`
* **Technical Entity:** `com.testbook.tbapp.onboarding.versionC.OnboardingActivity` / `ExamCategoriesFragment`
* **Category:** Onboarding / Personalization
* **Visual Reference:** `screenshots/57_onboarding_goal_selection.png`, `screenshots/58_onboarding_categories_scrolled.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_AUTH_OTP` (Post-login) OR `SCR_ENROLLED_EXAMS_SHEET` (via `+ Add More Exams`)
  * **Outgoing To:**
    * ➔ `SCR_HOME_FEED` (Tapping `"Save"` button)
    * ➔ `SCR_GLOBAL_SEARCH` (Tapping `"Search Target Exams"` bar)
* **Wireframe Components:**
  * Prep Mode Toggle: `"Govt. Exams Prep."` vs `"Private Jobs Prep."`
  * Category Switcher: `"All Exams (19 Categories)"` vs `"State Exams (32 States & UTs)"`
  * Popular Exam Chips: `[+ MPSC Group C]`, `[+ Maharashtra Police Constable]`, `[✕ SSC CGL]`, `[✕ RRB NTPC]`
  * Search Bar: `"🔍 Search Target Exams"`
  * Exam Category Cards: `Teaching Exams >`, `Civil Services Exam >`, `Railways Exams >`, `Engineering Exams >`
  * Sticky Bottom Bar: Counter `"2 Exams Selected"`, `"^ View All"`, Primary Button `"Save"`

---

### Screen 05: Home Feed Dashboard (Free / Pre-Purchase View)
* **Screen ID:** `SCR_HOME_FEED`
* **Technical Entity:** `com.testbook.tbapp.android.DashboardActivity` + `HomeFragment.kt` (Compose)
* **Category:** Core Hub
* **Visual Reference:** `screenshots/06_home_feed.png`, `screenshots/07_home_feed_scrolled.png`, `screenshots/08_home_feed_scrolled_more.png`, `screenshots/55_home_tab.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_SPLASH`, `SCR_GOAL_ONBOARDING`, or any Bottom Tab switch
  * **Outgoing To:**
    * ➔ `SCR_NAV_DRAWER` (Tapping hamburger `≡`)
    * ➔ `SCR_ENROLLED_EXAMS_SHEET` (Tapping `"My Exams: 3 ⌵"`)
    * ➔ `SCR_GLOBAL_SEARCH` (Tapping search icon `🔍`)
    * ➔ `SCR_AI_DOUBT_SOLVER` (Tapping top mascot or bottom FAB)
    * ➔ `SCR_FREE_QUIZZES` (Tapping `"Free Quizzes"` in QAB)
    * ➔ `SCR_FREE_PRACTICE` (Tapping `"Free Practice"` in QAB)
    * ➔ `SCR_TESTS_TAB` (Tapping bottom tab `"Tests"`)
    * ➔ `SCR_SUPER_LANDING` (Tapping bottom tab `"Super"`)
    * ➔ `SCR_PASS_PAYWALL` (Tapping bottom tab `"Pass"` or Pass renew card)
* **Wireframe Components:**
  * Top Bar: Drawer Toggle `[≡]`, Target Selector `"My Exams 3 ⌵"`, Search `[🔍]`, AI Mascot icon
  * QAB Rail: `"Live Classes (FREE)"`, `"Free Quizzes"`, `"Free Tests"`, `"Free Notes"`, `"Free Practice"`
  * Promotional Banner Carousel: Auto-scrolling feature banners (`AppBannersPagerUI`)
  * Pass Expiry Warning Card: `"Your subscription has Expired ⚠️"`, `"Renew yearly now at ₹749"`, `"Renew"` CTA
  * Pass Trial Pitch Strip: `"2 Days trial @ just ₹ 1 /- | Renews at ₹ 799/-"`
  * Coaching Recommendations: `"Coachings handpicked for you"`, `"₹69/- Valid for 6 months"`, `"Join Now"` CTA
  * Bottom Floating Action Button: AI Doubt Solver FAB
  * Bottom Navigation Tabs: `Home`, `Tests`, `Super`, `Pass`, `Super Pass`, `News`

---

### Screen 06: Global Search Screen
* **Screen ID:** `SCR_GLOBAL_SEARCH`
* **Technical Entity:** `com.testbook.tbapp.search.SearchActivity`
* **Category:** Discovery & Search
* **Visual Reference:** `screenshots/SCR_GLOBAL_SEARCH.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (Search icon)
  * **Outgoing To:**
    * ➔ `SCR_SEARCH_RESULTS` (Submitting query)
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Top Search Input: `AutoCompleteTextView` with hint `"Search Tests, Courses, Quizzes and more"`
  * Section Header: `"Trending Exams"`
  * Trending Exam Cards (Grid): `SSC CGL`, `RRB NTPC`, `SSC CHSL`, `UPSSSC PET`, `RRB Group D`, `IBPS RRB Clerk`

---

### Screen 07: Search Results Screen
* **Screen ID:** `SCR_SEARCH_RESULTS`
* **Technical Entity:** `com.testbook.tbapp.search.SearchActivity` / `AllSearchResultFragment`
* **Category:** Discovery & Search
* **Visual Reference:** `screenshots/SCR_SEARCH_RESULTS.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_GLOBAL_SEARCH`
  * **Outgoing To:**
    * ➔ `SCR_TEST_SERIES_OVERVIEW` (Clicking an exam or test series card)
    * ➔ `SCR_SUPER_LANDING` (Clicking a course card)
    * ➔ `SCR_GLOBAL_SEARCH` (Clearing query)
* **Wireframe Components:**
  * Search Header Input with active query (e.g. `"SSC"`)
  * Scope Filter Tabs: `All`, `Exams`, `Courses`, `Test Series`, `Study Notes`
  * EXAMS Section: `SSC MTS`, `SSC JE ME`, `SSC CHSL`, `SSC Stenographer` + `"View All"`
  * COURSES Section: `SSC CGL ब्रह्मास्त्र 2026`, `SSC Foundation Live Batch` + `"View All"`
  * Bottom Action Bar: `"See All Results"`

---

### Screen 08: Enrolled Exams Bottom Sheet
* **Screen ID:** `SCR_ENROLLED_EXAMS_SHEET`
* **Technical Entity:** `com.testbook.tbapp.onboarding.versionC.bottomsheet.OnboardingTargetRvBottomSheetFragment`
* **Category:** Feed Filter Modal
* **Visual Reference:** `screenshots/56_my_exams_sheet.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (Tapping `"My Exams ⌵"`)
  * **Outgoing To:**
    * ➔ `SCR_GOAL_ONBOARDING` (Tapping `"+ Add More Exams"`)
    * ➔ `SCR_HOME_FEED` (Tapping `"Apply Filter"` or dismissing)
* **Wireframe Components:**
  * Drag Handle
  * Header: `"Your Enrolled Exams"`
  * Action Link: `"+ Add More Exams"`
  * Checkbox Items: `[x] DSSSB Junior Assistant`, `[x] UPSC Civil Services`, `[x] SSC CHSL` (with 3-dots overflow)
  * Primary Button: `"Apply Filter"`

---

### Screen 09: User Account & Settings Screen
* **Screen ID:** `SCR_USER_SETTINGS`
* **Technical Entity:** `com.testbook.tbapp.userprofile.edit.EditProfileActivity` / `SettingsFragment`
* **Category:** Account Management
* **Visual Reference:** `screenshots/SCR_USER_SETTINGS.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_NAV_DRAWER` (Tapping `"User Settings"` in header card)
  * **Outgoing To:**
    * ➔ `SCR_HOME_FEED` (Pressing back)
    * ➔ Photo Picker (Tapping user avatar)
* **Wireframe Components:**
  * Profile Picture Avatar (`SK`) with Edit overlay
  * Full Name Field: `EditText` (`"Santhosh Kumar"`)
  * Email Field: `EditText` (`"akashmegha@gmail.com"`)
  * Mobile Number Field: `EditText` (`"916333123456"`)
  * Update Profile Action Button

---

### Screen 10: Daily Current Affairs Feed
* **Screen ID:** `SCR_CURRENT_AFFAIRS`
* **Technical Entity:** `com.testbook.tbapp.ca_module.views.CAActivity`
* **Category:** Daily Content / News
* **Visual Reference:** `screenshots/SCR_CURRENT_AFFAIRS.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_NAV_DRAWER` (Tapping `"Daily Current Affairs"`)
  * **Outgoing To:**
    * ➔ `SCR_CA_BOOKMARKS` (Tapping `"Saved News"`)
    * ➔ `SCR_FREE_QUIZZES` (Tapping `"Attempt Quiz"`)
    * ➔ External Chrome Custom Tab (Tapping article headline)
* **Wireframe Components:**
  * Top Bar: Back arrow, `"Current Affairs by Testbook.com"`
  * Quick Actions: `"Saved News"`, `"Attempt Quiz"`
  * Date Navigator: `"Today"` with previous/next arrows
  * Headline Card: `"23rd September Current Affairs: Click Here to Get Detailed News 👉"`
  * News Digest Bullets: 5 curated national/international updates
  * Card Actions: `"read_more"`, `"SAVE"` (bookmark)

---

### Screen 11: Saved News / Bookmarks Screen
* **Screen ID:** `SCR_CA_BOOKMARKS`
* **Technical Entity:** `com.testbook.tbapp.ca_module.SavedNewsActivity`
* **Category:** User Vault / News
* **Visual Reference:** `screenshots/SCR_CA_BOOKMARKS.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_CURRENT_AFFAIRS` (Tapping `"Saved News"`)
  * **Outgoing To:**
    * ➔ `SCR_CURRENT_AFFAIRS` (Pressing back)
* **Wireframe Components:**
  * Header: Back arrow, `"Saved News"`
  * Bookmarked Articles List: Article title, publication date (`"16 May, 2023"`), bookmark indicator icon

---

### Screen 12: Refer & Earn Dashboard
* **Screen ID:** `SCR_REFER_AND_EARN`
* **Technical Entity:** `com.testbook.tbapp.android.referral.referAndEarn.ReferAndEarnActivity`
* **Category:** Growth & Rewards
* **Visual Reference:** `screenshots/SCR_REFER_AND_EARN.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_NAV_DRAWER` (Tapping `"Refer & Earn"`)
  * **Outgoing To:**
    * ➔ `SCR_HOME_FEED` (Pressing back)
    * ➔ External WhatsApp Intent (Tapping `"Invite via whatsapp"`)
    * ➔ OS Share Sheet (Tapping `"Share Now"`)
* **Wireframe Components:**
  * Header: Back arrow, `"Refer & Earn"`, `"Earnings"`, `"T&C"`
  * Hero Graphic: `"Learn & Earn with Testbook - WIN upto 10% Cashback directly into your bank account"`
  * Incentive Banner: `"Earn incentive upto ₹3000 Extra"`
  * Unique Referral Code Box: `O834MK`
  * Action Buttons: `"Invite via whatsapp"` (Green CTA), `"Share Now"` (Blue CTA)

---

### Screen 13: Transactions & Order History Screen
* **Screen ID:** `SCR_TRANSACTIONS`
* **Technical Entity:** `com.testbook.tbapp.transactionsScreen.TransactionsListActivity` / `NewTransactionFragment`
* **Category:** Billing & Orders
* **Visual Reference:** `screenshots/SCR_TRANSACTIONS.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_NAV_DRAWER` (Tapping `"Transactions"`)
  * **Outgoing To:**
    * ➔ `SCR_TRANSACTION_RECEIPT` (Clicking any transaction item)
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Toolbar Title: `"Transactions"`
  * Transaction List Item (Cards):
    * Product Name: `"Yearly Testbook Pass"`, `"UPSC PrepLab Super Subscription"`
    * Amount: `₹749.0`, `₹1.0`
    * Transaction Date: `"23 Sep 2026"`, `"27 Apr 2026"`
    * Status Badges: `FAILURE` (Red), `SUCCESS` (Green), `PENDING` (Orange)

---

### Screen 14: Free Daily Quizzes Screen
* **Screen ID:** `SCR_FREE_QUIZZES`
* **Technical Entity:** `com.testbook.tbapp.tb_super.landingScreenV2.freeResources.activities.quizzes.TbFreeResourcesQuizzesActivity`
* **Category:** Practice & Assessment
* **Visual Reference:** `screenshots/SCR_FREE_QUIZZES.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (QAB `"Free Quizzes"`) OR `SCR_CURRENT_AFFAIRS` (`"Attempt Quiz"`)
  * **Outgoing To:**
    * ➔ `SCR_TEST_INTERFACE` (Attempting a quiz)
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Top Bar: Back arrow, `"Free Daily Quizzes"`
  * Exam Target Chips: `[SSC CGL]` (Active), `[RRB NTPC]`
  * Banner: `"All Your Attempted Quizzes"`
  * Quiz List / Empty State container

---

### Screen 15: Free Practice Screen
* **Screen ID:** `SCR_FREE_PRACTICE`
* **Technical Entity:** `com.testbook.tbapp.tb_super.landingScreenV2.freeResources.activities.practice.TbFreeResourcePracticeActivity`
* **Category:** Practice & Assessment
* **Visual Reference:** `screenshots/SCR_FREE_PRACTICE.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (QAB `"Free Practice"`)
  * **Outgoing To:**
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Top Bar: Back arrow, `"Free Practice"`
  * Exam Target Chips: `[SSC CGL]`, `[RRB NTPC]`
  * Practice Subject Cards list

---

### Screen 16: Study Notes Overview Screen
* **Screen ID:** `SCR_STUDY_NOTES`
* **Technical Entity:** `com.testbook.tbapp.tb_super.postPurchase.globalStudyNote.GlobalStudyNotesActivity`
* **Category:** Study Material
* **Visual Reference:** `screenshots/SCR_STUDY_NOTES.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TESTS_TAB` (Quick pill `"Study Notes"`) OR `SCR_HOME_FEED` (QAB `"Free Notes"`)
  * **Outgoing To:**
    * ➔ `SCR_CHAPTER_NOTES` (Clicking any subject/chapter card)
    * ➔ `SCR_PASS_PAYWALL` (Tapping `"Renew @₹749"` banner)
* **Wireframe Components:**
  * Top Bar: Back arrow, `"Study Notes"`
  * Goal Chips: `[SSC CGL PassOne]` (Active), `[SSC Exams PassOne]`
  * Pass Expired Alert: `"Your subscription has Expired ⚠️"`, `"Renew @₹749 before this price updates in 09:00:55"`
  * Subject Tabs: `[Mathematics]`, `[English]`, `[Logical Reasoning]`
  * Chapter Cards: `"Number System (9 PDFs) >"`, `"Percentage (12 PDFs) >"`

---

### Screen 17: Chapter PDF Notes List Screen
* **Screen ID:** `SCR_CHAPTER_NOTES`
* **Technical Entity:** `com.testbook.tbapp.study_module.ui.chapterScreen.ChapterActivity`
* **Category:** Study Material
* **Visual Reference:** `screenshots/SCR_CHAPTER_NOTES.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_STUDY_NOTES`
  * **Outgoing To:**
    * ➔ `SCR_NOTES_LOCKED_PAYWALL` (Clicking any locked note card)
    * ➔ Fullscreen PDF Viewer (If user has active pass)
* **Wireframe Components:**
  * Top Bar: Back arrow, Chapter Title (`"Ratio & Proportion - 6 PDFs"`)
  * PDF Topic Cards:
    * `"Types of Ratios - Notes"` (with Lock icon 🔒)
    * `"Basic Concept - Notes"` (with Lock icon 🔒)
    * `"Third Proportional - Notes"` (with Lock icon 🔒)
  * Floating Action Button: `"Sections"` selector

---

### Screen 18: Tests Explorer Tab Screen
* **Screen ID:** `SCR_TESTS_TAB`
* **Technical Entity:** `com.testbook.tbapp.android.DashboardActivity` (Bottom Tab 2) + `TestSeriesExploreFragment`
* **Category:** Test Series Explorer
* **Visual Reference:** `screenshots/SCR_TESTS_EXPLORE_SCROLLED.png`, `screenshots/SCR_TESTS_CATEGORIES.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (Bottom Tab `"Tests"`)
  * **Outgoing To:**
    * ➔ `SCR_TEST_SERIES_OVERVIEW` (Clicking enrolled or trending test series card)
    * ➔ `SCR_STUDY_NOTES` (Clicking `"Study Notes"` pill)
    * ➔ `SCR_FREE_QUIZZES` (Clicking `"Live Quizzes"` pill)
    * ➔ `SCR_PASS_PAYWALL` (Clicking Pass expired alert)
* **Wireframe Components:**
  * Enrolled Test Series Rail: `SSC Selection Post (1/609)`, `SSC MTS (1/2002)` + `"View All"`
  * Quick Filter Pills: `Study Notes (NEW)`, `Live Test`, `Live Quizzes (FREE)`, `Rankers Tests`, `Prev. Papers`
  * Toppers Streak Card: Badge `"Kickstarter"`, `"Attempt 2 more to unlock Rising Star"`, 7-day streak circles, `"Attempt Test Now"` CTA
  * Pass Expiry Alert: `"Restore your attempted tests by renewing Now"`

---

### Screen 19: Test Series Overview & Sections Detail
* **Screen ID:** `SCR_TEST_SERIES_OVERVIEW`
* **Technical Entity:** `com.testbook.tbapp.android.ui.activities.testSeriesSections.TestSeriesSectionsActivity`
* **Category:** Test Series
* **Visual Reference:** `screenshots/13_tests_landing.png`, `screenshots/14_test_list.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TESTS_TAB` OR `SCR_HOME_FEED` (Clicking test card)
  * **Outgoing To:**
    * ➔ `SCR_TEST_LEVEL_SHEET` (Tapping `"Level: All ⌵"`)
    * ➔ `SCR_PRE_INSTRUCTIONS` (Tapping `"Start Test"` on any test card)
    * ➔ `SCR_PASS_PAYWALL` (Tapping locked test)
* **Wireframe Components:**
  * Top Bar: Back arrow, Share icon
  * Series Title: `"SSC Selection Post (Phase 14) 2026 Mock Test Series"`
  * Stats: `"609 Total Tests"`, `"9 Free Tests"`
  * Level Filter: `"Level: All ⌵"`
  * Language Info: `"Available in English, Hindi"`
  * Test Type Tabs: `Mock Tests`, `PYPs`, `Study Notes`
  * Section Accordion Groups: `"Exam Day Special (6 Free Tests)"`, `"Most Saved Qs Subject Test"`
  * Test Item Card: `"FREE"` badge, `"SSC Selection Post: Practice Test Day - 01"`, `"100 Qs . 60 mins . 200.0 Marks"`, `"Start Test"` CTA

---

### Screen 20: Exam Level Selection Bottom Sheet
* **Screen ID:** `SCR_TEST_LEVEL_SHEET`
* **Technical Entity:** `com.testbook.tbapp.base_test_series.testSeriesBranchSelection.TestSeriesBranchSelectionBottomSheetFragment`
* **Category:** Filter Modal
* **Visual Reference:** `screenshots/12_tests_tab.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TEST_SERIES_OVERVIEW`
  * **Outgoing To:**
    * ➔ `SCR_TEST_SERIES_OVERVIEW` (Selecting level and tapping `"Proceed"`)
* **Wireframe Components:**
  * Sheet Title: `"Choose your Level :"`
  * Selectable Level Cards:
    * Card 1: `All`
    * Card 2: `Matriculation`
    * Card 3: `10+2 (Higher Secondary)`
    * Card 4: `Graduation and Above`
  * Action Button: `"Proceed"`

---

### Screen 21: Test Pre-Instructions & Rules Screen
* **Screen ID:** `SCR_PRE_INSTRUCTIONS`
* **Technical Entity:** `com.testbook.tbapp.test.testInstructions.preInstructions.PreInstructionsFragment`
* **Category:** Assessment Gate
* **Visual Reference:** `screenshots/15_test_instructions.png`, `screenshots/16_choose_lang_sheet.png`, `screenshots/17_lang_selected.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TEST_SERIES_OVERVIEW` (Tapping `"Start Test"`)
  * **Outgoing To:**
    * ➔ `SCR_TEST_INTERFACE` (Selecting language & tapping `"Agree and Continue"`)
    * ➔ `SCR_PASS_PAYWALL` (Tapping `"Get Pass"` on upsell banner)
* **Wireframe Components:**
  * Pass Upsell Strip: `"Get Unlimited Mock Tests, PYPs & more"`, `"Get Pass"` CTA
  * Test Title: `"SSC Selection Post (Phase 14): Practice Test Day - 01"`
  * Meta: `"Duration: 60 Mins."`, `"Maximum Marks: 200.0"`
  * Instructions Bullet Points: 100 questions, 4 options, 60 mins, sectional timers, marking scheme (+2.0, -0.5)
  * Default Language Selector: Dropdown modal with English, Hindi, Telugu, Marathi, Bengali, Tamil
  * Launch Button: `"Agree and Continue"`

---

### Screen 22: Live Test Taking Engine
* **Screen ID:** `SCR_TEST_INTERFACE`
* **Technical Entity:** `com.testbook.tbapp.revampedTest.TestAttemptActivity`
* **Category:** Core Assessment
* **Visual Reference:** `screenshots/18_test_interface.png`, `screenshots/22_section_b.png`, `screenshots/23_question_answered.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_PRE_INSTRUCTIONS`
  * **Outgoing To:**
    * ➔ `SCR_QUESTION_PALLET` (Tapping pallet toggle `[≡]`)
    * ➔ `SCR_SECTION_SUBMIT_MODAL` (Submitting a section)
    * ➔ `SCR_TEST_ANALYSIS` (Final test submission)
* **Wireframe Components:**
  * Top Bar: Pause `(||)`, Section Timer (`00:14:12`), Test Title, Language Toggle `[E / अ]`, Pallet Toggle `[≡]`
  * Section Navigation Tabs: `General Intelligence`, `General Awareness`, `Quantitative Aptitude`, `English Language`
  * Info Bar: `"Total Questions Answered: 0"`, Alert Pill `"Last 15 Mins"`
  * Question Card: Number Badge (`1`), Question Timer (`00:47`), Bookmark Icon, Star/Report Icon
  * Question Text (HTML / Equations)
  * Radio Options: 4 interactive selectable cards
  * Bottom Action Bar: `"Previous"`, `"Mark For Review"`, `"Save & Next"`

---

### Screen 23: Question Pallet Drawer
* **Screen ID:** `SCR_QUESTION_PALLET`
* **Technical Entity:** `com.testbook.tbapp.test.asm.asmDrawerNavigation.fragment.ASMTestQuestionNavigationFragment`
* **Category:** Assessment Drawer
* **Visual Reference:** `screenshots/19_question_pallet.png`, `screenshots/26_final_section_pallet.png`, `screenshots/28_section_d_pallet.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TEST_INTERFACE`
  * **Outgoing To:**
    * ➔ `SCR_TEST_INTERFACE` (Tapping any question number in grid)
    * ➔ `SCR_SECTION_SUBMIT_MODAL` (Tapping `"SUBMIT SECTION"`)
    * ➔ `SCR_TEST_SUBMIT_MODAL` (Tapping `"SUBMIT TEST"`)
* **Wireframe Components:**
  * Utility Header: `? Symbols` (legend modal), `i Instructions` (rules modal)
  * Section Chips: `[PART - A]`, `[PART - B]`, `[PART - C]`, `[PART - D]`
  * Status Summary Card: Answered count, Unanswered count
  * 5x5 Matrix Question Grid: Numbered buttons (1 to 25) with current question arrow indicator
  * Action Buttons: `"SUBMIT SECTION"`, `"SUBMIT TEST"`

---

### Screen 24: Submission Confirmation Dialogs
* **Screen ID:** `SCR_SUBMIT_CONFIRM`
* **Technical Entity:** `com.testbook.tbapp.test.asm.sectionSummary.fragment.ASMTestSectionsSummaryDialogFragment` / `ASMTestSubmitDialogFragment`
* **Category:** Assessment Modal
* **Visual Reference:** `screenshots/21_submit_section_dialog.png`, `screenshots/29_test_submit_confirmation.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_QUESTION_PALLET`
  * **Outgoing To:**
    * ➔ `SCR_TEST_INTERFACE` (Next section or if tapping `"No"`)
    * ➔ `SCR_TEST_ANALYSIS` (Test submitted)
* **Wireframe Components:**
  * Dialog Container
  * Breakdown Table: Time Left, Attempted, Unattempted, Marked counts
  * Confirmation Prompt: `"Are you sure you want to submit the section / test?"`
  * Action Buttons: `[Yes]` (Primary Blue) | `[No]` (Secondary Grey)

---

### Screen 25: SuperCoaching Pre-Purchase Landing
* **Screen ID:** `SCR_SUPER_LANDING`
* **Technical Entity:** `com.testbook.tbapp.tb_super.landingScreen.TbSuperLandingActivity` / `TbSuperLandingFragment`
* **Category:** SuperCoaching Sales
* **Visual Reference:** `screenshots/38_super_coaching_tab.png`, `screenshots/39_super_coaching_scrolled.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (Bottom Tab `"Super"`)
  * **Outgoing To:**
    * ➔ `SCR_SUPER_PLANS` (Tapping `"Claim Offer Now"` CTA)
    * ➔ `SCR_SUPER_CURRICULUM` (Tapping course syllabus)
* **Wireframe Components:**
  * Top Bar: Drawer Toggle `[≡]`, SuperCoaching Logo
  * Goal Hero Banner: `"UPSC EPFO APFC 2026 - One Batch. Complete Preparation"`
  * Expiration Banner: `"Offer Expires in 00:29:58 | Grab Now!"`
  * Personalization Greeting: `"Hi Santhosh Kumar! 👋 Great offer for you, Grab now!"`
  * Urgency Badge: `"OFFER CLOSING SOON"`
  * Sticky Action CTA: `"Claim Offer Now"`

---

### Screen 26: SuperCoaching Plan Selection & Pricing
* **Screen ID:** `SCR_SUPER_PLANS`
* **Technical Entity:** `com.testbook.tbapp.tb_super.ui.goalsubscription.GoalSubscriptionActivity`
* **Category:** Monetization & Plans
* **Visual Reference:** `screenshots/40_super_plan_selection.png`, `screenshots/41_super_plan_selection_full.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_SUPER_LANDING`
  * **Outgoing To:**
    * ➔ `SCR_PAYMENT_GATEWAY` (Tapping `"Proceed to Payment"`)
    * ➔ `SCR_SUPER_LANDING` (Pressing back)
* **Wireframe Components:**
  * Celebratory Coupon Modal: `"COUPON APPLIED - You got 16% Off with this coupon"`
  * Value Props Grid: 10+ Courses, 75+ Study Notes, 100+ Mock Tests, 70+ Practice Tests
  * Applied Coupon Box: `"Offer Closing Soon - EPFO Complete Course - Now at ₹3,000 [Apply / Remove]"`
  * EMI Switch: `"No Cost EMI available - View EMI Plans"` toggle
  * Plan Cards: `"Recommended"`, `"Total savings: ₹1,500"`, `"Pay in 2 EMIs of ₹1500"`
  * Sticky Bottom Checkout Bar: Struck-through `₹4,500`, Final `₹3,000`, `"Proceed to Payment"` CTA

---

### Screen 27: Testbook Pass Landing & Paywall
* **Screen ID:** `SCR_PASS_PAYWALL`
* **Technical Entity:** `com.testbook.tbapp.base_pass.passOne.PassOnePurchaseActivity`
* **Category:** Pass Paywall
* **Visual Reference:** `screenshots/48_pass_landing.png`, `screenshots/49_pass_plans.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (Bottom Tab `"Pass"` or Pass Renew Card) OR any locked content
  * **Outgoing To:**
    * ➔ `SCR_DYNAMIC_QR` / `SCR_PAYMENT_GATEWAY` (Tapping `"Buy Yearly Testbook Pass"`)
    * ➔ `SCR_PASS_COMPARE` (Tapping `"View Comparison"`)
* **Wireframe Components:**
  * Hero Visual: Phone Mockup, `"Mission Officer - One Pass to ACE all Exams"`
  * Expiry Alert Card: `"⚠️ Your Pass Subscription has expired!"`
  * Renewal Price Card: `"Your Renewal Price ₹749 (struck through ₹949)"`
  * Urgency Banner: `"Hurry ! Price increasing to ₹849 in 09:51:39"`
  * Benefit Cards (2x3): 150k+ Mock Tests, 30k+ PYPs, Rankers Series, 10k+ Notes, Doubt Support, Practice Qs
  * Sticky Purchase Bar: `"Pay using QR Code [Change >]"`, `₹749`, `"Buy Yearly Testbook Pass"` CTA

---

### Screen 28: Pass Plans & Included Test Series
* **Screen ID:** `SCR_PASS_PLANS`
* **Technical Entity:** `com.testbook.tbapp.base_pass.passOne.PassOnePurchaseFragment` (Scrolled View)
* **Category:** Pass Paywall
* **Visual Reference:** `screenshots/50_pass_plan_durations.png`, `screenshots/51_pass_vs_passpro.png`, `screenshots/52_pass_coupons_faq.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_PASS_PAYWALL`
  * **Outgoing To:**
    * ➔ `SCR_TEST_SERIES_OVERVIEW` (Clicking preview card)
    * ➔ `SCR_DYNAMIC_QR` (Tapping buy CTA)
* **Wireframe Components:**
  * Plan Card: `"Yearly Testbook Pass - ₹749"`
  * Social Proof Banner: `"Trusted by 3.6 Crore+ Students"` | `"4,23,891+ Students Selected"`
  * Included Tests Preview Tabs: `[Test Series]`, `[PYP Test]`, `[Study Notes]`
  * Preview Cards: SSC CHSL Series, Current Affairs Mega Pack, SSC Maths PYP Series
  * Action Button: `"View All Test Series"`

---

### Screen 29: Dynamic UPI QR Code Modal
* **Screen ID:** `SCR_DYNAMIC_QR`
* **Technical Entity:** `com.testbook.tbapp.allPayments.fragment.AllPaymentFragment` (QR Sub-view)
* **Category:** Payment
* **Visual Reference:** `screenshots/53_pass_checkout.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_PASS_PAYWALL` or `SCR_PAYMENT_GATEWAY`
  * **Outgoing To:**
    * ➔ `SCR_PASS_FAILURE_PAGE` (Canceling or timing out)
    * ➔ `SCR_PAYMENT_SUCCESS` (Successful UPI transaction)
* **Wireframe Components:**
  * App Crest
  * Title: `"Scan the QR Code"`
  * Dynamic BharatQR / UPI QR Image container
  * Expiry Timer: `"This QR code is valid for another 9:49 Minutes"`

---

### Screen 30: Pass Payment Failure Recovery Page
* **Screen ID:** `SCR_PASS_FAILURE_PAGE`
* **Technical Entity:** `com.testbook.tbapp.base_pass.passOne.PassPaymentFailureActivity`
* **Category:** Payment Recovery
* **Visual Reference:** `screenshots/54_pass_payment_failure.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_DYNAMIC_QR` (Dismissed/cancelled QR payment)
  * **Outgoing To:**
    * ➔ `SCR_DYNAMIC_QR` (Tapping `"Buy Yearly Testbook Pass"` to retry)
    * ➔ `SCR_PASS_PAYWALL` (Tapping `"View Plans"`)
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Top Bar: Back arrow
  * Graphic: Warning Credit Card icon
  * Title: `"Your Payment Failed"`
  * Subtitle: `"We tried to process your payment but something went wrong."`
  * Benefit Reminder Card: 150,000+ Mock Tests, 30,000+ PYPs
  * Retry Sticky Bar: `"Pay using QR Code [Change >]"`, `₹749`, `"Buy Yearly Testbook Pass"` CTA
  * Bottom Action Link: `"View Plans"`

---

### Screen 31: Consolidated Checkout & Payment Gateway
* **Screen ID:** `SCR_PAYMENT_GATEWAY`
* **Technical Entity:** `com.testbook.tbapp.allPayments.activity.AllPaymentsActivity` / `AllPaymentFragment`
* **Category:** Payment Gateway
* **Visual Reference:** `screenshots/42_make_payment_screen.png`, `screenshots/43_qr_payment.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_SUPER_PLANS` OR `SCR_PASS_PAYWALL`
  * **Outgoing To:**
    * ➔ `SCR_DYNAMIC_QR` (Tapping `"Scan QR Code"`)
    * ➔ External UPI App Intent (GPay, PhonePe, Paytm)
    * ➔ `SCR_PAYMENT_FAILURE_SHEET` (Payment failure or error)
    * ➔ `SCR_PAYMENT_SUCCESS` (Successful transaction)
* **Wireframe Components:**
  * Header: Back arrow, `"Make Payment"`
  * Order Summary Card: SuperCoaching / Pass logo, Product title, Original vs Payable price, Applied coupon badge, `"To Pay ⌵ ₹ 3000"` accordion
  * Payment Methods:
    * Section 1: UPI (`"Scan QR Code - Pay using any UPI app >"`)
    * Section 2: Cards (`"Pay with Debit / Credit Card >"`)
    * Section 3: Netbanking (Bank icons & other banks)
  * Payment Failure Sheet (Overlay): Exclamation graphic, `"Transaction Failed!"`, `"Try Again"`, `"Try different payment method"`

---

### Screen 32: Test Performance Analysis Scorecard
* **Screen ID:** `SCR_TEST_ANALYSIS`
* **Technical Entity:** `com.testbook.tbapp.test.analysis2.TestAnalysis2Activity`
* **Category:** Assessment Performance
* **Visual Reference:** `screenshots/31_test_analysis.png`, `screenshots/32_test_analysis_metrics.png`, `screenshots/33_test_analysis_score.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_SUBMIT_CONFIRM` (Post-test submit) OR `SCR_TESTS_TAB` (Attempted tests)
  * **Outgoing To:**
    * ➔ `SCR_TEST_SOLUTIONS` (Tapping `"Solutions"` tab)
    * ➔ `SCR_TEST_LEADERBOARD` (Tapping `"Leaderboard"` tab)
    * ➔ `SCR_PASS_PAYWALL` (Tapping `"Restore Now at ₹749"`)
    * ➔ `SCR_REATTEMPT_INTERFACE` (Tapping `"Unlock Reattempt Mode"`)
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Header Bar: Back arrow, Test Name, Language Switcher, Drawer Action Toggle
  * Top Promotional Banner: `"Testbook Creators Lab - Earn ₹50"`
  * Tabs: `Analysis` (Active), `Solutions`, `Leaderboard`
  * Paywall Card: `"Your subscription has Expired ⚠️"`, `"Your Renewal Price ₹749 (struck through ₹949)"`, Timer `"09:59:11"`, `"Restore Now"` CTA
  * Reattempt Upsell Card: `"Want to become a Top Ranker? Reattempt. Improve. Achieve"`, `"Unlock Reattempt Mode"`
  * Performance Scorecard:
    * `Rank: 19993 / 22112`
    * `Score: 2 / 200` (Average: 69.07, Best: 200)
    * `Percentile: 9.59 %`
    * `Accuracy: 100 %`
    * `Qs. Attempted: 1 / 100` (`Correct: 1`, `Incorrect: 0`, `Unattempted: 99`)

---

### Screen 33: Test Question Solutions Screen
* **Screen ID:** `SCR_TEST_SOLUTIONS`
* **Technical Entity:** `com.testbook.tbapp.test.solutions.TestSolutionsFragment`
* **Category:** Assessment Review
* **Visual Reference:** `screenshots/34_test_solutions.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TEST_ANALYSIS` (Tapping `"Solutions"` tab)
  * **Outgoing To:**
    * ➔ `SCR_TEST_ANALYSIS` (Tapping `"Analysis"` tab)
    * ➔ Question detailed solution view (Tapping question card)
* **Wireframe Components:**
  * Solution Filter Chips: `[All (100)]` (Selected), `[Overtime (3)]`, `[Unattempted (99)]`, `[Correct]`, `[Incorrect]`
  * Section Header: `"GENERAL INTELLIGENCE / 25 Questions"`
  * Solution Cards List: Question index, duration spent (`1:52`), community accuracy (`65% got it right`), Bookmark icon, Question snippet
  * Floating Bottom Button: `"Sections"` selector

---

### Screen 34: Test Leaderboard Podium Screen
* **Screen ID:** `SCR_TEST_LEADERBOARD`
* **Technical Entity:** `com.testbook.tbapp.test.leaderboard.TestLeaderBoardFragment`
* **Category:** Assessment Social
* **Visual Reference:** `screenshots/35_test_leaderboard.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_TEST_ANALYSIS` (Tapping `"Leaderboard"` tab)
  * **Outgoing To:**
    * ➔ `SCR_TEST_ANALYSIS` (Tapping `"Analysis"` tab)
* **Wireframe Components:**
  * Reattempt Upsell Banner
  * Top 3 Podium Cards:
    * Rank 1: "Raja" (`200.0 / 200.0`)
    * Rank 2: "Hemant" (`195.0 / 200.0`)
    * Rank 3: "Vivek" (`193.5 / 200.0`)
  * Sticky User Rank Bottom Bar: Rank `19993`, `"Santhosh Kumar (You)"`, Score `2.0 / 200.0 Marks`

---

### Screen 35: App Language Switcher Screen
* **Screen ID:** `SCR_APP_LANGUAGE`
* **Technical Entity:** `com.testbook.tbapp.android.changeLanguage.ChangeLanguageActivity`
* **Category:** Settings / Localization
* **Visual Reference:** `screenshots/SCR_APP_LANGUAGE.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_NAV_DRAWER` (Tapping `"Language"`)
  * **Outgoing To:**
    * ➔ `SCR_HOME_FEED` (Selecting language and applying)
* **Wireframe Components:**
  * Header: Back arrow, Title `"Change Language"`
  * Radio List: English, Hindi, Marathi, Bengali, Telugu, Tamil, Gujarati
  * Apply / Save CTA button

---

### Screen 36: AI Doubt Solver (Samadhan AI) Screen
* **Screen ID:** `SCR_AI_DOUBT_SOLVER`
* **Technical Entity:** `com.testbook.tbapp.base.webView.WebViewActivity` (`tpl.testbook.com/tb-ai`)
* **Category:** AI Learning Assistant
* **Visual Reference:** `screenshots/SCR_NOTIFICATIONS.png`
* **Wireflow Connections:**
  * **Incoming From:** `SCR_HOME_FEED` (Top mascot icon or Bottom FAB)
  * **Outgoing To:**
    * ➔ `SCR_HOME_FEED` (Pressing back)
* **Wireframe Components:**
  * Header Bar: Back arrow, Title `"Testbook"`
  * Target Exam Pill: `"My Exams ⌵"`
  * Mascot Hero: Book cartoon character + CTA `"+ Start Chat"`
  * Section: `"Your Preparation"`
  * Chat Composer Bar: Text field with placeholder `"Ask anything..."`, Attachment `(+)`, Send button `(↑)`

---

## 3. Summary of Visual Assets Produced

| Screen ID | Visual Asset File | Flow Phase |
|---|---|---|
| `SCR_SPLASH` | `screenshots/01_launch.png` | Launch |
| `SCR_AUTH_LOGIN` | `screenshots/02_login_screen.png`, `03_phone_entered.png` | Auth |
| `SCR_AUTH_OTP` | `screenshots/04_after_otp.png` | Auth |
| `SCR_GOAL_ONBOARDING` | `screenshots/57_onboarding_goal_selection.png`, `58_onboarding_categories_scrolled.png` | Onboarding |
| `SCR_HOME_FEED` | `screenshots/06_home_feed.png`, `07_home_feed_scrolled.png`, `08_home_feed_scrolled_more.png`, `55_home_tab.png` | Core Home |
| `SCR_GLOBAL_SEARCH` | `screenshots/SCR_GLOBAL_SEARCH.png` | Discovery |
| `SCR_SEARCH_RESULTS` | `screenshots/SCR_SEARCH_RESULTS.png` | Discovery |
| `SCR_ENROLLED_EXAMS_SHEET` | `screenshots/56_my_exams_sheet.png` | Home Modal |
| `SCR_USER_SETTINGS` | `screenshots/SCR_USER_SETTINGS.png` | Account |
| `SCR_CURRENT_AFFAIRS` | `screenshots/SCR_CURRENT_AFFAIRS.png` | News & CA |
| `SCR_CA_BOOKMARKS` | `screenshots/SCR_CA_BOOKMARKS.png` | News & CA |
| `SCR_REFER_AND_EARN` | `screenshots/SCR_REFER_AND_EARN.png` | Growth |
| `SCR_TRANSACTIONS` | `screenshots/SCR_TRANSACTIONS.png` | Billing |
| `SCR_TRANSACTION_RECEIPT` | `screenshots/SCR_TRANSACTION_RECEIPT.png` | Billing |
| `SCR_FREE_QUIZZES` | `screenshots/SCR_FREE_QUIZZES.png` | Practice |
| `SCR_FREE_PRACTICE` | `screenshots/SCR_FREE_PRACTICE.png` | Practice |
| `SCR_STUDY_NOTES` | `screenshots/SCR_STUDY_NOTES.png` | Study Material |
| `SCR_CHAPTER_NOTES` | `screenshots/SCR_CHAPTER_NOTES.png` | Study Material |
| `SCR_NOTES_LOCKED_PAYWALL`| `screenshots/SCR_NOTES_LOCKED_PAYWALL.png` | Paywall Modal |
| `SCR_TESTS_TAB` | `screenshots/SCR_TESTS_EXPLORE_SCROLLED.png`, `SCR_TESTS_CATEGORIES.png` | Test Series |
| `SCR_TEST_SERIES_OVERVIEW` | `screenshots/13_tests_landing.png`, `14_test_list.png` | Test Series |
| `SCR_TEST_LEVEL_SHEET` | `screenshots/12_tests_tab.png` | Filter Modal |
| `SCR_PRE_INSTRUCTIONS` | `screenshots/15_test_instructions.png`, `16_choose_lang_sheet.png`, `17_lang_selected.png` | Assessment |
| `SCR_TEST_INTERFACE` | `screenshots/18_test_interface.png`, `22_section_b.png`, `23_question_answered.png` | Assessment |
| `SCR_QUESTION_PALLET` | `screenshots/19_question_pallet.png`, `26_final_section_pallet.png`, `28_section_d_pallet.png` | Assessment Drawer |
| `SCR_SUBMIT_CONFIRM` | `screenshots/21_submit_section_dialog.png`, `29_test_submit_confirmation.png` | Assessment Modal |
| `SCR_SUPER_LANDING` | `screenshots/38_super_coaching_tab.png`, `39_super_coaching_scrolled.png` | SuperCoaching |
| `SCR_SUPER_PLANS` | `screenshots/40_super_plan_selection.png`, `41_super_plan_selection_full.png` | SuperCoaching |
| `SCR_PASS_PAYWALL` | `screenshots/48_pass_landing.png`, `49_pass_plans.png` | Pass Paywall |
| `SCR_PASS_PLANS` | `screenshots/50_pass_plan_durations.png`, `51_pass_vs_passpro.png`, `52_pass_coupons_faq.png` | Pass Paywall |
| `SCR_DYNAMIC_QR` | `screenshots/53_pass_checkout.png` | Payment Modal |
| `SCR_PASS_FAILURE_PAGE` | `screenshots/54_pass_payment_failure.png` | Payment Recovery |
| `SCR_PAYMENT_GATEWAY` | `screenshots/42_make_payment_screen.png`, `43_qr_payment.png` | Checkout Gateway |
| `SCR_TEST_ANALYSIS` | `screenshots/31_test_analysis.png`, `32_test_analysis_metrics.png`, `33_test_analysis_score.png` | Performance |
| `SCR_TEST_SOLUTIONS` | `screenshots/34_test_solutions.png` | Performance |
| `SCR_TEST_LEADERBOARD` | `screenshots/35_test_leaderboard.png` | Performance |
| `SCR_APP_LANGUAGE` | `screenshots/SCR_APP_LANGUAGE.png` | Settings |
| `SCR_AI_DOUBT_SOLVER` | `screenshots/SCR_NOTIFICATIONS.png` | AI Assistant |
