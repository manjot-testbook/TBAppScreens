# Testbook Android: Engineering Implementation & Handover Specification (Unified Analytics Architecture)

**Audience:** Android Engineering Pod, QA Automation Engineers, Data Platform Engineers  
**Client Version:** 9.11.x+  
**Target Repository:** `/Users/manjotsingh/PycharmProjects/TB-Android/tbapp`  
**Primary Module:** `analytics-module`  
**Location:** `/Users/manjotsingh/DataspellProjects/OFFICE/OpenCode/2. Events Planning/`  

---

## 1. Architectural Goal

Replace the sprawling **428 bespoke event classes** in `analytics-module` with a clean, extensible, type-safe **Unified Analytics Engine** that:
1. Uses a compact taxonomy of 6 core UI events: `screen_view`, `screen_duration`, `component_view`, `component_click`, `user_action`, `state_change`, plus domain-level `conversion` events.
2. Automatically attaches a **Common Analytics Context** (`user_type`, `has_pass`, `screen_instance_id`, `app_version`, `session_id`) to every dispatched event.
3. Integrates with the Design System through zero-boilerplate UI wrappers (`TrackedButton`, `TrackedCard`, XML view extensions).
4. Routes seamlessly to the existing dispatchers (`WebEngage`, `Firebase`, `Mixpanel`, `Branch`, and debug `EventLoggingFlipperPlugin`).

---

## 2. Kotlin Architecture & Data Models

### 2.1. Common Analytics Context

```kotlin
package com.testbook.tbapp.analytics.core

import androidx.annotation.Keep
import com.testbook.tbapp.BuildConfig
import com.testbook.tbapp.prefs.MySharedPreferences
import java.util.UUID

@Keep
data class CommonAnalyticsContext(
    val appVersion: String = BuildConfig.VERSION_NAME,
    val appBuild: Int = BuildConfig.VERSION_CODE,
    val platform: String = "android",
    val osVersion: String = android.os.Build.VERSION.RELEASE,
    val deviceModel: String = "${android.os.Build.MANUFACTURER} ${android.os.Build.MODEL}",
    val sessionId: String = MySharedPreferences.getSessionId() ?: "unknown",
    val userId: String? = MySharedPreferences.getUserId(),
    val userType: String = if (MySharedPreferences.isPaidUser()) "paid" else "free",
    val hasActivePass: Boolean = MySharedPreferences.hasActivePass(),
    val hasSuperSubscription: Boolean = MySharedPreferences.hasSuperSubscription(),
    val currentScreen: String,
    val screenInstanceId: String,
    val previousScreen: String? = null,
    val timestamp: Long = System.currentTimeMillis()
)
```

### 2.2. Unified Event Interface & Event Types

```kotlin
package com.testbook.tbapp.analytics.core

import androidx.annotation.Keep

@Keep
sealed class UnifiedEvent {
    abstract val eventName: String
    abstract val properties: Map<String, Any?>

    // 1. Screen View
    data class ScreenView(
        val screenName: String,
        val entrySource: String? = null,
        val previousScreen: String? = null,
        val customProperties: Map<String, Any?> = emptyMap()
    ) : UnifiedEvent() {
        override val eventName: String = "screen_view"
        override val properties: Map<String, Any?>
            get() = mutableMapOf<String, Any?>(
                "screen_name" to screenName,
                "entry_source" to entrySource,
                "previous_screen" to previousScreen
            ).apply { putAll(customProperties) }
    }

    // 2. Screen Duration
    data class ScreenDuration(
        val screenName: String,
        val durationMs: Long
    ) : UnifiedEvent() {
        override val eventName: String = "screen_duration"
        override val properties: Map<String, Any?> = mapOf(
            "screen_name" to screenName,
            "duration_ms" to durationMs
        )
    }

    // 3. Component View (Exposed High-Value Components Only)
    data class ComponentView(
        val screenName: String,
        val componentName: String,
        val componentType: String,
        val componentId: String? = null,
        val position: Int? = null,
        val customProperties: Map<String, Any?> = emptyMap()
    ) : UnifiedEvent() {
        override val eventName: String = "component_view"
        override val properties: Map<String, Any?>
            get() = mutableMapOf<String, Any?>(
                "screen_name" to screenName,
                "component_name" to componentName,
                "component_type" to componentType,
                "component_id" to componentId,
                "position" to position
            ).apply { putAll(customProperties) }
    }

    // 4. Component Click (Interactive Elements)
    data class ComponentClick(
        val screenName: String,
        val componentName: String,
        val componentType: String,
        val componentId: String? = null,
        val action: String = "click",
        val destination: String? = null,
        val position: Int? = null,
        val customProperties: Map<String, Any?> = emptyMap()
    ) : UnifiedEvent() {
        override val eventName: String = "component_click"
        override val properties: Map<String, Any?>
            get() = mutableMapOf<String, Any?>(
                "screen_name" to screenName,
                "component_name" to componentName,
                "component_type" to componentType,
                "component_id" to componentId,
                "action" to action,
                "destination" to destination,
                "position" to position
            ).apply { putAll(customProperties) }
    }

    // 5. User Action (Search, Filter, Input)
    data class UserAction(
        val screenName: String,
        val actionName: String,
        val actionValue: Any? = null,
        val customProperties: Map<String, Any?> = emptyMap()
    ) : UnifiedEvent() {
        override val eventName: String = "user_action"
        override val properties: Map<String, Any?>
            get() = mutableMapOf<String, Any?>(
                "screen_name" to screenName,
                "action_name" to actionName,
                "action_value" to actionValue
            ).apply { putAll(customProperties) }
    }

    // 6. State Change
    data class StateChange(
        val screenName: String,
        val stateName: String,
        val fromState: String? = null,
        val toState: String
    ) : UnifiedEvent() {
        override val eventName: String = "state_change"
        override val properties: Map<String, Any?> = mapOf(
            "screen_name" to screenName,
            "state_name" to stateName,
            "from_state" to fromState,
            "to_state" to toState
        )
    }

    // 7. Domain / Conversion Event
    data class Conversion(
        val conversionName: String,
        val transactionId: String? = null,
        val productId: String? = null,
        val productType: String? = null,
        val amount: Double? = null,
        val customProperties: Map<String, Any?> = emptyMap()
    ) : UnifiedEvent() {
        override val eventName: String = conversionName
        override val properties: Map<String, Any?>
            get() = mutableMapOf<String, Any?>(
                "conversion_name" to conversionName,
                "transaction_id" to transactionId,
                "product_id" to productId,
                "product_type" to productType,
                "amount" to amount
            ).apply { putAll(customProperties) }
    }
}
```

