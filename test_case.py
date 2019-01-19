from uiautomator import device as d
import time
import subprocess


# New Test Case
# Target App: Activity
# Number of actions: 1500
def test():
    d.click(730, 1833)
    # At M, android.widget.TextView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.long_click(525, 309)
    # At S0, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 587)
    # At S1, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d.click(154, 1203)
    # At S3, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.long_click(151, 2035)
    # At S4, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S0(1)
    d.click(180, 2243)
    # At S0, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 2487)
    # At S6, android.widget.FrameLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S6(2) to S0(1)
    d.click(1324, 683)
    # At S0, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S0(1)
    d.click(182, 1619)
    # At S0, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S0(1) to S6(2)
    d.click(1130, 683)
    # At S6, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    d(resourceId='com.android.packageinstaller:id/permission_allow_button').click()
    d.wait.update()
    time.sleep(1.5)
    # Permission State detected, 'Allow' selected
    # Transition from S6(2) to S0(1)
    d.click(148, 1203)
    # At S0, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S0(1) to S6(2)
    d.long_click(176, 1827)
    # At S6, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S6(2) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S1(2)
    d.click(720, 587)
    # At S1, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S1(2) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.long_click(182, 1827)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(1366, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S9(4)
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.long_click(154, 995)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S8(3) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S8(3)
    d.click(73, 136)
    # At S8, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1324, 683)
    # At S10, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Transition from S10(4) to S8(3)
    d.long_click(154, 995)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S8(3) to S9(4)
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(73, 136)
    # At S1, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S0(1)
    d.click(151, 1827)
    # At S0, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S0(1) to S6(2)
    d.long_click(182, 2035)
    # At S6, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S6(2) to S9(4)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S0(1)
    d.click(720, 446)
    # At S0, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.long_click(154, 995)
    # At S0, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S0(1) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(1329, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButtonRename
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S0(1)
    d.click(139, 787)
    # At S0, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S0(1) to S6(2)
    d.long_click(180, 1203)
    # At S6, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S6(2) to S1(2)
    d.click(720, 587)
    # At S1, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S1(2) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S1(2)
    d.click(720, 587)
    # At S1, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S8(3)
    d.click(152, 2035)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(1130, 683)
    # At S13, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Transition into invalid 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(139, 1411)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S8
    d.click(1366, 136)
    # At S8, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S8(3) to S9(4)
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S8(3)
    d.click(182, 1827)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S8(3) to S13(4)
    d.click(180, 1203)
    # At S13, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S13
    d.click(176, 995)
    # At S13, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S13(4) to S8(3)
    d.click(73, 136)
    # At S8, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S8(3) to S10(4)
    d.click(152, 2035)
    # At S10, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S10
    d.click(367, 1040)
    # At S10, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(73, 136)
    # At S14, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S14(5) to S8(3)
    d.click(1324, 683)
    # At S8, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S8
    d.click(525, 309)
    # At S8, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S8
    d.click(1130, 683)
    # At S8, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S8
    d.click(154, 995)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S8(3) to S13(4)
    d.click(73, 136)
    # At S13, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S13(4) to S10(4)
    d.click(720, 446)
    # At S10, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S10
    d.click(139, 1411)
    # At S10, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 1356)
    # At S15, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S15
    d.click(720, 2406)
    # At S15, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(1137, 1518)
    # At S16, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S16(6) to S15(5)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 2514)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Transition into invalid 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Still in 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 1412)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(719, 1173)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S18(7)
    d.click(719, 1299)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.click(73, 136)
    # At S17, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S17(6) to S8(3)
    d.click(1228, 136)
    # At S8, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(117, 377)
    # At S19, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S19(4) to S13(4)
    d.click(139, 1827)
    # At S13, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S13
    d.click(73, 136)
    # At S13, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S13(4) to S10(4)
    d.click(1130, 683)
    # At S10, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    # Transition from S10(4) to S8(3)
    d.click(156, 436)
    # At S8, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S8(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d.click(117, 1411)
    # At S20, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S20(3) to S13(4)
    d.long_click(225, 2243)
    # At S13, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S13(4) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S8(3)
    d.click(154, 995)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S8(3) to S13(4)
    d.long_click(139, 1827)
    # At S13, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S13(4) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S8(3)
    d.long_click(182, 1827)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S8(3) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S8(3)
    d.click(176, 1619)
    # At S8, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S8(3) to S13(4)
    d.long_click(180, 1203)
    # At S13, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S13(4) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(1329, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButtonRename
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(152, 1619)
    # At S21, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(148, 995)
    # At S22, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S22
    d.click(152, 1619)
    # At S22, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S22
    d.click(720, 446)
    # At S22, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S22(4) to S11(2)
    d.click(1136, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_end
    d.wait.update()
    time.sleep(1.5)
    d.click(1139, 1752)
    # At S23, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(975, 891)
    # At S23, android.widget.RadioButton, android:id/am_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S23
    d.click(975, 961)
    # At S23, android.widget.RadioButton, android:id/pm_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S23
    d.click(975, 961)
    # At S23, android.widget.RadioButton, android:id/pm_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S23
    d.click(606, 914)
    # At S23, android.widget.TextView, android:id/hours
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S23
    d.click(1139, 1752)
    # At S23, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(531, 807)
    # At S12, android.widget.TextView, android:id/date_picker_header_date
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S21(3)
    d.click(117, 1411)
    # At S21, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S21
    d.click(720, 446)
    # At S21, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S21
    d.long_click(148, 995)
    # At S21, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S21(3) to S1(2)
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(225, 1827)
    # At S24, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(525, 309)
    # At S25, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Transition from S25(4) to S24(3)
    d.click(1228, 136)
    # At S24, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.long_click(176, 712)
    # At S26, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S26(4) to S1(2)
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S26(4)
    d.click(1366, 136)
    # At S26, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S26(4) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S26(4)
    d.click(73, 136)
    # At S26, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(117, 377)
    # At S27, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S27
    d.click(1218, 136)
    # At S27, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S27
    d.click(1366, 136)
    # At S27, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S27(5) to S5(5)
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S27(5)
    d.click(367, 1292)
    # At S27, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1366, 136)
    # At S28, android.widget.TextView, de.rampro.activitydiary:id/action_show_hide_deleted
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 611)
    # At S29, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d.click(954, 1444)
    # At S30, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S30(8) to S29(7)
    d.click(720, 1577)
    # At S29, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S29(7) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S29(7)
    d.click(720, 450)
    # At S29, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Transition from S29(7) to S30(8)
    d.click(1139, 1444)
    # At S30, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S30(8) to S29(7)
    d.click(73, 136)
    # At S29, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S29(7) to S26(4)
    d.long_click(819, 135)
    # At S26, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S26
    d.click(73, 136)
    # At S26, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S26(4) to S27(5)
    d.click(152, 1382)
    # At S27, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S27
    d.click(367, 662)
    # At S27, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S27(5) to S26(4)
    d.click(1218, 136)
    # At S26, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S26
    d.click(117, 377)
    # At S26, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S26(4) to S25(4)
    d.long_click(152, 995)
    # At S25, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S25(4) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S24(3)
    d.click(1366, 136)
    # At S24, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S24(3) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S24(3)
    d.long_click(182, 1619)
    # At S24, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S24(3) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(73, 136)
    # At S31, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(73, 136)
    # At S32, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S32(7) to S31(6)
    d.click(225, 1203)
    # At S31, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.long_click(117, 787)
    # At S33, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S33(7) to S1(2)
    d.click(73, 136)
    # At S1, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S31(6)
    d.click(1366, 136)
    # At S31, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S31(6) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(117, 787)
    # At S34, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 446)
    # At S35, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S35(4) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 446)
    # At S36, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S36(3) to S11(2)
    d.click(720, 825)
    # At S11, android.widget.CheckBox, de.rampro.activitydiary:id/adjust_adjacent
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S36(3)
    d.click(1130, 683)
    # At S36, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Transition into invalid 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(1324, 683)
    # At S36, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S36(3)
    d.long_click(225, 995)
    # At S36, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S36(3) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(152, 787)
    # At S37, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 2487)
    # At S38, android.widget.FrameLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1228, 136)
    # At S39, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(1218, 136)
    # At S40, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S40
    d.click(182, 1047)
    # At S40, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S40(8) to S38(6)
    d.long_click(525, 309)
    # At S38, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S38(6) to S9(4)
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(73, 136)
    # At S41, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(117, 787)
    # At S42, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.long_click(720, 516)
    # At S44, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S44(8) to S7(2)
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S44(8)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S44, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S44(8) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S44(8)
    d.click(720, 2226)
    # At S44, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S44(8) to S11(2)
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(954, 1752)
    # At S23, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S44(8)
    d.click(720, 277)
    # At S44, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S44(8) to S11(2)
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1068, 996)
    # At S12, android.widget.ImageButton, android:id/next
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 996)
    # At S12, android.widget.ImageButton, android:id/prev
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 1950)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S44(8)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S44, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S44(8) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 1786)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(279, 1751)
    # At S23, android.widget.ImageButton, android:id/toggle_mode
    d.wait.update()
    time.sleep(1.5)
    d.swipe(1076, 1389, 1187, 1389, steps=10)
    # Swipe Right At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(954, 1585)
    # At S47, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S43
    d.click(720, 1569)
    # At S43, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(720, 1463)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(1139, 1752)
    # At S23, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1136, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(832, 914)
    # At S23, android.widget.TextView, android:id/minutes
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S23
    d.click(1139, 1752)
    # At S23, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(954, 1752)
    # At S23, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    d.click(279, 1751)
    # At S23, android.widget.ImageButton, android:id/toggle_mode
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S47(4)
    d.swipe(1076, 1389, 1076, 1447, steps=10)
    # Scroll up At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(312, 1382)
    # At S47, android.widget.EditText, android:id/input_hour
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S47
    d.swipe(1076, 1389, 965, 1389, steps=10)
    # Swipe Left At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 1187, 1389, steps=10)
    # Swipe Right At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1447, steps=10)
    # Scroll up At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1331, steps=10)
    # Scroll down At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(954, 1585)
    # At S47, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S11(2)
    d.click(1136, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(279, 1751)
    # At S23, android.widget.ImageButton, android:id/toggle_mode
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S47(4)
    d.long_click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S47
    d.swipe(1076, 1389, 965, 1389, steps=10)
    # Swipe Left At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1331, steps=10)
    # Scroll down At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(1139, 1585)
    # At S47, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S11(2)
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S43(7)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S45(8)
    d.click(73, 136)
    # At S45, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S45(8) to S41(5)
    d.click(1228, 136)
    # At S41, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(1218, 136)
    # At S49, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.click(152, 712)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(73, 136)
    # At S50, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S50(7) to S42(6)
    d.click(525, 309)
    # At S42, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S42
    d.long_click(152, 995)
    # At S42, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S42(6) to S14(5)
    d.click(73, 136)
    # At S14, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S14(5) to S41(5)
    d.click(1130, 683)
    # At S41, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Transition into invalid 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(1324, 683)
    # At S41, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S41(5)
    d.click(720, 446)
    # At S41, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d.click(1366, 136)
    # At S51, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S51(3) to S9(4)
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S37(5)
    d.click(73, 136)
    # At S37, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 446)
    # At S52, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S52
    d.click(720, 446)
    # At S52, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S52
    d.click(152, 995)
    # At S52, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S52(6) to S14(5)
    d.click(73, 136)
    # At S14, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S14(5) to S37(5)
    d.click(182, 1203)
    # At S37, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S37(5) to S38(6)
    d.click(152, 995)
    # At S38, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S38
    d.long_click(152, 995)
    # At S38, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S38(6) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S39(7)
    d.click(1324, 683)
    # At S39, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S39(7) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S37(5)
    d.click(1324, 683)
    # At S37, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S37(5) to S7(2)
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S37(5)
    d.click(1366, 136)
    # At S37, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S37(5) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S37(5)
    d.click(1324, 683)
    # At S37, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S37(5) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S37(5)
    d.click(73, 136)
    # At S37, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S37(5) to S52(6)
    d.click(367, 914)
    # At S52, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 267)
    # At S53, android.widget.Spinner, de.rampro.activitydiary:id/timeframeSpinner
    d.wait.update()
    time.sleep(1.5)
    d.click(657, 264)
    # At S54, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S54(8) to S53(7)
    d.swipe(720, 267, 720, 294, steps=10)
    # Scroll up At S53, android.widget.Spinner, de.rampro.activitydiary:id/timeframeSpinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S53(7) to S54(8)
    d.click(657, 435)
    # At S54, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    d.swipe(720, 267, 720, 294, steps=10)
    # Scroll up At S55, android.widget.Spinner, de.rampro.activitydiary:id/timeframeSpinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S55(9) to S54(8)
    d.click(657, 435)
    # At S54, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S54(8) to S55(9)
    d.swipe(720, 267, 5, 267, steps=10)
    # Swipe Left At S55, android.widget.Spinner, de.rampro.activitydiary:id/timeframeSpinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S55(9) to S54(8)
    d.click(657, 378)
    # At S54, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S54(8) to S53(7)
    d.long_click(720, 267)
    # At S53, android.widget.Spinner, de.rampro.activitydiary:id/timeframeSpinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S53(7) to S54(8)
    d.click(657, 321)
    # At S54, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S54(8) to S53(7)
    d.click(73, 136)
    # At S53, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S53(7) to S37(5)
    d.long_click(182, 1203)
    # At S37, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S37(5) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S51(3)
    d.click(525, 309)
    # At S51, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Transition from S51(3) to S41(5)
    d.click(117, 787)
    # At S41, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S50(7)
    d.long_click(525, 309)
    # At S50, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S41(5)
    d.click(156, 436)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S41(5)
    d.click(73, 136)
    # At S41, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S42(6)
    d.click(1324, 683)
    # At S42, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Transition from S42(6) to S41(5)
    d.click(1324, 683)
    # At S41, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S41(5)
    d.click(73, 136)
    # At S41, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S42(6)
    d.click(367, 1463)
    # At S42, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S42(6) to S15(5)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S17(6)
    d.click(720, 2213)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S17(6) to S18(7)
    d.click(719, 921)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.click(73, 136)
    # At S17, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S17(6) to S41(5)
    d.click(525, 309)
    # At S41, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.click(720, 446)
    # At S41, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.click(156, 436)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.long_click(525, 309)
    # At S41, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(525, 309)
    # At S56, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S56
    d.click(1130, 683)
    # At S56, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S56
    d.click(1228, 136)
    # At S56, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(152, 377)
    # At S57, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d.click(1324, 683)
    # At S58, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S58(5) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S56(3)
    d.click(720, 446)
    # At S56, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d.click(720, 446)
    # At S59, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S46
    d.click(531, 807)
    # At S46, android.widget.TextView, android:id/date_picker_header_date
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(531, 807)
    # At S12, android.widget.TextView, android:id/date_picker_header_date
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(720, 950)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.click(372, 996)
    # At S12, android.widget.ImageButton, android:id/prev
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S59(3)
    d.click(1324, 683)
    # At S59, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S59(3)
    d.long_click(152, 787)
    # At S59, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d.click(1228, 136)
    # At S60, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(73, 136)
    # At S61, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(367, 1166)
    # At S62, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S62(7) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S1(2) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S61(6)
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S61(6)
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S61(6)
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S9(4)
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S61(6)
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S61(6)
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S9(4)
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(720, 587)
    # At S1, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S1(2)
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S61(6)
    d.click(73, 136)
    # At S61, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S61(6) to S62(7)
    d.long_click(819, 135)
    # At S62, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S62
    d.long_click(819, 135)
    # At S62, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S62
    d.click(367, 1463)
    # At S62, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S62(7) to S15(5)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S17(6)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S18(7)
    d.click(719, 1677)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.click(720, 1082)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S17(6) to S18(7)
    d.click(719, 1173)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S18(7)
    d.click(1122, 1948)
    # At S18, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S18(7)
    d.click(719, 1047)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S17
    d.click(720, 1607)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S17(6) to S18(7)
    d.click(719, 1803)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.click(720, 887)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S17
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S18(7)
    d.click(719, 1173)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.click(720, 1997)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S17(6) to S18(7)
    d.click(719, 795)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S17
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S15(5)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S17(6)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S18(7)
    d.click(719, 1425)
    # At S18, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S18(7) to S17(6)
    d.click(720, 887)
    # At S17, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S17
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S15(5)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S17(6)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S17
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S17, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Transition from S17(6) to S15(5)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.click(720, 2406)
    # At S15, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S16(6)
    d.click(952, 1518)
    # At S16, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S16(6) to S15(5)
    d.click(720, 1686)
    # At S15, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1122, 1570)
    # At S63, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S63(6) to S15(5)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S15, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S15
    d.click(720, 966)
    # At S15, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S15
    d.click(720, 441)
    # At S15, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S16(6)
    d.click(720, 1377)
    # At S16, android.widget.EditText, android:id/edit
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S16
    d.click(1137, 1518)
    # At S16, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S16(6) to S15(5)
    d.click(73, 136)
    # At S15, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S15(5) to S57(4)
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.long_click(819, 135)
    # At S57, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S57
    d.click(1366, 136)
    # At S57, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S57(4) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(720, 587)
    # At S1, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S1(2) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(1366, 136)
    # At S57, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S57(4) to S9(4)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S57(4)
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(819, 135)
    # At S57, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(1366, 136)
    # At S57, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S57(4) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S57(4)
    d.click(73, 136)
    # At S57, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1218, 136)
    # At S64, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S64
    d.click(367, 1589)
    # At S64, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.long_click(720, 1630)
    # At S65, android.widget.TextView, de.rampro.activitydiary:id/aboutTextView
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S65
    d.click(720, 1630)
    # At S65, android.widget.TextView, de.rampro.activitydiary:id/aboutTextView
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S65
    d.click(73, 136)
    # At S65, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S65(6) to S57(4)
    d.click(819, 135)
    # At S57, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(819, 135)
    # At S57, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(152, 377)
    # At S57, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S57(4) to S58(5)
    d.click(1366, 136)
    # At S58, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S58(5) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S56(3)
    d.click(73, 136)
    # At S56, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(367, 1166)
    # At S66, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S66(4) to S9(4)
    d.click(1329, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButtonRename
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S41(5)
    d.click(152, 995)
    # At S41, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S50(7)
    d.click(117, 787)
    # At S50, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S50
    d.click(1228, 136)
    # At S50, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S49(6)
    d.long_click(117, 377)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S49(6)
    d.click(73, 136)
    # At S49, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.long_click(117, 712)
    # At S67, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S67(7) to S49(6)
    d.click(117, 377)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S49(6) to S50(7)
    d.click(156, 436)
    # At S50, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S51(3)
    d.click(139, 436)
    # At S51, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S51(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S51(3)
    d.click(1324, 683)
    # At S51, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S51(3) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S51(3)
    d.click(1130, 683)
    # At S51, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Transition into invalid 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(73, 136)
    # At S51, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # back() into Unknown State
    d.click(117, 995)
    # At S68, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S68(4) to S14(5)
    d.click(73, 136)
    # At S14, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S14(5) to S51(3)
    d.long_click(152, 995)
    # At S51, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S51(3) to S5(5)
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S56(3)
    d.click(139, 436)
    # At S56, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S56
    d.long_click(152, 787)
    # At S56, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S60(5)
    d.click(1324, 683)
    # At S60, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S60
    d.click(73, 136)
    # At S60, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(367, 1589)
    # At S69, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S69(6) to S65(6)
    d.click(73, 136)
    # At S65, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S65(6) to S60(5)
    d.click(720, 446)
    # At S60, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S60
    d.click(156, 436)
    # At S60, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S60
    d.click(1366, 136)
    # At S60, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S60(5) to S5(5)
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S60(5)
    d.long_click(525, 309)
    # At S60, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S60(5) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S60(5)
    d.click(1228, 136)
    # At S60, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S60(5) to S61(6)
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(73, 136)
    # At S61, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S61(6) to S62(7)
    d.click(367, 1589)
    # At S62, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S62(7) to S65(6)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S65, android.widget.ScrollView, (No resource.id)
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S65
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S65, android.widget.ScrollView, (No resource.id)
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S65
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S65, android.widget.ScrollView, (No resource.id)
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S65
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S65, android.widget.ScrollView, (No resource.id)
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S65
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S65, android.widget.ScrollView, (No resource.id)
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S65
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S65, android.widget.ScrollView, (No resource.id)
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S65
    d.click(73, 136)
    # At S65, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S65(6) to S61(6)
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S61(6)
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S61(6)
    d.click(1218, 136)
    # At S61, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(73, 136)
    # At S61, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S61(6) to S62(7)
    d.click(367, 1166)
    # At S62, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S62(7) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S61(6)
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S5(5)
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S61(6)
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.long_click(819, 135)
    # At S61, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S61
    d.click(1366, 136)
    # At S61, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S61(6) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Still in 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(730, 1833)
    # At M, android.widget.TextView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1366, 136)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(1130, 683)
    # At S41, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.click(1366, 136)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S5(5)
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(1228, 136)
    # At S41, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S49(6)
    d.click(819, 135)
    # At S49, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.click(152, 712)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S49(6) to S50(7)
    d.long_click(117, 787)
    # At S50, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S5(5)
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1218, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S56(3)
    d.long_click(525, 309)
    # At S56, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S9(4)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S56(3)
    d.click(1324, 683)
    # At S56, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S59(3)
    d.long_click(525, 309)
    # At S59, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S9(4)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S59(3)
    d.click(73, 136)
    # At S59, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(129, 436)
    # At S70, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S70
    d.click(367, 1166)
    # At S70, android.support.v7.widget.LinearLayoutCompat, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S70(4) to S9(4)
    d.click(1218, 136)
    # At S9, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S59(3)
    d.click(720, 446)
    # At S59, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(531, 807)
    # At S12, android.widget.TextView, android:id/date_picker_header_date
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(720, 1337)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1068, 996)
    # At S12, android.widget.ImageButton, android:id/next
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S59(3)
    d.long_click(152, 787)
    # At S59, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S9(4)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S59(3)
    d.click(525, 309)
    # At S59, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S59(3)
    d.click(68, 493)
    # At S59, android.widget.TextView, de.rampro.activitydiary:id/note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(730, 1833)
    # At M, android.widget.TextView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.long_click(525, 309)
    # At S59, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S59(3)
    d.click(720, 446)
    # At S59, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S59(3)
    d.long_click(152, 787)
    # At S59, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(720, 587)
    # At S9, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S9(4) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S9(4)
    d.click(73, 136)
    # At S9, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S59(3)
    d.click(720, 446)
    # At S59, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S59(3) to S11(2)
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(720, 1056)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1136, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(1139, 1752)
    # At S23, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S56(3)
    d.click(152, 787)
    # At S56, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S56
    d.click(1130, 683)
    # At S56, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S56
    d.click(720, 446)
    # At S56, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S56
    d.long_click(525, 309)
    # At S56, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S9(4)
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S9
    d.click(1149, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(73, 136)
    # At S1, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S41(5)
    d.click(1324, 683)
    # At S41, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.click(156, 436)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.long_click(152, 995)
    # At S41, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S41(5)
    d.click(73, 136)
    # At S41, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S42(6)
    d.long_click(117, 787)
    # At S42, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S42(6) to S43(7)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S43, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S43(7) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 2360)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 807)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.long_click(720, 423)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.long_click(720, 2360)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 423)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.click(720, 423)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.click(1136, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(954, 1752)
    # At S23, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S11(2)
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 1569)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.long_click(720, 2360)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(720, 1715)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 996)
    # At S12, android.widget.ImageButton, android:id/prev
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 807)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S45(8)
    d.long_click(720, 423)
    # At S45, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S45(8) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S45(8)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S45, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S45
    d.click(1376, 136)
    # At S45, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S71, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S71
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S71, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S71(9) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S46
    d.swipe(720, 1351, 1174, 1351, steps=10)
    # Swipe Right At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.click(372, 996)
    # At S12, android.widget.ImageButton, android:id/prev
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(531, 807)
    # At S12, android.widget.TextView, android:id/date_picker_header_date
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(372, 730)
    # At S46, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S46
    d.click(1063, 1877)
    # At S46, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S71(9)
    d.click(967, 135)
    # At S71, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S71
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S71, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 1439)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.click(1366, 136)
    # At S72, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.click(720, 358)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.long_click(720, 2201)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S7(2) to S72(10)
    d.long_click(720, 1097)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.long_click(720, 1439)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.click(720, 716)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(1136, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/time_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S23(3)
    d.click(279, 1751)
    # At S23, android.widget.ImageButton, android:id/toggle_mode
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S47(4)
    d.swipe(1076, 1389, 1187, 1389, steps=10)
    # Swipe Right At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(312, 1382)
    # At S47, android.widget.EditText, android:id/input_hour
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 965, 1389, steps=10)
    # Swipe Left At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(312, 1382)
    # At S47, android.widget.EditText, android:id/input_hour
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 1076, 1447, steps=10)
    # Scroll up At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1187, 1389, steps=10)
    # Swipe Right At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1447, steps=10)
    # Scroll up At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.click(279, 1584)
    # At S47, android.widget.ImageButton, android:id/toggle_mode
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S23(3)
    d.click(279, 1751)
    # At S23, android.widget.ImageButton, android:id/toggle_mode
    d.wait.update()
    time.sleep(1.5)
    # Transition from S23(3) to S47(4)
    d.swipe(1076, 1389, 965, 1389, steps=10)
    # Swipe Left At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1187, 1389, steps=10)
    # Swipe Right At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 965, 1389, steps=10)
    # Swipe Left At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(312, 1382)
    # At S47, android.widget.EditText, android:id/input_hour
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 1076, 1447, steps=10)
    # Scroll up At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(312, 1382)
    # At S47, android.widget.EditText, android:id/input_hour
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 1187, 1389, steps=10)
    # Swipe Right At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 965, 1389, steps=10)
    # Swipe Left At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 1076, 1331, steps=10)
    # Scroll down At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1331, steps=10)
    # Scroll down At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(312, 1382)
    # At S47, android.widget.EditText, android:id/input_hour
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.swipe(1076, 1389, 1076, 1331, steps=10)
    # Scroll down At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.long_click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1447, steps=10)
    # Scroll up At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1515)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.swipe(1076, 1389, 1076, 1331, steps=10)
    # Scroll down At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(2.0)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.long_click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.long_click(1076, 1389)
    # At S47, android.widget.Spinner, android:id/am_pm_spinner
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S48(5)
    d.click(1013, 1389)
    # At S48, android.widget.CheckedTextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S48(5) to S47(4)
    d.click(443, 1382)
    # At S47, android.widget.EditText, android:id/input_minute
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S47
    d.click(954, 1585)
    # At S47, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S47(4) to S11(2)
    d.click(437, 720)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_end
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.click(720, 1463)
    # At S46, android.widget.TextView, android:id/text1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1068, 996)
    # At S12, android.widget.ImageButton, android:id/next
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    # back() into Unknown State
    d.swipe(720, 886, 720, 215, steps=10)
    # Scroll down At S73, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S73(4) to S72(10)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S7(2) to S72(10)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.click(1366, 136)
    # At S72, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.long_click(720, 2201)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 825)
    # At S11, android.widget.CheckBox, de.rampro.activitydiary:id/adjust_adjacent
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.click(967, 135)
    # At S72, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.long_click(967, 135)
    # At S72, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S72
    d.click(720, 716)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(1366, 136)
    # At S11, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.swipe(720, 1385, 1435, 1385, steps=10)
    # Swipe Right At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.click(878, 1877)
    # At S12, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(437, 543)
    # At S11, android.widget.Button, de.rampro.activitydiary:id/date_start
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S12(3)
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 1790, steps=10)
    # Scroll up At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 720, 912, steps=10)
    # Scroll down At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S12, com.android.internal.widget.ViewPager, android:id/day_picker_view_pager
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S12
    d.click(372, 730)
    # At S12, android.widget.TextView, android:id/date_picker_header_year
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S46(4)
    d.swipe(720, 1351, 266, 1351, steps=10)
    # Swipe Left At S46, android.widget.ListView, android:id/date_picker_year_picker
    d.wait.update()
    time.sleep(2.0)
    # Transition from S46(4) to S12(3)
    d.click(1063, 1877)
    # At S12, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(3) to S11(2)
    d.click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.long_click(720, 1037)
    # At S11, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S11
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.click(967, 135)
    # At S72, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.long_click(720, 716)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.long_click(720, 1820)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.long_click(720, 1097)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S7
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.long_click(720, 1439)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S7(2) to S72(10)
    d.swipe(720, 1385, 720, 215, steps=10)
    # Scroll down At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.long_click(720, 1439)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.click(1137, 1512)
    # At S7, android.widget.Button, android:id/button1
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S7(2) to S72(10)
    d.swipe(720, 1385, 5, 1385, steps=10)
    # Swipe Left At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S11(2) to S72(10)
    d.long_click(720, 2201)
    # At S72, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S72(10) to S7(2)
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.long_click(720, 1288)
    # At S7, android.widget.EditText, de.rampro.activitydiary:id/noteText
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(952, 1512)
    # At S7, android.widget.Button, android:id/button2
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(2) to S72(10)
    d.swipe(720, 1385, 720, 2555, steps=10)
    # Scroll up At S72, android.support.v7.widget.RecyclerView, de.rampro.activitydiary:id/history_list
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S72
    d.click(73, 136)
    # At S72, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S72(10) to S41(5)
    d.click(117, 787)
    # At S41, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S50(7)
    d.click(1366, 136)
    # At S50, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S9(4)
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(540, 319)
    # At S9, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(1329, 298)
    # At S9, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButtonRename
    d.wait.update()
    time.sleep(1.5)
    # Transition from S9(4) to S1(2)
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S39(7)
    d.click(1130, 683)
    # At S39, android.widget.ImageButton, de.rampro.activitydiary:id/fab_attach_picture
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    #Transition into invalid 3rd party app
    d.wait.update()
    time.sleep(2.0)
    d.click(212, 436)
    # At S39, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S39(7)
    d.click(182, 1203)
    # At S39, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S39(7) to S38(6)
    d.click(182, 1203)
    # At S38, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S38(6) to S39(7)
    d.long_click(152, 995)
    # At S39, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S39(7) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(73, 136)
    # At S1, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S39(7)
    d.click(1324, 683)
    # At S39, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S39
    d.long_click(182, 1203)
    # At S39, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S39(7) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(1228, 136)
    # At S41, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S49(6)
    d.click(819, 135)
    # At S49, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.click(117, 377)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S49(6) to S50(7)
    d.long_click(525, 309)
    # At S50, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S56(3)
    d.click(1228, 136)
    # At S56, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S57(4)
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(1218, 136)
    # At S57, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S57
    d.click(152, 377)
    # At S57, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S57(4) to S58(5)
    d.click(720, 2487)
    # At S58, android.widget.FrameLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S58
    d.click(152, 787)
    # At S58, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S58(5) to S56(3)
    d.click(1366, 136)
    # At S56, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S56(3)
    d.click(1228, 136)
    # At S56, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S56(3) to S57(4)
    d.long_click(152, 377)
    # At S57, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S57(4) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Possible Crash Detected
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 1379)
    # At S74, android.widget.Button, android:id/aerr_restart
    d.wait.update()
    time.sleep(1.5)
    # -Possible Crash Occurred-
    d.click(730, 1833)
    # At M, android.widget.TextView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Continue Testing
    d.click(1366, 136)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(1366, 136)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(1324, 683)
    # At S41, android.widget.ImageButton, de.rampro.activitydiary:id/fab_edit_note
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S41
    d.long_click(525, 309)
    # At S41, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(1228, 136)
    # At S41, android.widget.ImageView, de.rampro.activitydiary:id/search_button
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S49(6)
    d.click(819, 135)
    # At S49, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.click(1218, 136)
    # At S49, android.widget.ImageView, de.rampro.activitydiary:id/search_close_btn
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.long_click(152, 712)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S49(6)
    d.click(1366, 136)
    # At S49, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(1097, 1684)
    # At S2, android.widget.Button, de.rampro.activitydiary:id/okColorButton
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(3) to S5(5)
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S49(6)
    d.click(1366, 136)
    # At S49, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S49(6)
    d.click(1366, 136)
    # At S49, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S49(6)
    d.click(819, 135)
    # At S49, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.click(819, 135)
    # At S49, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S49
    d.long_click(819, 135)
    # At S49, android.widget.EditText, de.rampro.activitydiary:id/search_src_text
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S49
    d.long_click(117, 377)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(73, 136)
    # At S1, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S1(2) to S49(6)
    d.click(1366, 136)
    # At S49, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S49(6) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S49(6)
    d.click(117, 377)
    # At S49, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S49(6) to S50(7)
    d.long_click(117, 787)
    # At S50, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S50(7) to S5(5)
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(720, 587)
    # At S5, android.widget.ImageView, de.rampro.activitydiary:id/edit_activity_color
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S5(5) to S2(3)
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.long_click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S2
    d.click(315, 1681)
    # At S2, android.widget.EditText, de.rampro.activitydiary:id/hexCode
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.press.back()
    #Self Transition Limit Reached
    d.wait.update()
    time.sleep(2.0)
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1366, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(73, 136)
    # At S5, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(720, 446)
    # At S41, android.view.ViewGroup, de.rampro.activitydiary:id/header_area
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S11(2)
    d.click(73, 136)
    # At S11, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S11(2) to S41(5)
    d.long_click(525, 309)
    # At S41, android.widget.RelativeLayout, de.rampro.activitydiary:id/activity_background
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S1(2)
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(1366, 136)
    # At S1, android.widget.TextView, de.rampro.activitydiary:id/action_edit_done
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S41(5)
    d.click(1366, 136)
    # At S41, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S41(5) to S5(5)
    d.click(1218, 136)
    # At S5, android.widget.TextView, de.rampro.activitydiary:id/action_edit_delete
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S41(5)
    d.click(73, 136)
    # At S41, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S41(5) to S42(6)
    d.click(1366, 136)
    # At S42, android.widget.TextView, de.rampro.activitydiary:id/action_add_activity
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Transition from S42(6) to S5(5)
    d.long_click(615, 319)
    # At S5, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1314, 298)
    # At S5, android.widget.ImageButton, de.rampro.activitydiary:id/quickFixButton1
    d.wait.update()
    time.sleep(1.5)
    # Transition from S5(5) to S1(2)
    d.long_click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S1
    d.click(720, 319)
    # At S1, android.widget.EditText, de.rampro.activitydiary:id/edit_activity_name
    d.wait.update()
    time.sleep(1.5)
    d(focused=True).clear_text()
    d.wait.update()
    time.sleep(1.5)
    # Removed any text
    d(focused=True).set_text('98ab')
    d.wait.update()
    time.sleep(1.5)
    # Entered 98ab
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # Self Transition in S1
    d.click(73, 136)
    # At S1, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S42(6)
    d.click(156, 436)
    # At S42, android.widget.TextView, de.rampro.activitydiary:id/duration_label
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S42
    d.long_click(117, 787)
    # At S42, android.widget.FrameLayout, de.rampro.activitydiary:id/select_card_view
    d.wait.update()
    time.sleep(1.5)
    # Transition from S42(6) to S43(7)
    subprocess.call('adb shell am force-stop de.rampro.activitydiary')
    time.sleep(1.5)


if __name__ == '__main__':
    test()
    # -End Test Case-
    # -Number of crashes detected: 1
    # Elapsed Time: 02:43:55
