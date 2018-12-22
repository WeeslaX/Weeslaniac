import xml.etree.ElementTree as ET
import networkx as nx
import subprocess
import matplotlib.pyplot as plt
from uiautomator import device as d
import numpy as np
import sys
import time
import hashlib
import random
import os

# User inputs
numberOfInstructions = 500
chanceOfNormalClicks = 54
chanceOfLongClicks = 36
chanceOfScroll = 10
selfTransitionLimit = 6     # Defaults at 6
inputText = '987abc'        # Enhancement: User input list
deviceName = 'emulator-5554'
appName = "'content-desc': 'Omni"   # Insert App Name
ssLocation = "C:/Users/awslw/Desktop/FYP/uiAutomator Dump/Pics/"
tcLocation = "C:/Users/awslw/Desktop/FYP/uiAutomator Dump/"

# Fixed Weights
enterInput = 70
doNotEnterInput = 100 - enterInput
closeKeyboard = 65
doNotCloseKeyboard = 100 - closeKeyboard
defaultWeight = 20

# Data Structures
class MainNode:
    def __init__(self, state):
        global appName
        self.state = generateHashedState(state)
        self.name = "M"
        self.depth = 1
        self.appXCoor = 0
        self.appYCoor = 0
        self.package = ''
        self.views = []
        self.resourceId = []
        self.currentIndex = 0
        # Find clickable XY locations
        found = False
        root = ET.fromstring(state)
        for elem in root.iter():

            strAttrib = str(elem.attrib)
            if appName in strAttrib:
                # Obtain XY Coordinates of clickable coordinates
                start = strAttrib.find("'bounds': '") + 12
                end = strAttrib.find('[', start)
                temp = strAttrib[start:end]
                start = temp.find("[") + 1
                end = temp.find(",", start)
                self.appXCoor = int(temp[start:end])
                start = temp.find(",") + 1
                end = temp.find("]", start)
                self.appYCoor = int(temp[start:end])
                # Obtain view names
                start = strAttrib.find("'class': '") + 10
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                self.views.append(str(temp))
                # Obtain resource-id
                start = strAttrib.find("'resource-id': '") + 16
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                # No resource-id
                if temp == '':
                    temp = '(No resource.id)'
                    self.resourceId.append(temp)
                # Has resource-id
                else:
                    self.resourceId.append(temp)
                found = True
                print("App Found")
                break

        # Index of App
        self.currentIndex = len(self.views)-1

        if found == False:
            print("Target App Not Found")
            f.write("#-Terminate Test (App not Found)-\n")
            f.close()
            sys.exit()

        # Screen shot of State
        d.screenshot(ssLocation + self.name + '.png')  # Screenshot of state

        # Add and Display with matlibplot
        # G.add_node(self.name)
        # pos = nx.spring_layout(G)
        # nx.draw_networkx(G, pos, node_color='g', node_size=1000)
        # plt.axis('off')
        # plt.draw()
        # plt.pause(1)