---

## 3. Dispatcher Integration & Flipper Pipeline

The core dispatcher sits in `analytics-module` and handles context injection, multi-service forwarding, and Flipper interception:

```kotlin
package com.testbook.tbapp.analytics.core

import android.content.Context
import android.os.Bundle
import com.testbook.tbapp.EventLoggingFlipperPlugin
import com.testbook.tbapp.analytics.Analytics
import com.testbook.tbapp.analytics.FirebaseAnalyticsManager
import com.testbook.tbapp.analytics.WebEngageAnalytics
import java.util.UUID

object UnifiedAnalyticsTracker {

    private var currentScreenName: String = "unknown"
    private var currentScreenInstanceId: String = UUID.randomUUID().toString().take(8)
    private var previousScreenName: String? = null
    private var screenStartTime: Long = System.currentTimeMillis()

    fun onScreenStarted(screenName: String, entrySource: String? = null) {
        // Track duration of previous screen
        val duration = System.currentTimeMillis() - screenStartTime
        if (currentScreenName != "unknown") {
            post(UnifiedEvent.ScreenDuration(currentScreenName, duration))
        }

        previousScreenName = currentScreenName
        currentScreenName = screenName
        currentScreenInstanceId = UUID.randomUUID().toString().take(8)
        screenStartTime = System.currentTimeMillis()

        // Track new screen view
        post(
            UnifiedEvent.ScreenView(
                screenName = screenName,
                entrySource = entrySource,
                previousScreen = previousScreenName
            )
        )
    }

    fun post(event: UnifiedEvent, context: Context? = null) {
        val appContext = CommonAnalyticsContext(
            currentScreen = currentScreenName,
            screenInstanceId = currentScreenInstanceId,
            previousScreen = previousScreenName
        )

        val fullPayload = mutableMapOf<String, Any?>()
        fullPayload.putAll(event.properties)
        fullPayload["screen_instance_id"] = appContext.screenInstanceId
        fullPayload["user_type"] = appContext.userType
        fullPayload["has_active_pass"] = appContext.hasActivePass
        fullPayload["has_super_subscription"] = appContext.hasSuperSubscription
        fullPayload["app_version"] = appContext.appVersion
        fullPayload["session_id"] = appContext.sessionId

        // 1. Dispatch to WebEngage
        WebEngageAnalytics.pushAnEvent(event.eventName, fullPayload as HashMap<String, Any>)

        // 2. Dispatch to Firebase
        val bundle = Bundle()
        fullPayload.forEach { (key, value) ->
            when (value) {
                is String -> bundle.putString(key, value)
                is Int -> bundle.putInt(key, value)
                is Long -> bundle.putLong(key, value)
                is Double -> bundle.putDouble(key, value)
                is Boolean -> bundle.putBoolean(key, value)
            }
        }
        FirebaseAnalyticsManager.pushAnEvent(event.eventName, bundle)

        // 3. Dispatch to Flipper (Debug only)
        EventLoggingFlipperPlugin.getEventInterceptorPlugin().logUnifiedEventInFlipper(
            eventName = event.eventName,
            payload = fullPayload
        )
    }
}
```

