from uiautomator import device as d
import time
import subprocess

d.click(264, 1833) # At M, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2)
d.long_click(720, 397) # At S0, android.widget.RelativeLayout, (No resource.id)
d.wait.update()
time.sleep(2)
#Transition from S1(2) to S1(2)
d.long_click(1387, 136) # At S1, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S1
d.swipe(720, 1385, 5, 1385, steps=10)
# Swipe Left At S1, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
d.long_click(1387, 136) # At S21, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S21
d.swipe(720, 1385, 5, 1385, steps=10)
# Swipe Left At S21, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
d.long_click(760, 356) # At S22, android.widget.Spinner, de.koelle.christian.trickytripper:id/reportViewBaseSpinner
d.wait.update()
time.sleep(2)
d.click(697, 545) # At S23, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2)
#Transition from S22(4) to S22(4)
d.swipe(760, 356, 1393, 356, steps=10)
# Swipe Right At S22, android.widget.Spinner, de.koelle.christian.trickytripper:id/reportViewBaseSpinner
d.wait.update()
time.sleep(2.5)
#Transition from S21(3) to S21(3)
d.swipe(720, 1385, 1435, 1385, steps=10)
# Swipe Right At S21, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
#Transition from S1(2) to S1(2)
d.swipe(720, 1385, 1435, 1385, steps=10)
# Swipe Right At S1, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
# Self Transition in S1
d.swipe(720, 1385, 5, 1385, steps=10)
# Swipe Left At S1, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
#Transition from S21(3) to S21(3)
d.swipe(720, 1385, 5, 1385, steps=10)
# Swipe Left At S21, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
#Transition from S22(4) to S22(4)
d.swipe(720, 1385, 720, 2555, steps=10)
# Scroll up At S22, android.support.v4.view.ViewPager, de.koelle.christian.trickytripper:id/drawer_content_pager
d.wait.update()
time.sleep(2.5)
# Self Transition in S22
d.long_click(1387, 136) # At S22, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
# Self Transition in S22
d.click(1387, 136) # At S22, android.widget.ImageView, (No resource.id)
d.wait.update()
time.sleep(2)
d.click(1172, 514) # At S24, android.widget.LinearLayout, (No resource.id)
d.wait.update()
time.sleep(2)
d.press.back() # Possible Crash Detected
d.wait.update()
time.sleep(3)
d.click(720, 1379) # At S25, android.widget.Button, android:id/aerr_restart
d.wait.update()
time.sleep(2)
# -Possible Crash Occurred-
d.click(264, 1833) # At M, android.widget.TextView, (No resource.id)
d.wait.update()
time.sleep(2)