class Node:
    global prevNode
    global defaultWeight

    def __init__(self, name, state, depth):
        # Node Attributes
        self.name = str(name)
        self.state = generateHashedState(state)
        self.depth = int(depth)
        self.package = ''

        # Click Attributes
        self.views = []
        self.resourceId = []
        self.clickableXCoor = np.array([], dtype=int)
        self.clickableYCoor = np.array([], dtype=int)
        self.noClickableView = False
        self.clickableLength = 0
        self.longClickable = []
        self.hasLongClicks = False
        self.currentIndex = 0

        # Scroll/Swipe Attributes
        self.isScrollable = False
        self.isMultiScrollable = False
        self.canScrollDown = False
        self.canScrollUp = False
        self.scrollableX = []
        self.scrollableY = []

        # Weights
        self.cTransitionWeight = []
        self.lcTransitionWeight = []

        # Conditions
        clickCondition = "'clickable': 'true'"
        enabledCondition = "'enabled': 'true'"
        longClickCondition = "'long-clickable': 'true'"
        scrollCondition = "'scrollable': 'true'"


        # Keeps track of all Long Click view
        longClickIndex = 0

        # Parsing with ET to obtain dump information
        root = ET.fromstring(state)
        for elem in root.iter():
            strAttrib = str(elem.attrib)
            # View is enabled and clickable
            if clickCondition in strAttrib and enabledCondition in strAttrib:
                # Obtain XY Coordinates of clickable and enabled views
                start = strAttrib.find("'bounds': '") + 12
                end = strAttrib.find('[', start)
                temp = strAttrib[start:end]
                start = temp.find("[") + 1
                end = temp.find(",", start)
                xCoordinate = int(temp[start:end])
                self.clickableXCoor = np.append(self.clickableXCoor, xCoordinate)
                start = temp.find(",") + 1
                end = temp.find("]", start)
                yCoordinate = int(temp[start:end])
                self.clickableYCoor = np.append(self.clickableYCoor, yCoordinate)
                # Set clickable weights to default
                self.cTransitionWeight.append(defaultWeight)

                # Obtain package names
                start = strAttrib.find("'package': '") + 12
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                self.package = str(temp)
                # Obtain view names
                start = strAttrib.find("'class': '") + 10
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                self.views.append(str(temp))
                # Obtain resource-id
                start = strAttrib.find("'resource-id': '") + 16
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                # No resource-id
                if temp == '':
                    temp = '(No resource.id)'
                    self.resourceId.append(temp)
                # Has resource-id
                else:
                    self.resourceId.append(temp)
                # View is long-clickable
                if longClickCondition in strAttrib:
                    self.longClickable.append(longClickIndex)
                    # Set long-clickable weights to default
                    self.lcTransitionWeight.append(defaultWeight)
                    # Long clicks Present
                    self.hasLongClicks = True

                longClickIndex = longClickIndex + 1
            # Find scrollable views
            if scrollCondition in strAttrib:
                # Obtain XY Coordinates of scrollable coordinates
                start = strAttrib.find("'bounds': '") + 12
                end = strAttrib.find('[', start)
                temp = strAttrib[start:end]
                start = temp.find("[") + 1
                end = temp.find(",", start)
                xCoordinate = int(temp[start:end])
                self.scrollableX.append(xCoordinate)
                start = temp.find(",") + 1
                end = temp.find("]", start)
                yCoordinate = int(temp[start:end])
                self.scrollableY.append(yCoordinate)

                if len(self.scrollableX) == 1:
                    self.isScrollable = True
                    self.canScrollDown = True
                    self.canScrollUp = True

                if len(self.scrollableX) > 1:
                    self.isMultiScrollable = True

        # Get number of clickable objects
        self.clickableLength = len(self.clickableXCoor)

        # No clickable views
        if self.clickableLength == 0:
            print("No Clickable View")
            # Check if its Main Activity
            if len(stateList) == 0:
                # Screen shot of State
                d.screenshot(ssLocation + self.name + '.png')  # Screenshot of state
                # Terminate Testing
                print("Terminate Testing")
                f.write("# -Terminate Testing (No Clickable View in Main Activity)-\n")
                f.close()
                sys.exit()
            else:
                self.noClickableView = True
                # Screen shot of State
                d.screenshot(ssLocation + self.name + '.png')  # Screenshot of state

                # Add and Display with matlibplot
                # plt.clf()  # Clear previous graph
                # G.add_edges_from([(prevNode.name, self.name)])
                # G.add_edges_from([(self.name, prevNode.name)])
                # pos = nx.spring_layout(G)
                # nx.draw_networkx(G, pos, node_color='g', node_size=1000)
                # plt.axis('off')
                # plt.draw()
                # plt.pause(1)

        # Normal Operation (Have clickable views)
        else:
            # Screen shot of State
            d.screenshot(ssLocation + self.name + '.png')  # Screenshot of state

            # Add and Display with matlibplot
            # plt.clf()  # Clear previous graph
            # G.add_edges_from([(prevNode.name, self.name)])
            # pos = nx.spring_layout(G)
            # nx.draw_networkx(G, pos, node_color='g', node_size=1000)
            # plt.axis('off')
            # plt.draw()
            # plt.pause(1)


