# Product Journey 05: Daily News, Study Material, Account & Utilities

**Owner:** Product & Retention Pod  
**Target Platform:** Testbook Android App  

---

## 1. Journey Overview & Wireflow

This journey maps retention and daily habit-forming features: reading daily current affairs digests, bookmarking news, reviewing study notes and chapter PDFs, managing referral earnings, inspecting transaction receipts, and switching app language.

```
[Navigation Drawer] ──┬──▶ Daily Current Affairs ──▶ Saved News / Bookmarks
                      ├──▶ Study Notes Overview ──▶ Chapter PDF Notes ──▶ Notes Paywall Sheet
                      ├──▶ Refer & Earn Dashboard
                      ├──▶ Transactions History ──▶ Detailed Order Receipt
                      └──▶ App Language Switcher
```

---

## 2. Screen Specifications & Event Contracts

### Screen 21: Daily Current Affairs Digest (`SCR_CURRENT_AFFAIRS`)
* **Visual Reference:** `../screenshots/SCR_CURRENT_AFFAIRS.png`
* **Came From:** Navigation Drawer ("Daily Current Affairs")
* **Leads To:** Saved News (`SCR_CA_BOOKMARKS`) or Free Quizzes (`SCR_FREE_QUIZZES`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "current_affairs_feed", "active_date": "2026-09-23"}`
  * **`component_click` (Save / Bookmark News CTA)**
    * *Properties:* `{"screen_name": "current_affairs_feed", "component_name": "bookmark_news_btn", "component_type": "button", "article_title": "23rd September Current Affairs"}`

---

### Screen 22: Study Notes Overview & Chapter Notes (`SCR_STUDY_NOTES` & `SCR_CHAPTER_NOTES`)
* **Visual Reference:** `../screenshots/SCR_STUDY_NOTES.png`, `../screenshots/SCR_CHAPTER_NOTES.png`
* **Came From:** Tests Tab OR Navigation Drawer
* **Leads To:** Notes Locked Paywall Sheet (`SCR_NOTES_LOCKED_PAYWALL`)
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "study_notes_overview", "active_subject": "Mathematics"}`
  * **`component_click` (Locked Note Card Tap)**
    * *Properties:* `{"screen_name": "chapter_notes", "component_name": "locked_note_card", "component_type": "card", "note_title": "Types of Ratios", "is_locked": true, "destination": "notes_paywall_sheet"}`

---

### Screen 23: Refer & Earn Dashboard (`SCR_REFER_AND_EARN`)
* **Visual Reference:** `../screenshots/SCR_REFER_AND_EARN.png`
* **Came From:** Navigation Drawer ("Refer & Earn")
* **Leads To:** WhatsApp Intent or OS Share Sheet
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "refer_and_earn_dashboard"}`
  * **`user_action` (Share Referral Code CTA)**
    * *Properties:* `{"screen_name": "refer_and_earn_dashboard", "action_name": "share_referral_code", "referral_code": "O834MK", "channel": "whatsapp | native_share"}`

---

### Screen 24: Transactions History & Order Receipt (`SCR_TRANSACTIONS` & `SCR_TRANSACTION_RECEIPT`)
* **Visual Reference:** `../screenshots/SCR_TRANSACTIONS.png`, `../screenshots/SCR_TRANSACTION_RECEIPT.png`
* **Came From:** Navigation Drawer ("Transactions")
* **Events to Track:**
  * **`screen_view` (Transactions List)**
    * *Properties:* `{"screen_name": "transactions_history", "orders_count": 5}`
  * **`screen_view` (Order Receipt)**
    * *Properties:* `{"screen_name": "order_receipt", "order_id": "69eefbd25d...", "status": "Payment Successful", "amount_paid": 1.0}`

---

### Screen 25: App Language Switcher (`SCR_APP_LANGUAGE`)
* **Visual Reference:** `../screenshots/SCR_APP_LANGUAGE.png`
* **Came From:** Navigation Drawer ("Language")
* **Events to Track:**
  * **`screen_view`**
    * *Properties:* `{"screen_name": "change_language"}`
  * **`state_change` (Language Changed)**
    * *Properties:* `{"screen_name": "change_language", "state_name": "app_language", "from_state": "English", "to_state": "Hindi | Marathi | Telugu"}`
