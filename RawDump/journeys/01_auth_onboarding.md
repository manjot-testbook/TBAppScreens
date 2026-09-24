# Product Journey 01: User Acquisition, Authentication & Goal Selection

**Owner:** Product & Growth Pod  
**Target Platform:** Testbook Android App  

---

## 1. Journey Overview & Wireflow

This journey maps the new and returning user lifecycle from app cold start through mobile verification, notification permission gating, target exam selection, and initial landing on the Home Feed.

```
[Cold App Start] ──▶ Splash Screen ──▶ Mobile Login Entry ──▶ OTP Verification ──▶ Target Exam Selection ──▶ Home Feed
```

---

## 2. Screen Specifications & Event Contracts

### Screen 01: Splash Screen (`SCR_SPLASH`)
* **Visual Reference:** `../screenshots/01_launch.png`
* **Came From:** Device App Launcher / Cold Start
* **Leads To:** Mobile Login Entry (`SCR_AUTH_LOGIN`) or Home Feed (`SCR_HOME_FEED`)
* **Events to Track:**
  * **`screen_view`**
    * *Trigger:* Screen completes initial animation and gate logic.
    * *Properties:*
      ```json
      {
        "screen_name": "splash",
        "entry_source": "cold_start",
        "is_first_session": true
      }
      ```

---

### Screen 02: Mobile Login Entry (`SCR_AUTH_LOGIN`)
* **Visual Reference:** `../screenshots/02_login_screen.png`
* **Came From:** Splash Screen
* **Leads To:** OTP Verification Screen (`SCR_AUTH_OTP`)
* **UI Elements:** Title ("Start your preparation"), Subtitle, Phone Number input with +91 country prefix, Google Assisted Phone Number Hint sheet.
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "login_mobile_input", "entry_source": "auth_gate"}`
  * **`user_action` (Phone Number Entered)**
    * *Trigger:* User inputs 10-digit number or selects a number from Google Phone Hint.
    * *Properties:*
      ```json
      {
        "screen_name": "login_mobile_input",
        "action_name": "phone_entered",
        "method": "manual | google_hint",
        "phone_length": 10
      }
      ```

---

### Screen 03: OTP Verification (`SCR_AUTH_OTP`)
* **Visual Reference:** `../screenshots/04_after_otp.png`
* **Came From:** Mobile Login Entry
* **Leads To:** Target Exam Selection (`SCR_GOAL_ONBOARDING`) or Home Feed
* **UI Elements:** 6-digit discrete input boxes, countdown timer ("Resend In 43s"), edit number link ("change"), auto-detection indicator.
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "login_otp_verification", "otp_method": "sms"}`
  * **`component_click` (Resend OTP Button)**
    * *Properties:* `{"screen_name": "login_otp_verification", "component_name": "resend_otp", "component_type": "button", "resend_count": 1}`
  * **`component_click` (Change Phone Number)**
    * *Properties:* `{"screen_name": "login_otp_verification", "component_name": "change_number", "component_type": "link", "destination": "login_mobile_input"}`
  * **`conversion` (Login Success)**
    * *Trigger:* 6-digit code verified successfully.
    * *Properties:*
      ```json
      {
        "conversion_name": "login_success",
        "auth_method": "sms_otp",
        "is_new_user": false,
        "user_id": "62382e83..."
      }
      ```

---

### Screen 04: Target Exam Selection (`SCR_GOAL_ONBOARDING`)
* **Visual Reference:** `../screenshots/57_onboarding_goal_selection.png`, `../screenshots/58_onboarding_categories_scrolled.png`
* **Came From:** OTP Verification OR Home Feed Exam Switcher
* **Leads To:** Home Feed (`SCR_HOME_FEED`)
* **UI Elements:** Domain switcher ("Govt. Exams" vs "Private Jobs"), Category switcher ("All Exams" vs "State Exams"), Popular Exam Chips, Search Bar, Sticky Bottom Bar ("2 Exams Selected", "Save").
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "onboarding_goal_selection", "entry_source": "auth_flow | home_switcher"}`
  * **`component_click` (Exam Chip Selected / Deselected)**
    * *Properties:* `{"screen_name": "onboarding_goal_selection", "component_name": "exam_chip", "component_type": "chip", "exam_name": "SSC CGL", "action": "select | deselect"}`
  * **`component_click` (Save Goals CTA)**
    * *Properties:*
      ```json
      {
        "screen_name": "onboarding_goal_selection",
        "component_name": "save_goals",
        "component_type": "button",
        "selected_count": 2,
        "selected_goals": ["SSC CGL", "RRB NTPC"],
        "destination": "home_feed"
      }
      ```