# Misc
def generateHashedState(state):
    # Conditions
    clickCondition = "'clickable': 'true'"
    enableCondition = "'enabled': 'true'"
    longClickCondition = "'long-clickable': 'true'"
    scrollCondition = "'scrollable': 'true'"
    # Attributes
    resourceId = ''
    view = ''
    package = ''
    longClickable = ''
    scroll = 'False'
    root = ET.fromstring(state)
    for elem in root.iter():
        strAttrib = str(elem.attrib)
        # Find clickable Views
        if clickCondition in strAttrib and enableCondition in strAttrib:
            # Obtain package names
            start = strAttrib.find("'package': '") + 12
            end = strAttrib.find("'", start)
            temp = strAttrib[start:end]
            package = str(temp)
            # Obtain view names
            start = strAttrib.find("'class': '") + 10
            end = strAttrib.find("'", start)
            temp = strAttrib[start:end]
            view = view+str(temp)
            # Obtain resource-id
            start = strAttrib.find("'resource-id': '") + 16
            end = strAttrib.find("'", start)
            temp = strAttrib[start:end]
            # No resource-id
            if temp == '':
                temp = '(No resource.id)'
                resourceId = resourceId + temp
            # Has resource-id
            else:
                resourceId = resourceId + temp
            # Long clickable
            if longClickCondition in strAttrib:
                longClickable = longClickable + "True"
        # Determine if scrollable
        if scrollCondition in strAttrib:
            scroll = 'True'

    # Return Hash
    return hashlib.md5((package+view+resourceId+longClickable+scroll)).digest().encode("base64")


def setupLogFile():
    global f
    exists = os.path.isfile(tcLocation + "/testCases.py")
    # File already created
    if exists:
        print("Test Case File Exists, adding new test case.")
        # Use existing python test file
        f = open(tcLocation + "/testCases.py", "a")
        f.write("# New Test Case\n")
        f.write("# Target: " + str(numberOfInstructions) + " actions\n")

    # File not created
    else:
        print("File Exists, adding new test case.")
        # Create new Python test file
        f = open(tcLocation + "/testCases.py", "a+")

        # Import List
        f.write("from uiautomator import device as d\n")
        f.write("import time\n")
        f.write("import subprocess\n\n")
        f.write("# New Test Case\n")
        f.write("# Target: " + str(numberOfInstructions) + " actions\n")


def addNode(state):
    global stateCount
    global prevNode
    global stateList
    x = Node('S' + str(stateCount), state, (prevNode.depth + 1))
    stateList.append(x)

    # New state does not have any clickable views
    if stateList[stateCount].noClickableView is True:
        stateCount = stateCount + 1
        print("New node no clickable views")
        back("New node no clickable Views")
        return

    # New State that has clickable views
    prevNode = stateList[stateCount]
    stateCount = stateCount + 1
    print("New node added: " + prevNode.name)
    return


# Emulator Actions
def back(text):
    global prevNode
    global stateCount
    global stateList
    global TransitionCount
    d.press.back()
    d.wait.update()
    time.sleep(3)
    print("d.press.back() - " + str(text))
    f.write("d.press.back() #" + str(text) +"\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(3)\n")
    # Checking state after back()
    backState = d.dump(compressed=True).encode('utf-8')
    backState_h = generateHashedState(backState)

    # back() into Main menu
    if backState_h == m.state:
        print("back() into main menu, Reopening app")
        prevNode = m
        click(m.appXCoor, m.appYCoor)

    # back() to known state
    for i in range(len(stateList)):
        # If back() to known state
        if backState_h == stateList[i].state:
            print("back() into Existing State: " + stateList[i].name)
            prevNode = stateList[i]
            return

    # back() to unknown state, Add new node
    msg = "back() into Unknown State"
    print(msg)
    f.write("#" + msg + "\n")
    addNode(backState)
    return