---

## 4. UI Layer Integration (Zero Boilerplate)

### 4.1. Jetpack Compose Integration

Create reusable modifiers and composable wrappers:

```kotlin
package com.testbook.tbapp.base_ui.analytics

import androidx.compose.foundation.clickable
import androidx.compose.material.Button
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.ui.Modifier
import com.testbook.tbapp.analytics.core.UnifiedAnalyticsTracker
import com.testbook.tbapp.analytics.core.UnifiedEvent

/**
 * Auto tracks screen duration on Composable lifecycle
 */
@Composable
fun TrackScreen(screenName: String, entrySource: String? = null) {
    DisposableEffect(screenName) {
        UnifiedAnalyticsTracker.onScreenStarted(screenName, entrySource)
        onDispose { /* handled in tracker */ }
    }
}

/**
 * Standard Design System TrackedButton
 */
@Composable
fun TrackedButton(
    componentName: String,
    screenName: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    destination: String? = null,
    metadata: Map<String, Any?> = emptyMap(),
    content: @Composable () -> Unit
) {
    Button(
        modifier = modifier,
        onClick = {
            UnifiedAnalyticsTracker.post(
                UnifiedEvent.ComponentClick(
                    screenName = screenName,
                    componentName = componentName,
                    componentType = "button",
                    action = "click",
                    destination = destination,
                    customProperties = metadata
                )
            )
            onClick()
        }
    ) {
        content()
    }
}
```

### 4.2. XML / ViewBinding Integration

```kotlin
package com.testbook.tbapp.base_ui.analytics

import android.view.View
import com.testbook.tbapp.analytics.core.UnifiedAnalyticsTracker
import com.testbook.tbapp.analytics.core.UnifiedEvent

fun View.trackClick(
    screenName: String,
    componentName: String,
    componentType: String = "button",
    destination: String? = null,
    metadata: Map<String, Any?> = emptyMap(),
    action: (View) -> Unit
) {
    this.setOnClickListener { v ->
        UnifiedAnalyticsTracker.post(
            UnifiedEvent.ComponentClick(
                screenName = screenName,
                componentName = componentName,
                componentType = componentType,
                action = "click",
                destination = destination,
                customProperties = metadata
            )
        )
        action(v)
    }
}
```

---

## 5. Phased Rollout & Migration Strategy

```
Phase 1: Foundation (Sprint 1)
  ├── Implement UnifiedAnalyticsTracker in analytics-module
  ├── Implement CommonAnalyticsContext auto-injection
  └── Hook into EventLoggingFlipperPlugin for QA visibility

Phase 2: Core Funnels Instrumentation (Sprint 2)
  ├── Instrument Auth (OTPLessLoginActivity, VerifyOTPDialogFragment)
  ├── Instrument Onboarding (OnboardingActivity, ExamCategoriesFragment)
  └── Instrument Home Screen & Navigation Shell (DashboardActivity, HomeFragment)

Phase 3: Revenue & Assessment Instrumentation (Sprint 3)
  ├── Instrument Test Engine (PreInstructionsFragment, TestAttemptActivity, TestAnalysis2Activity)
  ├── Instrument Pass Paywall (PassOnePurchaseActivity, PassPaymentFailureActivity)
  └── Instrument SuperCoaching & Checkout (TbSuperLandingActivity, AllPaymentsActivity)

Phase 4: Deprecation & Clean Up (Sprint 4)
  ├── Run parallel validation between legacy and clean events in WebEngage
  ├── Deprecate 428 legacy classes in analytics_events/
  └── Remove unused strings in AllEventsNameSchemes.java
```

---

## 6. Verification & QA Sign-Off Guide

1. **Flipper Desktop Verification:**
   * Launch Flipper Desktop 0.273.0 on host Mac.
   * Connect emulator `emulator-5554` via USB / ADB.
   * Enable the `TestBookAnalyticsLogging` plugin.
   * Verify that every click or view appears with its standardized `eventName` (`screen_view`, `component_click`, etc.) and the complete `context` block.
2. **Logcat Verification Command:**
   ```bash
   adb logcat -v time | grep -E "WebEngage|FirebaseAnalytics|TestBookAnalyticsLogging"
   ```
3. **Acceptance Criteria:**
   * No hardcoded `LANDED_*` or `CLICKED_*` events sent by newly instrumented screens.
   * `screen_instance_id` changes deterministically on every screen transition.
   * All conversion events (`test_started`, `test_submitted`, `checkout_started`, `payment_success`, `payment_failed`) retain critical business fields.
