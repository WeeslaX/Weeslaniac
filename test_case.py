from uiautomator import device as d
import time
import subprocess


# New Test Case
# Target App: Omni
# Number of actions: 30
def test():
    d.click(497, 1833)
    # At M, android.widget.TextView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1387, 136)
    # At S0, android.widget.ImageView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(1172, 136)
    # At S1, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S1(2) to S0(1)
    d.click(73, 136)
    # At S0, android.widget.ImageButton, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.long_click(1322, 2442)
    # At S2, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
    d.wait.update()
    time.sleep(1.5)
    # Transition from S2(2) to S0(1)
    d.click(720, 1385)
    # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/empty_list
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S0
    d.long_click(1144, 136)
    # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S0
    d.click(1271, 136)
    # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
    d.wait.update()
    time.sleep(1.5)
    d.click(1146, 514)
    # At S3, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S3(2) to S0(1)
    d.long_click(1271, 136)
    # At S0, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S0
    d.click(1322, 2442)
    # At S0, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_expand_menu_button
    d.wait.update()
    time.sleep(1.5)
    d.long_click(1271, 136)
    # At S4, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_sort
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S4
    d.click(1144, 136)
    # At S4, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_search
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    subprocess.call('adb shell input text 98ab')
    # Enter 98ab into input field
    time.sleep(1.5)
    # back() into Unknown State
    d.click(720, 1385)
    # At S5, android.widget.TextView, it.feio.android.omninotes.foss:id/empty_list
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S5
    d.click(1322, 2259)
    # At S5, android.widget.ImageButton, it.feio.android.omninotes.foss:id/fab_note
    d.wait.update()
    time.sleep(1.5)
    d.click(728, 392)
    # At S6, android.widget.EditText, it.feio.android.omninotes.foss:id/detail_content
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    subprocess.call('adb shell input text 98ab')
    # Enter 98ab into input field
    time.sleep(1.5)
    # back() into Unknown State
    d.click(1144, 136)
    # At S7, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_tag
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S7
    d.click(1387, 136)
    # At S7, android.widget.ImageView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    # Transition from S7(5) to S3(2)
    d.click(1146, 136)
    # At S3, android.widget.LinearLayout, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.click(770, 419)
    # At S8, android.widget.EditText, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    subprocess.call('adb shell input text 98ab')
    # Enter 98ab into input field
    time.sleep(1.5)
    # back() into Unknown State
    d.click(1017, 136)
    # At S9, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_category
    d.wait.update()
    time.sleep(1.5)
    d.click(1058, 1407)
    # At S10, android.widget.TextView, it.feio.android.omninotes.foss:id/buttonDefaultPositive
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    # back() into Unknown State
    d.long_click(720, 1188)
    # At S11, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    subprocess.call('adb shell input text 98ab')
    # Enter 98ab into input field
    time.sleep(1.5)
    # back() into Unknown State
    d.long_click(720, 1188)
    # At S12, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.long_click(720, 1188)
    # At S12, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 1188)
    # At S12, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(720, 1188)
    # At S12, android.widget.EditText, it.feio.android.omninotes.foss:id/category_title
    d.wait.update()
    time.sleep(1.5)
    d.press.back()
    # Close Keyboard
    d.wait.update()
    time.sleep(2.0)
    d.click(959, 1571)
    # At S12, android.widget.Button, it.feio.android.omninotes.foss:id/save
    d.wait.update()
    time.sleep(1.5)
    # Transition from S12(7) to S9(4)
    d.long_click(1271, 136)
    # At S9, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_share
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.long_click(890, 136)
    # At S9, android.widget.TextView, it.feio.android.omninotes.foss:id/menu_attachment
    d.wait.update()
    time.sleep(1.5)
    # Self Transition in S9
    d.click(1356, 423)
    # At S9, android.widget.ImageView, (No resource.id)
    d.wait.update()
    time.sleep(1.5)
    subprocess.call('adb shell pm clear it.feio.android.omninotes.foss')
    time.sleep(1.5)


if __name__ == '__main__':
    test()
    # -End Test Case-
    # -Number of crashes detected: 0
    # Elapsed Time: 00:02:34