def click(xCoor, yCoor):
    global prevNode
    d.click((xCoor+5), (yCoor+5))
    time.sleep(2)
    temp = 'd.click(' + str(xCoor+5) + ', ' + str(yCoor+5) + ') # At '
    info = prevNode.name + ', ' + prevNode.views[prevNode.currentIndex] + ', ' + prevNode.resourceId[prevNode.currentIndex]
    print(temp+info)
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2.5)\n")
    d.wait.update()


def long_click(xCoor,yCoor):
    global prevNode
    d.long_click(xCoor+5, yCoor+5)
    time.sleep(1.5)
    temp = 'd.long_click(' + str(xCoor + 5) + ', ' + str(yCoor + 5) + ') # At '
    info = prevNode.name + ', ' + prevNode.views[prevNode.currentIndex] + ', ' + prevNode.resourceId[
        prevNode.currentIndex]
    print(temp + info)
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(3)\n")
    d.wait.update()


def scroll_up():
    global prevNode
    d(scrollable=True).swipe.down()
    d.wait.update()
    time.sleep(1.5)
    temp = "d(scrollable=True).swipe.down()# At " + prevNode.name
    print(temp)
    f.write(temp + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(3)\n")


def scroll_down():
    global prevNode
    d(scrollable=True).swipe.up()
    d.wait.update()
    time.sleep(1.5)
    temp = "d(scrollable=True).swipe.up() # At " + prevNode.name
    print(temp)
    f.write(temp + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(3)\n")


# Logic Checks
def checkInputWeights():
    # Check weight of operations:
    total = chanceOfLongClicks+chanceOfNormalClicks+chanceOfScroll

    # Correct Weights
    if total == 100:
        print("Input Weights Ok")
        return

    elif total <100:
        print("Input Weights below 100%, Terminating Program")
        sys.exit()
    else:
        print("Input Weights above 100%, Terminating Program")
        sys.exit()


def checkEmulator():
    global deviceName
    cmd = 'adb devices'
    s = subprocess.check_output(cmd)

    if deviceName in s:
        print("Target Device Detected")
        return

    print("Target device not connected, Abort Testing")
    sys.exit()


def checkKeyboard():
    global inputText
    global enterInput
    global doNotEnterInput
    global closeKeyboard
    global doNotCloseKeyboard
    keyboardCondition = "mInputShown=true"

    cmd = 'adb shell dumpsys input_method | grep mInputShown'
    s = subprocess.check_output(cmd)

    # Soft keyboard found
    if keyboardCondition in s:
        # Decision to enter input
        decisionEnter = random.choice([0] * enterInput + [1] * doNotEnterInput)

        # Enter inputText into input field
        if decisionEnter == 0:
            cmd = "adb shell input text " + inputText
            subprocess.call(cmd)
            print("Enter " + inputText + " into input field")
            f.write("subprocess.call(" + "'" + cmd + "'" + ") # Enter " + inputText + " into input field\n")
            f.write("time.sleep(1.5)\n")

        # Check state after entering input
        keyState = d.dump(compressed=True).encode('utf-8')
        keyState_h = generateHashedState(keyState)

        # If current state = known state
        for i in range(len(stateList)):
            #In known state
            if keyState_h == stateList[i].state:
                # Decision to close keyboard
                decisionClose = random.choice([0] * closeKeyboard + [1] * doNotCloseKeyboard)

                # Close Keyboard
                if decisionClose == 0:
                    back("Close keyboard")

                print("Did not close keyboard")
                return

        # If current state = unknown state, Add new node
        msg = "Unknown state when Soft Keyboard Appears."
        print(msg)
        f.write("#" + msg + "\n")
        addNode(keyState)
        return
    # Soft keyboard not found
    return


def checkSelfTransLimit():
    global selfTransitionCount
    global selfTransitionLimit

    # If limit reached
    if selfTransitionCount >= selfTransitionLimit:
        back("Self Transition Limit Reached")
        # Reset Count
        selfTransitionCount = 0
    return


def checkCurrentPackage(state):
    global invalidStateList
    # Normal Operation (Return 1st clickable view's package)
    clickCondition = "'clickable': 'true'"
    root = ET.fromstring(state)
    for elem in root.iter():
        strAttrib = str(elem.attrib)
        if clickCondition in strAttrib:
            # Obtain package names
            start = strAttrib.find("'package': '") + 12
            end = strAttrib.find("'", start)
            return str(strAttrib[start:end])

    # No clickable Views
    invalid = hashlib.md5(state).digest().encode("base64")
    # Invalid state exists
    for i in invalidStateList:
        if invalid == i:
            return ''

    # New invalid state
    invalidStateList.append(invalid)
    d.screenshot(ssLocation + "Invalid State " + str(len(invalidStateList)+1) + '.png')
    return ''


def checkNode():
    global stateList
    global prevNode
    global stateCount
    global selfTransitionCount
    global crashNum

    stateExist = False
    index = 0

    # Get current State
    currentState = d.dump(compressed=True).encode('utf-8')
    currentState_h = generateHashedState(currentState)

    # Check current state package
    temp = checkCurrentPackage(currentState)

    # Check current state with approved list
    if temp != m.package:
        # Current state package is empty
        if temp == '':
            back("Transition into state with no package name")
            return

        # Current state package belongs to 3rd party
        back("Transition into invalid 3rd party app")
        return

    # Check if state exists
    for i in range(len(stateList)):
        if currentState_h == stateList[i].state:
            stateExist = True
            break

        index = index + 1

    # Transition to new state
    if stateExist is False:
        addNode(currentState)
        return
    # Transition to existing state
    else:
        # Transition to main menu, possible Crash
        if currentState_h == m.state:
            # Update number of possible crash
            crashNum = crashNum + 1
            temp = "-Possible Crash Occurred-"
            print(temp)
            f.write("# " + temp + "\n")
            click(m.appXCoor, m.appYCoor)
            f.write("# New Test Case \n")

            # Get state after opening app
            y = d.dump(compressed=True).encode('utf-8')
            y_h = generateHashedState(y)

            # If Main Activity after opening app
            if stateList[0].state == y_h:
                prevNode = stateList[0]
                print("Returned to S0 after possible crash")
                return
            else:
                # If existing state after opening app
                for n in stateList:
                    if n.state == y_h:
                        prevNode = n
                        print("Returned to " + n.name + " after possible crash")
                        return

                # If new state after opening app
                addNode(y)  # New node will be represented as prevNode
                print("Returned to new state after possible crash")
                return

        # Self Transition
        elif currentState_h == prevNode.state:
            # Add self transition count
            selfTransitionCount = selfTransitionCount + 1
            temp = "Self Transition in " + prevNode.name
            print(temp)
            f.write("# " + temp + "\n")
            return

        # Transition to known state
        else:
            # Transition from Child state to parent state
            if stateList[index].depth < prevNode.depth:
                # Reset Self Transition Count
                selfTransitionCount = 0
                temp = "Transition from " + prevNode.name + "(" + str(prevNode.depth) + ") to " + stateList[
                    i].name + "(" + str(stateList[i].depth) + ")"
                print(temp)
                f.write("# " + temp + "\n")
                prevNode = stateList[index]
                return

            # Transition from parent state to child state
            if stateList[index].depth > prevNode.depth:
                # Reset Self Transition Count
                selfTransitionCount = 0
                temp = "Transition from " + prevNode.name + "(" + str(prevNode.depth) + ") to " + stateList[
                    i].name + "(" + str(stateList[i].depth) + ")"
                print(temp)
                f.write("# " + temp + "\n")
                prevNode = stateList[index]
                return

            # Transition between states with same depth
            # Add self transition count
            selfTransitionCount = selfTransitionCount + 1
            temp = "Transition from " + prevNode.name + "(" + str(prevNode.depth) + ") to " + stateList[
                i].name + "(" + str(stateList[i].depth) + "), Both nodes same depth"
            print(temp)
            f.write("#" + temp + "\n")
            return


def currentIndexDecision(decision):
    global prevNode
    # Decision Point
    # Index logic point for Long Click
    if decision == 'long-click':
        index = random.randint(0, len(prevNode.longClickable)-1)
        return prevNode.longClickable[index]

    # Index logic point for Normal Click
    if decision == 'click':
        return random.randint(0, prevNode.clickableLength-1)


def operationDecision():
    global prevNode
    # Decision Point (Weighted Random Algorithm)
    choice = random.choice([0] * chanceOfLongClicks + [1] * chanceOfScroll + [2] * chanceOfNormalClicks)

    # Long Click Selected
    if choice == 0:
        # State has no long clicks
        if prevNode.hasLongClicks is False:
            # Re-randomise
            temp = chanceOfLongClicks / 2
            choice = random.choice([1] * (chanceOfScroll + temp) + [2] * (chanceOfNormalClicks + temp))

        # State has long clicks
        else:
            # Index decision
            prevNode.currentIndex = currentIndexDecision('long-click')

            # Long Click Operation
            long_click(prevNode.clickableXCoor[prevNode.currentIndex], prevNode.clickableYCoor[prevNode.currentIndex])
            return

    # Scroll Selected
    if choice == 1:
        # State cannot be scrolled
        if prevNode.isScrollable is False:
            choice = 2  # Default to normal click

        # State can be scrolled
        else:
            # State can scroll up and down
            if prevNode.canScrollDown is True and prevNode.canScrollUp is True:
                # Direction Decision Point
                scrollDecision = random.randint(0, 1)

                # Scroll up decided
                if scrollDecision == 0:
                    scroll_up()
                    # Check current state
                    temp = generateHashedState(d.dump(compressed=True).encode('utf-8'))
                    # Cannot scroll up (Self Transition)
                    if prevNode.state == temp:
                        prevNode.canScrollUp = False
                    return

                # Scroll down decided
                else:
                    scroll_down()
                    # Check current state
                    temp = generateHashedState(d.dump(compressed=True).encode('utf-8'))
                    # Cannot scroll down (Self Transition)
                    if prevNode.state == temp:
                        prevNode.canScrollDown = False
                    return

            # State can only scroll down
            elif prevNode.canScrollDown is True and prevNode.canScrollUp is False:
                scroll_down()
                return

            # State can only scroll up
            elif prevNode.canScrollUp is True and prevNode.canScrollDown is False:
                scroll_up()
                return


    # Normal Click Selected
    if choice == 2:
        # Index decision
        prevNode.currentIndex = currentIndexDecision('click')

        # Normal Click Operation
        click(prevNode.clickableXCoor[prevNode.currentIndex], prevNode.clickableYCoor[prevNode.currentIndex])
        return


# Start of Testing Program
checkEmulator()
checkInputWeights()
setupLogFile()

# Initialization
G = nx.MultiDiGraph()   # Create Visual Graph
stateCount = 0          # Keeps track of number of States
stateList = []          # Keeps track of states
invalidStateList = []   # Keeps track of invalid states (No clickable views)
crashNum = 0
selfTransitionCount = 0

# Setup Main Menu
m = MainNode(d.dump(compressed=True).encode('utf-8'))
prevNode = m
click(prevNode.appXCoor, prevNode.appYCoor)


# Setup App's Main Activity
temp = Node('S'+str(stateCount), d.dump(compressed=True).encode('utf-8'), 1)
stateList.append(temp)
m.package = stateList[0].package     # Use Main Activity's package name
prevNode = stateList[stateCount]
stateCount = stateCount + 1
checkKeyboard()

# Random Algorithm
instCount = 0

# Loop till every clickable view in main activity is selected
while instCount < numberOfInstructions:
    # Random Algorithm
    operationDecision()

    # Pre-Checks
    checkKeyboard()
    checkSelfTransLimit()

    # Transition Checks
    checkNode()

    # Instruction Counter
    instCount = instCount + 1

# Exiting from Test
d.press.home()
d.wait.update()
print("End Test Case, Number of crashes detected: " + str(crashNum))
print("Total Actions: " + str(numberOfInstructions))
f.write("d.press.home()\n")
f.write("# -End Test Case-\n")
f.write("#-Number of crashes detected: " + str(crashNum) + "\n")
f.close()
