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

# To be added to GUI

# Static values
rotationDelay = 1.5

class Main:

    def __init__(self, inst):
        self.inst = inst
        self.name = "Action #0"

    def action(self):
        # Action
        exec self.inst
        print(self.name + " : " + self.inst)
        # Delay
        d.wait.update()
        time.sleep(1.5)


class TestNode:
    def __init__(self, inst, name):
        # Atributes
        self.inst = ''
        self.name = 'Action #' + str(name)

        # Determine type of action: Click
        if inst.find("d.click(") >= 0:
            start = inst.find("d.click(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        # Determine type of action: Back
        elif inst.find("d.press.back(") >= 0:
            start = inst.find("d.press.back(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        # Determine type of action: L-Click
        elif inst.find("d.long_click(") >= 0:
            start = inst.find("d.long_click(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        # Determine type of action: Swipe
        elif inst.find("d.swipe(") >= 0:
            start = inst.find("d.swipe(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        # Determine type of action: subprocess.call
        elif inst.find("subprocess.call(") >= 0:
            start = inst.find("subprocess.call(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        # Determine type of action: error message
        elif inst.find("d(") >= 0:
            start = inst.find("d(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        # Determine type of action: home button
        elif inst.find("d.press.home(") >= 0:
            start = inst.find("d.press.home(")
            end = inst.find("\n", start)
            self.inst = inst[start:end]

        else:
            print("Cannot form instruction with: " + inst)
            print("Terminating Program")
            sys.exit()

    def action(self):
        # uiAutomator operations
        if self.inst.find('d') >= 0:
            exec self.inst
            print(self.name + " : " + self.inst)
            d.wait.update()
            time.sleep(2)
            return
        # adb operations
        elif self.inst.find('s') >= 0:
            exec self.inst
            print(self.name + " : " + self.inst)
            time.sleep(1.5)
            return


# Mutation types
def rotation():
    print("Rotation Test Started")
    print("Rotate R-N")
    d.orientation = 'r'
    d.wait.update()
    time.sleep(rotationDelay)
    d.orientation = 'n'
    d.wait.update()
    time.sleep(rotationDelay)
    print("Rotate L-N")
    d.orientation = 'l'
    d.wait.update()
    time.sleep(rotationDelay)
    d.orientation = 'n'
    d.wait.update()
    time.sleep(rotationDelay)
    print("Rotate R-L-R-N")
    d.orientation = 'r'
    d.wait.update()
    time.sleep(rotationDelay)
    d.orientation = 'l'
    d.wait.update()
    time.sleep(rotationDelay)
    d.orientation = 'r'
    d.wait.update()
    time.sleep(rotationDelay)
    d.orientation = 'n'
    d.wait.update()
    time.sleep(rotationDelay)


# GUI Interface

def save(entries, checkboxes):
    global gui
    global testCasePath
    global testCaseName
    global startMutation
    global enableMutation

    # Test Case path
    testCasePath = str(entries[0].get())

    # Test Case name
    testCaseName = str(entries[1].get())

    # Start Mutation
    startMutation = int(entries[2].get())
    # Negative startMutation
    if startMutation < 0:
        startMutation = 0

    # Enable Mutation
    temp = str(checkboxes[0].get())
    if temp == '0':
        enableMutation = False
    else:
        enableMutation = True

    showinfo("Success", "Settings Saved.")
    gui.quit()


def setupGUI():
    global gui

    # Preset Values
    label = ['Test Case Path: ', 'Test Case name: ', 'Start Mutation: \n(0 - After Action #0)']
    default = ['C:/Users/awslw/Desktop/FYP/uiAutomator Dump', 'testCases', 0]
    checkboxLabel = ['Enable Mutation']

    # Widget Storage
    entries = []        # Act as a container and keeps track of values stored in textbox
    checkbox = []       # Container for all checkboxes
    vars = []           # Keeps track of integer values of checkboxes (0 - False, 1 - True)

    # Gui Settings
    gui.title("mutator_W Setup")
    gui["bg"] = 'black'

    # Automate Multiple Labels
    index = 0
    for i in label:
        Label(text=i, fg='white', bg='black').grid(row=index, column=0, sticky=W, pady=5)
        index = index + 1

    # Automate Preset Entry fields
    index = 0
    for i in default:
        entries.append(Entry(gui, width=50))
        entries[index].insert(0, str(i))
        entries[index].grid(row=index, column=1, sticky=W, pady=5)
        Label(gui, text=' ', bg='black').grid(row=index, column=2, sticky=W, pady=1)
        index = index + 1

    # Automate checkboxes
    cIndex = 0
    for i in checkboxLabel:
        var = IntVar()
        checkbox.append(Checkbutton(gui, text=i, bg='black', fg='forest green', variable=var))
        checkbox[cIndex].grid(row=index, column=1, sticky=W, pady=5)
        checkbox[cIndex]
        cIndex += 1
        index += 1
        vars.append(var)

    # Save button
    Button(gui, text="Save", command=(lambda v=vars, e=entries: save(e, v)), width=10, relief="groove")\
        .grid(row=index + 1, column=1, pady=4, sticky=W)
    gui.mainloop()
    gui.destroy()


# Obtain instructions from string
def getInstructions(test):
    global instList
    shortenTest = test
    # Obtain 1st instruction separately [Click App]
    start = shortenTest.find("d.click")
    end = shortenTest.find("\n", start)
    # Add First instruction
    instList = np.append(instList, shortenTest[start:end])

    # Reduce list to exclude previous instruction
    shortenTest = shortenTest[end + 1:len(shortenTest)]

    # Obtain all instructions within test case
    while 1:
        # Append instruction (and update) and info text
        start = shortenTest.find("time.sleep(") + 16
        end = shortenTest.find("time.sleep(", start) - 1

        if end < 0:
            break

        instList = np.append(instList, shortenTest[start:end])
        shortenTest = shortenTest[end + 1:len(shortenTest)]

    return


# List of mutations
def mutationDecision():
    rotation()


# List of all possible test types
def operationList():
    global enableMutation

    # Full Test without mutation
    if enableMutation is False:
        print("Commencing Full Test without Mutation")
        for i in range(len(nodeList)):
            nodeList[i].action()

    # Full Test with mutation
    elif enableMutation is True:
        print("Commencing Test with Mutation after Action #" + str(startMutation))
        for i in range(len(nodeList)):
            nodeList[i].action()
            if i >= enableMutation:
                mutationDecision()

    # Invalid option
    else:
        print("Invalid test Selected, Terminating test")
        sys.exit()


# User defined Variables
testCasePath = ''
testCaseName = ''
enableMutation = True
startMutation = 0

# Override (GUI)
try:
    gui = Tk()
    setupGUI()
except:
    print("Settings not set. Testing Aborted.")
    sys.exit()

# Check test case locaton
tcLocation = testCasePath + "/" + testCaseName +".py"
tcExists = os.path.isfile(tcLocation)
if tcExists is False:
    print('Test Case File not found. Terminating Test')
    sys.exit()

# Check validity of test case
f = open(tcLocation, "r")
firstLine = f.read()
if firstLine.find('uiautomator import device as d') < 0:
    print("Invalid File. Terminating Test")
    f.close()
    sys.exit()
else:
    f.close()

#  Initialization
instList = np.array([])
nodeList = []

# Import test case script
sys.path.append(testCasePath)
tc = __import__(testCaseName, globals(), locals(), [])

# Obtain target test string
targetTestCase = getsource(tc.test)

# Separate instructions to be appended to a list
getInstructions(targetTestCase)

# Create main node and add to nodeList (Main Menu)
m = Main(instList[0])
nodeList.append(m)

# Create and add all subsequent nodes to nodeList
for i in range(1, len(instList)):
    newNode = TestNode(instList[i], i)
    nodeList.append(newNode)

# Ensure orientation is natural by default
if d.orientation == 'left' or d.orientation == 'right':
    d.orientation = 'n'
    time.sleep(1)

# Benchmark
sTime = time.time()

# Operation Selection
operationList()

# Obtain elapsed time
eTime = time.time() - sTime
print("Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(eTime))))
