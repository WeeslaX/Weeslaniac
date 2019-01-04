from uiautomator import device as d
import time
import subprocess

# New Test Case
# Target: 100 actions
d.click(53, 1066) # At M, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2)
d.long_click(945, 1641) # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
d.long_click(540, 585) # At S1, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2)
d.click(861, 1004) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2)
# Transition from S2(3) to S1(2)
d.click(540, 585) # At S1, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2)
d.click(540, 1155) # At S3, android.view.View, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S3
d.swipe(540, 1195, 540, 885, steps=5)
 # Scroll down At S3, android.widget.ListView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S3
d.swipe(540, 1195, 140, 1195, steps=5)
 # Swipe Left At S3, android.widget.ListView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S3
d.click(540, 1470) # At S3, android.view.View, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S3
d.swipe(540, 1195, 540, 1505, steps=5)
 # Scroll up At S3, android.widget.ListView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S3
d.swipe(540, 1195, 940, 1195, steps=5)
 # Swipe Right At S3, android.widget.ListView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S3
d.click(540, 1585) # At S3, android.widget.Button, it.feio.android.omninotes.foss:id/done
d.wait.update()
time.sleep(2)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.long_click(456, 156) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.long_click(888, 156) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.click(600, 156) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
d.click(781, 1033) # At S4, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2)
d.click(540, 998) # At S5, android.widget.ImageView, it.feio.android.omninotes.foss:id/color_chooser
d.wait.update()
time.sleep(2)
d.click(432, 922) # At S6, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2)
d.click(432, 1114) # At S7, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S7
d.click(218, 1114) # At S7, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S7
d.click(232, 1342) # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultNeutral
d.wait.update()
time.sleep(2)
d.long_click(387, 909) # At S8, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S8
d.click(387, 909) # At S8, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S8
d.click(235, 1534) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultNeutral
d.wait.update()
time.sleep(2)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.click(540, 784) # At S5, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
d.wait.update()
time.sleep(2)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
d.click(540, 784) # At S9, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S9
d.click(540, 998) # At S9, android.widget.ImageView, it.feio.android.omninotes.foss:id/color_chooser
d.wait.update()
time.sleep(2)
#Transition from S9(5) to S6(5)
d.click(540, 998) # At S9, android.widget.ImageView, it.feio.android.omninotes.foss:id/color_chooser
d.wait.update()
time.sleep(2)
#Transition from S9(5) to S6(5)
d.long_click(540, 784) # At S9, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
d.wait.update()
time.sleep(2)
#Transition from S9(5) to S6(5)
d.long_click(540, 784) # At S9, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
d.wait.update()
time.sleep(2)
#Transition from S9(5) to S6(5)
d.click(540, 998) # At S9, android.widget.ImageView, it.feio.android.omninotes.foss:id/color_chooser
d.wait.update()
time.sleep(2)
#Transition from S9(5) to S6(5)
d.long_click(540, 784) # At S9, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
d.wait.update()
time.sleep(2)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.click(813, 1220) # At S9, android.widget.Button, it.feio.android.omninotes.foss:id/save
d.wait.update()
time.sleep(2)
# Transition from S9(5) to S1(2)
d.long_click(549, 447) # At S1, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.click(600, 156) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
# Transition from S1(2) to S4(3)
d.click(364, 1033) # At S4, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultNegative
d.wait.update()
time.sleep(2)
# Transition from S4(3) to S1(2)
d.long_click(744, 156) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.click(549, 447) # At S1, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S1
d.long_click(600, 156) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.long_click(550, 315) # At S1, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.long_click(550, 315) # At S1, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.click(84, 156) # At S1, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2)
d.long_click(600, 156) # At S10, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
# Self Transition in S10
d.click(456, 156) # At S10, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.long_click(456, 156) # At S10, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2)
d.long_click(945, 1641) # At S11, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2)
d.click(456, 156) # At S12, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2)
d.click(540, 1284) # At S13, android.widget.TextView, it.feio.android.omninotes.foss:id/timestamp
d.wait.update()
time.sleep(2)
d.click(550, 315) # At S14, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S14
d.long_click(744, 156) # At S14, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2)
# Self Transition in S14
d.click(540, 585) # At S14, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2)
# Transition from S14(7) to S3(3)
d.click(540, 777) # At S3, android.widget.TextView, it.feio.android.omninotes.foss:id/date_picker_year
d.wait.update()
time.sleep(2)
d.swipe(540, 1195, 940, 1195, steps=5)
 # Swipe Right At S15, android.widget.ListView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S15(4) to S3(3)
d.click(540, 777) # At S3, android.widget.TextView, it.feio.android.omninotes.foss:id/date_picker_year
d.wait.update()
time.sleep(2)
# Transition from S3(3) to S15(4)
d.swipe(540, 1195, 540, 885, steps=5)
 # Scroll down At S15, android.widget.ListView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(540, 527) # At S16, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/date_picker_month_and_day
