from uiautomator import device as d
import time
import subprocess

# New Test Case
# Target: 250 actions
d.click(40, 1121) # At M, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(870, 1584) # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2.5)
d.long_click(853, 78) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(3)
# Self Transition in S1
d.long_click(870, 1584) # At S1, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(3)
# Transition from S1(2) to S0(1)
d.click(5, 68) # At S0, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(726, 78) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
# Self Transition in S2
d.long_click(26, 236) # At S2, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(3)
# Self Transition in S2
d.click(853, 78) # At S2, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(2.5)
# Transition from S2(2) to S0(1)
d.long_click(853, 78) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(3)
# Self Transition in S0
d.click(726, 78) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(663, 94) # At S3, android.widget.ImageView, it.feio.android.omninotes.foss:id/search_voice_btn
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(958, 78) # At S3, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tags
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(831, 78) # At S4, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_uncomplete_checklists
d.wait.update()
time.sleep(2.5)
d.click(958, 78) # At S5, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tags
d.wait.update()
time.sleep(2.5)
# Self Transition in S5
d.click(5, 68) # At S5, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S5(4) to S0(1)
d.click(980, 78) # At S0, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(560, 78) # At S6, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S6(2) to S0(1)
d.click(26, 236) # At S0, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2.5)
d.click(472, 78) # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2.5)
d.click(75, 425) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/camera
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(853, 78) # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(47, 465) # At S7, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2.5)
d(scrollable=True).swipe.up() # At S9
d.wait.update()
time.sleep(3)
d.click(190, 412) # At S10, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/date_picker_month_and_day
d.wait.update()
time.sleep(2.5)
# Transition from S10(4) to S9(3)
d(scrollable=True).swipe.up() # At S9
d.wait.update()
time.sleep(3)
d.click(190, 1449) # At S11, android.widget.Button, it.feio.android.omninotes.foss:id/done
d.wait.update()
time.sleep(2.5)
d.click(397, 409) # At S12, android.widget.Button, it.feio.android.omninotes.foss:id/hours
d.wait.update()
time.sleep(2.5)
# Self Transition in S12
d.click(397, 409) # At S12, android.widget.Button, it.feio.android.omninotes.foss:id/hours
d.wait.update()
time.sleep(2.5)
# Self Transition in S12
d.click(190, 1352) # At S12, android.widget.Button, it.feio.android.omninotes.foss:id/done_button
d.wait.update()
time.sleep(2.5)
d.click(151, 1254) # At S13, android.widget.Button, it.feio.android.omninotes.foss:id/done
d.wait.update()
time.sleep(2.5)
# Transition from S13(6) to S7(2)
d.click(5, 68) # At S7, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S7(2) to S0(1)
d.click(853, 78) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(2.5)
d.click(498, 330) # At S14, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S14(2) to S0(1)
d.click(5, 68) # At S0, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(870, 1584) # At S15, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2.5)
# Transition from S15(2) to S0(1)
d.click(26, 236) # At S0, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2.5)
# Transition from S0(1) to S7(2)
d.click(44, 236) # At S7, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
# Self Transition in S7
d.long_click(599, 78) # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Self Transition in S7
d.click(5, 68) # At S7, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S7(2) to S0(1)
d.click(870, 1584) # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2.5)
# Transition from S0(1) to S1(2)
d.long_click(726, 78) # At S1, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(3)
# Self Transition in S1
d.click(5, 68) # At S1, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.long_click(870, 1584) # At S16, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(3)
# Transition from S16(3) to S1(2)
d.click(891, 1260) # At S1, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_checklist
d.wait.update()
time.sleep(2.5)
d.long_click(599, 78) # At S17, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(3)
# Self Transition in S17
d.long_click(47, 481) # At S17, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(3)
d.long_click(75, 842) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(3)
# Self Transition in S18
d.click(75, 842) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2.5)
# Self Transition in S18
d.click(794, 941) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2.5)
# Transition from S18(4) to S17(3)
d.click(47, 481) # At S17, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2.5)
#Transition from S17(3) to S9(3), Both nodes same depth
d.click(726, 78) # At S17, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2.5)
# Self Transition in S17
d.click(231, 368) # At S17, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Self Transition in S17
d.long_click(853, 78) # At S17, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(3)
# Self Transition in S17
d.click(5, 68) # At S17, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S17(3) to S0(1)
d.long_click(726, 78) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(3)
# Self Transition in S0
d.long_click(26, 236) # At S0, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(3)
# Self Transition in S0
d.long_click(870, 1584) # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(3)
# Transition from S0(1) to S7(2)
d.click(472, 78) # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2.5)
# Transition from S7(2) to S8(3)
d.click(75, 679) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/files
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.long_click(47, 465) # At S7, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(3)
# Transition from S7(2) to S18(4)
d.click(794, 941) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2.5)
# Transition from S18(4) to S7(2)
d.click(980, 78) # At S7, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
#Transition from S7(2) to S14(2), Both nodes same depth
d.click(63, 368) # At S7, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
d.wait.update()
time.sleep(2.5)
# Self Transition in S7
d.click(980, 78) # At S7, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
#Transition from S7(2) to S14(2), Both nodes same depth
d.long_click(47, 465) # At S7, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(3)
# Self Transition in S7
d.click(980, 78) # At S7, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
#Transition from S7(2) to S14(2), Both nodes same depth
d.click(726, 78) # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2.5)
# Transition from S7(2) to S17(3)
d.click(231, 368) # At S17, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(599, 78) # At S19, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2.5)
d.click(252, 1029) # At S20, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultNegative
d.wait.update()
time.sleep(2.5)
# Transition from S20(5) to S19(4)
d.click(853, 78) # At S19, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(44, 236) # At S19, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
# Self Transition in S19
d.click(472, 78) # At S19, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2.5)
# Transition from S19(4) to S8(3)
d.click(75, 806) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/recording
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 1187) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/timestamp
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 552) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/video
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 1314) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/pushbullet
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 1060) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/location
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
#back() into Unknown State
d.click(696, 991) # At S21, android.widget.Button, com.android.packageinstaller:id/permission_allow_button
d.wait.update()
time.sleep(2.5)
# Transition from S21(4) to S8(3)
d.click(75, 425) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/camera
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(75, 679) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/files
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(75, 1187) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/timestamp
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 1187) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/timestamp
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 1187) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/timestamp
d.wait.update()
time.sleep(2.5)
# Self Transition in S8
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
#back() into Unknown State
d.click(253, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_eraser
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(42, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_stroke
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into state with no package name
d.wait.update()
time.sleep(3)
d.click(42, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_stroke
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into state with no package name
d.wait.update()
time.sleep(3)
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(464, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_undo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(464, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_undo
d.wait.update()
time.sleep(2.5)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.click(253, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_eraser
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(253, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_eraser
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into state with no package name
d.wait.update()
time.sleep(3)
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(253, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_eraser
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into state with no package name
d.wait.update()
time.sleep(3)
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(42, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_stroke
d.wait.update()
time.sleep(2.5)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.click(464, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_undo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(464, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_undo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
d.press.back() #Self Transition Limit Reached
d.wait.update()
time.sleep(3)
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(5, 68) # At S23, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(726, 78) # At S24, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(831, 78) # At S25, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_uncomplete_checklists
d.wait.update()
time.sleep(2.5)
d.long_click(26, 338) # At S26, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(3)
# Self Transition in S26
d.click(26, 338) # At S26, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2.5)
# Transition from S26(8) to S23(5)
d.click(980, 78) # At S23, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(560, 582) # At S27, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(5, 68) # At S28, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(5, 68) # At S29, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S29
d.click(5, 409) # At S29, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S29
d.click(5, 659) # At S29, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(980, 78) # At S30, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(560, 78) # At S31, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S31(10) to S30(9)
d.click(996, 215) # At S30, android.widget.ImageView, it.feio.android.omninotes.foss:id/search_cancel
d.wait.update()
time.sleep(2.5)
d.click(853, 78) # At S32, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(2.5)
# Transition from S32(10) to S14(2)
d.click(498, 204) # At S14, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S14(2) to S32(10)
d.click(26, 236) # At S32, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2.5)
# Transition from S32(10) to S23(5)
d.click(231, 594) # At S23, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(231, 707) # At S33, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S33
d.long_click(472, 78) # At S33, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Self Transition in S33
d.click(231, 481) # At S33, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.long_click(231, 368) # At S34, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(231, 481) # At S35, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S35(8) to S34(7)
d.long_click(231, 594) # At S34, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.long_click(231, 707) # At S36, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.long_click(47, 933) # At S37, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(3)
# Transition from S37(9) to S18(4)
d.click(794, 941) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2.5)
# Transition from S18(4) to S37(9)
d.click(231, 594) # At S37, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(147, 383) # At S38, android.widget.CheckBox, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S38
d.click(44, 236) # At S38, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d(scrollable=True).swipe.down()# At S39
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
# Self Transition in S39
d.click(726, 78) # At S39, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S39(11) to S37(9)
d.click(599, 78) # At S37, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2.5)
# Transition from S37(9) to S20(5)
d.click(75, 861) # At S20, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S20(5) to S37(9)
d.click(231, 820) # At S37, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S37(9) to S39(11)
d.long_click(231, 707) # At S39, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(231, 481) # At S40, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.long_click(231, 368) # At S41, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(231, 820) # At S42, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
d.click(47, 993) # At S43, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
# Self Transition in S43
d.click(980, 78) # At S43, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(560, 330) # At S44, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.long_click(726, 78) # At S45, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(3)
# Self Transition in S45
d.click(726, 78) # At S45, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(980, 78) # At S46, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(560, 330) # At S47, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S47(19) to S18(4)
d.click(794, 941) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2.5)
d.long_click(173, 94) # At S48, android.widget.EditText, it.feio.android.omninotes.foss:id/search_src_text
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Self Transition in S48
d.click(980, 78) # At S48, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S48(5) to S47(19)
d.click(560, 330) # At S47, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S47(19) to S18(4)
d.click(75, 842) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2.5)
# Self Transition in S18
d.click(75, 842) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/content
d.wait.update()
time.sleep(2.5)
# Self Transition in S18
d.click(794, 941) # At S18, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2.5)
# Transition from S18(4) to S48(5)
d.click(173, 94) # At S48, android.widget.EditText, it.feio.android.omninotes.foss:id/search_src_text
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Self Transition in S48
d.click(5, 68) # At S48, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S48(5) to S45(17)
d.long_click(853, 78) # At S45, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(3)
# Self Transition in S45
d.click(5, 68) # At S45, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(853, 78) # At S49, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
d.wait.update()
time.sleep(2.5)
# Transition from S49(18) to S45(17)
d.click(726, 78) # At S45, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.long_click(173, 94) # At S50, android.widget.EditText, it.feio.android.omninotes.foss:id/search_src_text
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
#Transition from S50(18) to S46(18), Both nodes same depth
d.click(385, 874) # At S50, android.widget.TextView, it.feio.android.omninotes.foss:id/empty_list
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
#Transition from S50(18) to S46(18), Both nodes same depth
d.click(726, 78) # At S50, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_uncomplete_checklists
d.wait.update()
time.sleep(2.5)
d.click(173, 94) # At S51, android.widget.EditText, it.feio.android.omninotes.foss:id/search_src_text
d.wait.update()
time.sleep(2.5)
# Self Transition in S51
d.click(26, 338) # At S51, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2.5)
d.click(147, 609) # At S52, android.widget.CheckBox, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S52
d.click(231, 707) # At S52, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(44, 236) # At S53, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(2.5)
d.click(5, 68) # At S54, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S54(22) to S30(9)
d.click(5, 68) # At S30, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(726, 78) # At S55, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
# Self Transition in S55
d.click(980, 78) # At S55, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S55(10) to S30(9)
d.click(726, 78) # At S30, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
d.click(26, 338) # At S56, android.widget.FrameLayout, it.feio.android.omninotes.foss:id/root
d.wait.update()
time.sleep(2.5)
# Transition from S56(10) to S52(20)
d.click(147, 722) # At S52, android.widget.CheckBox, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S52
d.click(231, 481) # At S52, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.click(853, 78) # At S57, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(2.5)
d.press.back() #Transition into invalid 3rd party app
d.wait.update()
time.sleep(3)
d.click(472, 78) # At S57, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2.5)
# Transition from S57(21) to S8(3)
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
# Transition from S8(3) to S22(4)
d.click(676, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_redo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(253, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_eraser
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(464, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_undo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S22(4) to S52(20)
d.click(472, 78) # At S52, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2.5)
# Transition from S52(20) to S8(3)
d.click(75, 933) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/sketch
d.wait.update()
time.sleep(2.5)
# Transition from S8(3) to S22(4)
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(888, 228) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_erase
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S18(4), Both nodes same depth
d.click(464, 226) # At S22, android.widget.ImageView, it.feio.android.omninotes.foss:id/sketch_undo
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.click(5, 68) # At S22, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S22(4) to S52(20)
d.long_click(599, 78) # At S52, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(3)
# Self Transition in S52
d.click(231, 933) # At S52, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
d.long_click(853, 78) # At S58, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(3)
# Self Transition in S58
d.click(959, 893) # At S58, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S58(21) to S37(9)
d.click(147, 496) # At S37, android.widget.CheckBox, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S37
d.click(726, 78) # At S37, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2.5)
# Self Transition in S37
d.click(231, 368) # At S37, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S37(9) to S42(14)
d.long_click(231, 481) # At S42, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S42(14) to S41(13)
d.long_click(44, 236) # At S41, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_title
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S41(13) to S37(9)
d.click(147, 722) # At S37, android.widget.CheckBox, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S37
d.click(472, 78) # At S37, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
d.wait.update()
time.sleep(2.5)
# Transition from S37(9) to S8(3)
d.click(75, 1314) # At S8, android.widget.TextView, it.feio.android.omninotes.foss:id/pushbullet
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S8(3) to S37(9)
d.click(231, 481) # At S37, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S37(9) to S41(13)
d.click(599, 78) # At S41, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2.5)
# Transition from S41(13) to S20(5)
d.click(75, 861) # At S20, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S20(5) to S41(13)
d.click(47, 933) # At S41, android.widget.LinearLayout, it.feio.android.omninotes.foss:id/reminder_layout
d.wait.update()
time.sleep(2.5)
# Self Transition in S41
d.click(231, 368) # At S41, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.long_click(853, 78) # At S59, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
# Self Transition in S59
d(scrollable=True).swipe.down()# At S59
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
# Self Transition in S59
d.long_click(231, 649) # At S59, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S59(14) to S38(10)
d.click(147, 609) # At S38, android.widget.CheckBox, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S38
d.long_click(231, 594) # At S38, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(3)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S38(10) to S41(13)
d.long_click(853, 78) # At S41, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
d.wait.update()
time.sleep(3)
# Self Transition in S41
d.click(726, 78) # At S41, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
d.wait.update()
time.sleep(2.5)
# Self Transition in S41
d.click(231, 820) # At S41, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(231, 649) # At S60, android.widget.EditText, (No resource.id)
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text 987abc') # Enter 987abc into input field
time.sleep(1.5)
subprocess.call('adb shell input keyevent 111') # Close keyboard
time.sleep(1.5)
# Transition from S60(14) to S38(10)
d.click(599, 78) # At S38, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
d.wait.update()
time.sleep(2.5)
# Transition from S38(10) to S20(5)
d.click(654, 1029) # At S20, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
d.wait.update()
time.sleep(2.5)
d.click(466, 919) # At S61, android.widget.ImageView, it.feio.android.omninotes.foss:id/color_chooser
d.wait.update()
time.sleep(2.5)
d.click(295, 775) # At S62, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.long_click(820, 775) # At S63, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(3)
# Self Transition in S63
d.click(820, 775) # At S63, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S63
d.click(295, 943) # At S63, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S63
d.click(470, 943) # At S63, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S63
d.click(470, 775) # At S63, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S63
d.click(645, 775) # At S63, android.widget.FrameLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Self Transition in S63
d.press.home()
# -End Test Case-
#-Number of crashes detected: 0