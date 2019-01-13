
# Made by: Aaron
# Name: Mutator
# Description: Mutate Culebra test cases to detect problems in apps
#              [Work in progress, currently a prototype with limited functionality]

import xml.etree.ElementTree as ET
import subprocess
from uiautomator import device as d
import sys
import numpy as np
import time
import hashlib
import random
import os
from Tkinter import *
from tkMessageBox import *
from dill.source import getsource

# User defined inputs
ssLocation = "C:/Users/awslw/Desktop/FYP/uiAutomator Dump/Pics/"
testCasePath = 'C:/Users/awslw/Desktop/FYP/AndroidViewClient-master/tools'
testCaseName = 'myTestCase'
package = 'it.feio.android.omninotes.foss'
enableMutations = True


class UserNode:
    def __init__(self, inst, count):
        self.name = "S" + str(count)
        self.identification = ''
        self.identificationType = ''
        self.selectionType = ''
        self.text = ''

        # Check selection Type (Eg: Click, Long Click, etc)
        [self.selectionType, self.text] = checkSelection(inst)

        # Check identification Type (Eg: content desc, resource-id, text, etc)
        [self.identificationType, self.identification] = checkIdentification(inst)

    # Converts Culebra's operations to uiAutomator (Work in progress)
    def action(self):
        # Selection Type: Click
        if self.selectionType == 'click':
            # For type: content desc
            if self.identificationType == 'content desc':
                d(description=self.identification).click()
                d.wait.update()
                temp = "Clicked on view with content desc: " + self.identification + " in " + self.name
                print(temp)
                time.sleep(2)
                return

            # For type: resource id
            if self.identificationType == 'resource-id':
                d(resourceId=self.identification).click()
                d.wait.update()
                temp = "Click on view with resource-id: " + self.identification + " in " + self.name
                print(temp)
                time.sleep(2)
                return

        # Selection Type: Input Text
        if self.selectionType == 'inputText':

            # For type: Text
            if self.identificationType == 'text':
                # Click on view
                d(text=self.identification).click()
                d.wait.update()
                temp = "Click on textbox with text: " + self.identification + " in " + self.name
                print(temp)
                time.sleep(2)
                # Enter user defined text
                cmd = "adb shell input text " + self.text
                subprocess.call(cmd)
                print("Entered: " + self.text + " in " + self.name)
                # Close keyboard
                d.press.back()
                d.wait.update()
                print("Close keyboard")
                time.sleep(2)


# (Work in progress to add all possible Culebra operations)
def checkSelection(inst):
    # If click
    if inst.find(".touch()") > 0:
        return 'click', ''

    # If input text
    if inst.find(".setText(") > 0:
        # Obtain input text
        start = inst.find(".setText(") + 11
        end = inst.find('"', start)
        return 'inputText', inst[start:end]


# (Work in progress to add all possible detection types)
def checkIdentification(inst):

    # Content Desc
    if inst.find("findViewWithContentDescriptionOrRaise(") > 0:
        start = inst.find("findViewWithContentDescriptionOrRaise") + 42
        end = inst.find("'", start)
        return 'content desc', inst[start:end]

    # Resource-Id
    if inst.find("findViewById") > 0:
        start = inst.find("findViewById") + 21
        end = inst.find('"', start)
        return 'resource-id', inst[start:end]

    # Text
    if inst.find("findViewWithText") > 0:
        start = inst.find("findViewWithText") + 26
        end = inst.find("'", start)
        return 'text', inst[start:end]


# (Work in progress to add more functionaility and mutation types)
def mutationSelect():
    mutationDecision = random.randint(0, 1)

    # Mutation: Select Home button
    if mutationDecision == 0:
        d.press.home()
        d.wait.update()
        print("Mutation: Home button selected.")
        time.sleep(1.5)

    # Mutation: Change orientation
    if mutationDecision == 1:
        # If orientation: Left
        if str(d.orientation) == 'left':
            # Change orientation to right
            d.orientation = 'r'
            d.wait.update()
            print("Changed orientation to right")
            time.sleep(2)

        # If orientation: Right
        elif str(d.orientation) == 'right':
            # Change orientation to natural
            d.orientation = 'n'
            d.wait.update()
            print("Changed orientation to natural")
            time.sleep(2)

        # If orientation: Natural
        else:
            # Change orientation to left
            d.orientation = 'l'
            d.wait.update()
            print("Changed orientation to left")
            time.sleep(2)


def getInstructions(test):
    global instList
    shortenTest = test
    # Obtain all instructions within test case
    while 1:
        # Append only instruction
        start = shortenTest.find("self.vc.dump(window=-1)") + 32
        end = shortenTest.find("self.vc.sleep(_s)") - 9

        if end < 0:
            break

        instList = np.append(instList, shortenTest[start:end])
        shortenTest = shortenTest[end+26:len(shortenTest)]

    return


#  Initialization
instList = np.array([])
nodeList = []

# (Temporary) User inputs
ip = int(input("Enable mutatation? (0: No, 1: Yes): "))

if ip == 0:
    enableMutations = False
else:
    enableMutations = True

# Import test case script
sys.path.append(testCasePath)
tc = __import__(testCaseName, globals(), locals(), [])

# Obtain target test case in string
targetClass = tc.CulebraTests
targetTestCase = getsource(targetClass.testSomething)

# Separate instructions into a list
getInstructions(targetTestCase)

# Add each instruction as a new object
for i in range(len(instList)):
    newNode = UserNode(instList[i], i)
    nodeList.append(newNode)

# Normal User defined test case
if enableMutations is False:
    print("Start Normal Testing")
    # Normal Test
    for i in range(len(nodeList)):
        # Normal Operation
        nodeList[i].action()

    # Force Close App (Reset to S0)
    cmd = "adb shell am force-stop " + package
    subprocess.call(cmd)
    time.sleep(1)
    # Check orientation
    if str(d.orientation) == 'left' or str(d.orientation) == 'right':
        d.orientation = 'n'
        d.wait.update()
        time.sleep(1)
    print("Testing Done")

# Mutation enabled [Work in progress: Add more functionailities]
else:
    print("Start Mutation-based Testing")
    # Refers to number of normal actions to be taken [Open app]
    actions = 1

    while actions < len(nodeList) + 1:

        # Normal user defined operation
        for i in range(actions):
            nodeList[i].action()

        # Mutation [Work in Progress, for now do only one type of mutation]
        mutationSelect()

        # Force close app
        cmd = "adb shell am force-stop " + package
        subprocess.call(cmd)
        time.sleep(1)

        # Keyboard detection
        keyboardCondition = "mInputShown=true"
        cmd = 'adb shell dumpsys input_method | grep mInputShown'
        s = subprocess.check_output(cmd)
        # Keyboard detected
        if keyboardCondition in s:
            d.press.back()
            d.wait.update()
            time.sleep(1.5)
            print("Keyboard closed")

        # Check orientation
        if d.orientation == 'l' or d.orientation == 'r':
            d.orientation = 'n'
            time.sleep(1)

        actions += 1

    print("Testing Done")
