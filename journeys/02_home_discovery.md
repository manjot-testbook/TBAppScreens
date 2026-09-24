# Product Journey 02: Home Feed, Discovery & Global Search

**Owner:** Product & Discovery Pod  
**Target Platform:** Testbook Android App  

---

## 1. Journey Overview & Wireflow

This journey maps the central hub of the app: browsing the dynamic Home Feed, interacting with promotional strips, switching target exams, opening global search, and executing search queries across exams and courses.

```
[Home Feed] ──┬──▶ Enrolled Exams Bottom Sheet ──▶ Target Exam Selection
               ├──▶ Global Search ──────────────▶ Search Results (Exams, Courses, Tests)
               ├──▶ Samadhan AI Doubt Solver (FAB / Mascot)
               └──▶ Navigation Drawer ──────────▶ (Utilities & Settings)
```

---

## 2. Screen Specifications & Event Contracts

### Screen 05: Home Feed Dashboard (`SCR_HOME_FEED`)
* **Visual Reference:** `../screenshots/06_home_feed.png`, `../screenshots/07_home_feed_scrolled.png`, `../screenshots/08_home_feed_scrolled_more.png`
* **Came From:** Onboarding OR any Bottom Tab
* **Leads To:** Global Search, Enrolled Exams Sheet, Doubt Solver, Bottom Tabs (Tests, Super, Pass, News)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "home_feed", "active_tab": "home", "is_paid_user": false, "enrolled_goals_count": 2}`
  * **`screen_duration`**
    * *Trigger:* On screen pause, navigation away, or app backgrounding.
    * *Properties:* `{"screen_name": "home_feed", "duration_ms": 38400}`
  * **`component_view` (Pass Elite ₹1 Trial Strip)**
    * *Trigger:* Promotional ₹1 trial card enters viewport.
    * *Properties:* `{"screen_name": "home_feed", "component_name": "pass_trial_strip", "component_type": "banner", "trial_price": 1, "renewal_price": 799}`
  * **`component_click` (Join Coaching Card)**
    * *Properties:* `{"screen_name": "home_feed", "component_name": "coaching_card_join", "component_type": "card", "product_name": "Courses by Testbook", "price": 69, "destination": "super_plan_selection"}`
  * **`component_click` (AI Doubt Solver FAB)**
    * *Properties:* `{"screen_name": "home_feed", "component_name": "ai_doubt_solver_fab", "component_type": "fab", "destination": "ai_doubt_solver"}`
  * **`component_click` (Bottom Navigation Tab)**
    * *Properties:* `{"screen_name": "home_feed", "component_name": "bottom_nav_tab", "component_type": "tab", "tab_name": "tests | super | pass | news"}`

---

### Screen 06: Enrolled Exams Bottom Sheet (`SCR_ENROLLED_EXAMS_SHEET`)
* **Visual Reference:** `../screenshots/56_my_exams_sheet.png`
* **Came From:** Home Feed (tapping "My Exams ⌵")
* **Leads To:** Target Exam Onboarding (via "+ Add More Exams") or filters Home Feed
* **Events to Track:**
  * **`component_view`**
    * *Properties:* `{"screen_name": "home_feed", "component_name": "enrolled_exams_sheet", "component_type": "bottom_sheet", "enrolled_count": 3}`
  * **`component_click` (Add More Exams Link)**
    * *Properties:* `{"screen_name": "home_feed", "component_name": "add_more_exams", "component_type": "link", "destination": "onboarding_goal_selection"}`

---

### Screen 07: Global Search Query Screen (`SCR_GLOBAL_SEARCH`)
* **Visual Reference:** `../screenshots/SCR_GLOBAL_SEARCH.png`
* **Came From:** Home Feed header (Search icon)
* **Leads To:** Search Results Screen (`SCR_SEARCH_RESULTS`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "global_search", "entry_source": "home_header"}`
  * **`component_click` (Trending Exam Chip)**
    * *Properties:* `{"screen_name": "global_search", "component_name": "trending_search_chip", "component_type": "chip", "query": "SSC CGL", "destination": "search_results"}`

---

### Screen 08: Search Results Screen (`SCR_SEARCH_RESULTS`)
* **Visual Reference:** `../screenshots/SCR_SEARCH_RESULTS.png`
* **Came From:** Global Search Screen
* **Leads To:** Test Series Overview (`SCR_TEST_SERIES_OVERVIEW`) or SuperCoaching Landing (`SCR_SUPER_LANDING`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "search_results", "query": "SSC", "scope": "all | exams | courses | test_series"}`
  * **`component_click` (Search Result Item)**
    * *Properties:* `{"screen_name": "search_results", "component_name": "search_result_card", "component_type": "card", "item_type": "exam | course", "item_title": "SSC MTS", "destination": "test_series_overview"}`
