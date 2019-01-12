
# Made by: Aaron
# Name: Mutator
# Description: Mutate Culebra test cases to detect problems in apps
#              Work in progress, prototype with limited functionality

import xml.etree.ElementTree as ET
import networkx as nx
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
testCasePath = 'C:/Users/awslw/Desktop/FYP/AndroidViewClient-master/tools'
testCaseName = 'myTestCase'


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
                print("Click in " + self.name)
                time.sleep(2)
                return

            # For type: resource id
            if self.identificationType == 'resource-id':
                d(resourceId=self.identification).click()
                d.wait.update()
                print("Click in " + self.name)
                time.sleep(2)
                return

        # Selection Type: Input Text
        if self.selectionType == 'inputText':

            # For type: Text
            if self.identificationType == 'text':
                # Click on view
                d(text=self.identification).click()
                d.wait.update()
                print("Click in " + self.name)
                time.sleep(2)
                # Enter user defined text
                cmd = "adb shell input text " + self.text
                subprocess.call(cmd)
                print("Entered: " + self.text + "in " + self.name)
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


# Initialization
instList = np.array([])
nodeList = []

# Import test case script
sys.path.append(testCasePath)
tc = __import__(testCaseName, globals(), locals(), [])

# Obtain target test case in string
targetClass = tc.CulebraTests
targetTestCase = getsource(targetClass.testSomething)

# Separate instructions into a list
getInstructions(targetTestCase)
print(instList)

# Add each instruction as a new object
for i in range(len(instList)):
    newNode = UserNode(instList[i], i)
    nodeList.append(newNode)

# Test
for i in range(6):
    nodeList[i].action()

# Force Close App
cmd = "adb shell am force-stop it.feio.android.omninotes.foss"
subprocess.call(cmd)
