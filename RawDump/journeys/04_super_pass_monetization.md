# Product Journey 04: Monetization, Pass Subscriptions & SuperCoaching

**Owner:** Product & Monetization Pod  
**Target Platform:** Testbook Android App  

---

## 1. Journey Overview & Wireflow

This journey maps the two primary revenue funnels of Testbook: SuperCoaching course subscriptions and Testbook Pass / Pass Pro renewals, through plan selection, coupon application, checkout gateway, dynamic UPI QR payments, and failure recovery.

```
[SuperCoaching Landing] ──▶ Super Plan Selection ──┬──▶ Payment Gateway ──┬──▶ Dynamic UPI QR ──▶ Payment Status
                                                   │                      │
[Pass Landing / Paywall] ─▶ Pass Plans & Benefits ─┘                      └──▶ Payment Failure Sheet ──(Retry)
```

---

## 2. Screen Specifications & Event Contracts

### Screen 16: SuperCoaching Landing Page (`SCR_SUPER_LANDING`)
* **Visual Reference:** `../screenshots/38_super_coaching_tab.png`, `../screenshots/39_super_coaching_scrolled.png`
* **Came From:** Home Feed (Bottom Tab "Super")
* **Leads To:** Super Plan Selection (`SCR_SUPER_PLANS`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "super_landing", "goal_name": "UPSC EPFO APFC 2026", "is_paid": false}`
  * **`component_view` (Urgency Offer Expiration Banner)**
    * *Properties:* `{"screen_name": "super_landing", "component_name": "offer_expiry_banner", "component_type": "banner", "time_remaining_secs": 1798}`
  * **`component_click` (Claim Offer Now Sticky CTA)**
    * *Properties:* `{"screen_name": "super_landing", "component_name": "claim_offer_now", "component_type": "button", "destination": "super_plan_selection"}`

---

### Screen 17: SuperCoaching Plan Selection & Coupon Sheet (`SCR_SUPER_PLANS`)
* **Visual Reference:** `../screenshots/40_super_plan_selection.png`, `../screenshots/41_super_plan_selection_full.png`
* **Came From:** SuperCoaching Landing Page
* **Leads To:** Payment Gateway (`SCR_PAYMENT_GATEWAY`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "super_plan_selection", "goal_name": "UPSC EPFO APFC 2026"}`
  * **`component_view` (Coupon Applied Celebration Dialog)**
    * *Properties:* `{"screen_name": "super_plan_selection", "component_name": "coupon_applied_dialog", "component_type": "modal", "coupon_code": "EPF026", "discount_pct": 16}`
  * **`state_change` (No Cost EMI Toggle)**
    * *Properties:* `{"screen_name": "super_plan_selection", "state_name": "no_cost_emi_toggle", "to_state": "enabled | disabled"}`
  * **`conversion` (Checkout Started)**
    * *Trigger:* Tapping "Proceed to Payment" sticky button.
    * *Properties:*
      ```json
      {
        "conversion_name": "checkout_started",
        "product_type": "super_coaching",
        "product_name": "UPSC EPFO APFC 2026",
        "plan_duration": "6_months",
        "original_amount": 4500,
        "payable_amount": 3000,
        "coupon_code": "EPF026"
      }
      ```

---

### Screen 18: Testbook Pass Renewal & Paywall (`SCR_PASS_PAYWALL`)
* **Visual Reference:** `../screenshots/48_pass_landing.png`, `../screenshots/49_pass_plans.png`, `../screenshots/50_pass_plan_durations.png`
* **Came From:** Home Feed (Bottom Tab "Pass" or Pass renewal cards)
* **Leads To:** Dynamic UPI QR Modal (`SCR_DYNAMIC_QR`) or Payment Gateway
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "pass_plans", "user_status": "expired", "renewal_price": 749}`
  * **`component_view` (Pass Expiry Alert Banner)**
    * *Properties:* `{"screen_name": "pass_plans", "component_name": "pass_expiry_alert", "component_type": "banner"}`
  * **`conversion` (Checkout Started - Pass)**
    * *Trigger:* Tapping "Buy Yearly Testbook Pass" sticky bar.
    * *Properties:*
      ```json
      {
        "conversion_name": "checkout_started",
        "product_type": "pass",
        "product_name": "Yearly Testbook Pass",
        "payable_amount": 749,
        "original_amount": 949
      }
      ```

---

### Screen 19: Dynamic UPI QR Code Modal (`SCR_DYNAMIC_QR`)
* **Visual Reference:** `../screenshots/53_pass_checkout.png`
* **Came From:** Pass Paywall OR Payment Gateway
* **Leads To:** Pass Payment Failure (`SCR_PASS_FAILURE_PAGE`) or Payment Success (`SCR_PAYMENT_SUCCESS`)
* **Events to Track:**
  * **`component_view` (Dynamic UPI QR Code Rendered)**
    * *Properties:* `{"screen_name": "upi_qr_modal", "component_name": "dynamic_qr", "component_type": "modal", "expiry_seconds": 600}`

---

### Screen 20: Consolidated Payment Gateway (`SCR_PAYMENT_GATEWAY`)
* **Visual Reference:** `../screenshots/42_make_payment_screen.png`, `../screenshots/43_qr_payment.png`
* **Came From:** Super Plan Selection OR Pass Paywall
* **Leads To:** UPI Intent / QR, Payment Failure Sheet, Payment Success
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "payment_gateway", "payable_amount": 3000, "product_name": "UPSC EPFO APFC"}`
  * **`component_click` (Payment Method Card Selected)**
    * *Properties:* `{"screen_name": "payment_gateway", "component_name": "payment_method", "component_type": "card", "method": "qr_code | card | netbanking"}`
  * **`conversion` (Payment Failed)**
    * *Trigger:* User cancels transaction or bank gateway returns failure.
    * *Properties:*
      ```json
      {
        "conversion_name": "payment_failed",
        "order_amount": 3000,
        "payment_method": "upi_qr",
        "failure_reason": "USER_CANCELLED | BANK_TIMEOUT"
      }
      ```
