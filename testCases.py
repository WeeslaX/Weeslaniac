from uiautomator import device as d
import time
import subprocess

# New Test Case
d.click(844, 1340) # At M, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(363, 861) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/empty_list
d.wait.update()
time.sleep(2.5)
# Self Transition in S0
d.click(677, 89) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text aaa123') # Enter aaa123 into input field
time.sleep(1.5)
d.press.back() #Close keyboard
d.wait.update()
time.sleep(3)
#back() into Unknown State
# Self Transition in S1
d.click(5, 77) # At S1, android.widget.ImageButton, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S1(2) to S0(1)
d.click(839, 1535) # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2.5)
d.click(965, 89) # At S2, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(485, 89) # At S3, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S3(3) to S0(1)
d.click(363, 861) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/empty_list
d.wait.update()
time.sleep(2.5)
# Self Transition in S0
d.click(839, 1535) # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
d.wait.update()
time.sleep(2.5)
# Transition from S0(1) to S2(2)
d.click(863, 1349) # At S2, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_note
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text aaa123') # Enter aaa123 into input field
time.sleep(1.5)
d.press.back() #Close keyboard
d.wait.update()
time.sleep(3)
#back() into Unknown State
# Self Transition in S4
d.click(71, 419) # At S4, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
d.wait.update()
time.sleep(2.5)
subprocess.call('adb shell input text aaa123') # Enter aaa123 into input field
time.sleep(1.5)
d.press.back() #Close keyboard
d.wait.update()
time.sleep(3)
# Self Transition in S4
d.click(965, 89) # At S4, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
d.click(485, 377) # At S5, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S5(4) to S0(1)
d.click(363, 861) # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/empty_list
d.wait.update()
time.sleep(2.5)
# Self Transition in S0
d.click(965, 89) # At S0, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S0(1) to S3(3)
d.click(485, 89) # At S3, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2.5)
# Transition from S3(3) to S0(1)
# -End Test Case-
#-Number of crashes detected: 0