d.wait.update()
time.sleep(2)
# Transition from S16(5) to S3(3)
d.click(540, 1585) # At S3, android.widget.Button, it.feio.android.omninotes.foss:id/done
d.wait.update()
time.sleep(2)
d.click(422, 445) # At S17, android.widget.Button, it.feio.android.omninotes.foss:id/hours
d.wait.update()
time.sleep(2)
# Self Transition in S17
d.click(642, 445) # At S17, android.widget.Button, it.feio.android.omninotes.foss:id/minutes
d.wait.update()
time.sleep(2)
# Self Transition in S17
d.click(797, 445) # At S17, android.widget.Button, it.feio.android.omninotes.foss:id/ampm_hitspace
d.wait.update()
time.sleep(2)
# Self Transition in S17
d.click(540, 1474) # At S17, android.widget.Button, it.feio.android.omninotes.foss:id/done_button
d.wait.update()
time.sleep(2)
d.click(882, 516) # At S18, android.widget.Switch, it.feio.android.omninotes.foss:id/repeat_switch
d.wait.update()
time.sleep(2)
d.long_click(298, 669) # At S19, android.widget.EditText, it.feio.android.omninotes.foss:id/interval
d.wait.update()
time.sleep(2)
# Self Transition in S19
d.click(303, 1163) # At S19, android.widget.Spinner, it.feio.android.omninotes.foss:id/endSpinner
d.wait.update()
time.sleep(2)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.long_click(462, 222) # At S20, android.widget.Spinner, it.feio.android.omninotes.foss:id/freqSpinner
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S20
d.swipe(462, 222, 462, 161, steps=5)
 # Scroll down At S20, android.widget.Spinner, it.feio.android.omninotes.foss:id/freqSpinner
d.wait.update()
time.sleep(2.5)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S20
d.long_click(298, 375) # At S20, android.widget.EditText, it.feio.android.omninotes.foss:id/interval
d.wait.update()
time.sleep(2)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.long_click(456, 156) # At S14, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2)
# Self Transition in S14
d.long_click(600, 156) # At S14, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
# Self Transition in S14
d.click(549, 447) # At S14, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
d.wait.update()
time.sleep(2)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.click(84, 156) # At S21, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2)
d.long_click(744, 156) # At S22, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2)
# Self Transition in S22
d.click(1020, 156) # At S22, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
d.click(774, 156) # At S23, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2)
# Transition from S23(10) to S22(9)
d.long_click(888, 156) # At S22, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(2)
# Self Transition in S22
d.click(888, 156) # At S22, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(2)
d.click(744, 156) # At S24, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2)
# Transition from S24(10) to S22(9)
d.click(540, 747) # At S22, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2)
# Self Transition in S22
d.click(744, 156) # At S22, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
d.click(1020, 156) # At S25, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
d.click(774, 300) # At S26, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2)
# Transition from S26(11) to S22(9)
d.click(540, 417) # At S22, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2)
# Transition from S22(9) to S21(8)
d.click(550, 315) # At S21, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S21
d.click(456, 156) # At S21, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2)
# Transition from S21(8) to S13(6)
d.click(540, 1140) # At S13, android.widget.TextView, it.feio.android.omninotes.foss:id/location
d.wait.update()
time.sleep(2)
# Transition from S13(6) to S21(8)
d.click(744, 156) # At S21, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2)
# Self Transition in S21
d.click(549, 447) # At S21, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
d.wait.update()
time.sleep(2)
d.press.back() # Close Keyboard
d.wait.update()
time.sleep(2.5)
# Self Transition in S21
d.long_click(540, 585) # At S21, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2)
# Transition from S21(8) to S2(3)
d.long_click(540, 851) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2)
# Self Transition in S2
d.click(540, 851) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2)
# Self Transition in S2
d.click(540, 851) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2)
# Self Transition in S2
d.long_click(540, 851) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2)
# Self Transition in S2
d.click(861, 1004) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2)
# Transition from S2(3) to S21(8)
d.long_click(744, 156) # At S21, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2)
# Self Transition in S21
d.long_click(600, 156) # At S21, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
# Self Transition in S21
d.click(1020, 156) # At S21, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
d.click(774, 1020) # At S27, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2)
d.press.back() #Transition into state with no package name
d.wait.update()
time.sleep(3)
d.click(600, 156) # At S21, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2)
# Transition from S21(8) to S4(3)
d.click(781, 1033) # At S4, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2)
# Transition from S4(3) to S5(4)
d.click(813, 1220) # At S5, android.widget.Button, it.feio.android.omninotes.foss:id/save
d.wait.update()
time.sleep(2)
# Self Transition in S5
d.click(540, 998) # At S5, android.widget.ImageView, it.feio.android.omninotes.foss:id/color_chooser
d.wait.update()
time.sleep(2)
# Transition from S5(4) to S6(5)
d.press.home()
# -End Test Case-
#-Number of crashes detected: 0
