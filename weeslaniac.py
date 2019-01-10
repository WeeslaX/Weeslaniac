#####################################################################################################################
# Made by:      Aaron                                                                                               #
# Name:         Weeslaniac Android app fuzzing tool                                                                 #
# Desciption:   A pure python android fuzzing tool that detects crashes.                                            #
#####################################################################################################################

import xml.etree.ElementTree as ET
import networkx as nx
import subprocess
from uiautomator import device as d
import numpy as np
import sys
import time
import hashlib
import random
import os
from Tkinter import *
from tkMessageBox import *


# Possible User inputs
definedInvalidState = [""]    # .encode("base64") adds \n to the back 0RgeA6iQVV5U2UkI+0r1GA==\n
selfTransitionLimit = 6
inputText = '987abc'        # Enhancement: User input list
scrollSteps = 10

# Operation Weights
chanceOfNormalClicks = 1
chanceOfLongClicks = 1
chanceOfScroll = 1
chanceOfSwipe = 1

# Keyboard Weights
enterInput = 4
doNotEnterInput = 10 - enterInput
closeKeyboard = 7
doNotCloseKeyboard = 10 - closeKeyboard

# Static Weights
defaultWeight = 40
baseWeight = 5
selfTransitionWeight = 2
crashWeight = 2
invalidTransitionWeight = 1
noPackageWeight = 1
notAllowedWeight = 1
noClickableViewWeight = 1


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
        self.cVisitFreq = []
        self.lcVisitFreq = []
        self.clickableXCoor = np.array([], dtype=int)
        self.clickableYCoor = np.array([], dtype=int)
        self.e_clickableXCoor = np.array([], dtype=int)
        self.e_clickableYCoor = np.array([], dtype=int)
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
        self.canSwipeLeft = False
        self.canSwipeRight = False
        self.scrollableX = []
        self.scrollableY = []
        self.e_scrollableX = []
        self.e_scrollableY = []
        self.c_scrollableX = []
        self.c_scrollableY = []
        self.scrollableResourceId = []
        self.scrollableView = []

        # Weights
        self.cTransitionWeight = []
        self.lcTransitionWeight = []

        # Conditions
        clickCondition = "'clickable': 'true'"
        enabledCondition = "'enabled': 'true'"
        longClickCondition = "'long-clickable': 'true'"
        scrollCondition = "'scrollable': 'true'"

        # Keeps track of all Long Click views
        longClickIndex = 0

        # Parsing with ET to obtain dump information
        root = ET.fromstring(state)
        for elem in root.iter():
            strAttrib = str(elem.attrib)
            # View is enabled and clickable
            if clickCondition in strAttrib and enabledCondition in strAttrib:

                # Obtain Start XY Coordinates of clickable and enabled views
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

                # Obtain End XY Coordinates of clickable and enabled views
                start = strAttrib.find("[") + len(str(yCoordinate)) + len(str(xCoordinate)) + 3
                end = strAttrib.find(" '", start)
                temp = strAttrib[start:end]
                start = temp.find("[") + 1
                end = temp.find(",", start)
                self.e_clickableXCoor = np.append(self.e_clickableXCoor, int(temp[start:end]))
                start = temp.find(",") + 1
                end = temp.find("]", start)
                self.e_clickableYCoor = np.append(self.e_clickableYCoor, int(temp[start:end]))

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

                # Update cVisitFreq List
                self.cVisitFreq.append(0)

                # View is long-clickable
                if longClickCondition in strAttrib:
                    self.longClickable.append(longClickIndex)
                    # Set long-clickable weights to default
                    self.lcTransitionWeight.append(defaultWeight)
                    # Long clicks Present
                    self.hasLongClicks = True
                    # Update lcVisitFreq List
                    self.lcVisitFreq.append(0)

                longClickIndex = longClickIndex + 1

            # Find scrollable views
            if scrollCondition in strAttrib and enabledCondition in strAttrib:
                # Obtain Start XY Coordinates of scrollable views
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

                # Obtain End XY Coordinates of scrollable views
                start = strAttrib.find("[") + len(str(yCoordinate)) + len(str(xCoordinate)) + 3
                end = strAttrib.find(" '", start)
                temp = strAttrib[start:end]
                start = temp.find("[") + 1
                end = temp.find(",", start)
                self.e_scrollableX.append(int(temp[start:end]))
                start = temp.find(",") + 1
                end = temp.find("]", start)
                self.e_scrollableY.append(int(temp[start:end]))

                # Obtain scrollable view names
                start = strAttrib.find("'class': '") + 10
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                temp = str(temp)
                self.scrollableView.append(temp)

                # Obtain scrollable resource id
                start = strAttrib.find("'resource-id': '") + 16
                end = strAttrib.find("'", start)
                temp = strAttrib[start:end]
                if temp == '':
                    temp = '(No resource.id)'
                    self.scrollableResourceId.append(temp)
                else:
                    self.scrollableResourceId.append(temp)

        # Single scrollable view
        if len(self.scrollableX) == 1:
            self.isScrollable = True
            self.canScrollDown = True
            self.canScrollUp = True
            self.canSwipeLeft = True
            self.canSwipeRight = True

            # X-Center coordinates
            temp = int(((self.e_scrollableX[0] - self.scrollableX[0]) / 2) + self.scrollableX[0])
            self.c_scrollableX.append(temp)
            # Y-Center coordinates
            temp = (((self.e_scrollableY[0] - self.scrollableY[0]) / 2) + self.scrollableY[0])
            self.c_scrollableY.append(temp)

        # Multiple scrollable views
        if len(self.scrollableX) > 1:
            # isScrollable = False by default
            self.isMultiScrollable = True

            # Obtain center of scrollable views
            for i in range(len(self.scrollableX)):
                # X-Center coordinates
                temp = int(((self.e_scrollableX[i]-self.scrollableX[i])/2) + self.scrollableX[i])
                self.c_scrollableX.append(temp)
                # Y-Center coordinates
                temp = (((self.e_scrollableY[i]-self.scrollableY[i])/2) + self.scrollableY[i])
                self.c_scrollableY.append(temp)

        # Get number of clickable views
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
    enabledCondition = "'enabled': 'true'"
    longClickCondition = "'long-clickable': 'true'"
    scrollCondition = "'text': 'true'"
    # Attributes
    resourceId = ''
    view = ''
    package = ''
    text = ''
    longClickable = ''
    scroll = ''
    root = ET.fromstring(state)
    for elem in root.iter():
        strAttrib = str(elem.attrib)
        # Find clickable Views
        if clickCondition in strAttrib and enabledCondition in strAttrib:
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
            # resource-id is empty
            if temp == '':
                temp = '(No resource.id)'
                resourceId = resourceId + temp
            # Has resource-id
            else:
                resourceId = resourceId + temp
            # Obtain text
            start = strAttrib.find("'text': '") + 9
            end = strAttrib.find("'", start)
            temp = strAttrib[start:end]
            # Text is empty
            if temp == '':
                temp = '(No text)'
                text = text + temp
            else:
                text = text + temp

            # Long clickable
            if longClickCondition in strAttrib:
                longClickable = longClickable + "True"
        # Determine if scrollable
        if scrollCondition in strAttrib and enabledCondition in strAttrib:
            scroll = scroll + 'True'

    # Return Hash
    return hashlib.md5((package+view+resourceId+text+longClickable+scroll)).digest().encode("base64")


def generateHashedHierarchy(state):
    # Used only for identifying unique state during swiping
    return hashlib.md5(state).digest().encode("base64")


def setupLogFile():
    global f
    global tcLocation
    global appName
    exists = os.path.isfile(tcLocation + "/testCases.py")
    # File already created
    if exists:
        print("File Exists, adding new test case to " + tcLocation)
        # Use existing python test file
        f = open(tcLocation + "/testCases.py", "a")
        f.write("# New Test Case\n")
        f.write("# Target App: " + str(appName) + "\n")
        f.write("# Target: " + str(numberOfInstructions) + " actions\n")

    # File not created
    else:
        print("Creating new test case file at " + tcLocation)
        # Create new Python test file
        f = open(tcLocation + "/testCases.py", "a+")

        # Import List
        f.write("from uiautomator import device as d\n")
        f.write("import time\n")
        f.write("import subprocess\n\n")
        f.write("# New Test Case\n")
        f.write("# Target App: " + str(appName) + "\n")
        f.write("# Number of actions: " + str(numberOfInstructions) + "\n")


def addNode(state):
    global stateCount
    global prevNode
    global stateList
    global selectionType
    global baseWeight
    global noClickableViewWeight
    global lcIndex

    x = Node('S' + str(stateCount), state, (prevNode.depth + 1))
    stateList.append(x)

    # New state does not have any clickable views
    if stateList[stateCount].noClickableView is True:
        stateCount = stateCount + 1

        # Adjust previous node's weights and # of visits
        if selectionType == 'click':
            prevNode.cVisitFreq[prevNode.currentIndex] += 1
            prevNode.cTransitionWeight[prevNode.currentIndex] = noClickableViewWeight

        if selectionType == 'long-click':
            prevNode.lcVisitFreq[lcIndex] += 1
            prevNode.lcTransitionWeight[lcIndex] = noClickableViewWeight

        print("New node no clickable views")
        back("New node no clickable Views")
        return

    # (Normal Operation) Adjust previous node's weights and # of visits
    if selectionType == 'click':
        prevNode.cVisitFreq[prevNode.currentIndex] += 1
        prevNode.cTransitionWeight[prevNode.currentIndex] = baseWeight + x.clickableLength + \
                                                            len(x.longClickable) + len(x.scrollableX)

    if selectionType == 'long-click':
        prevNode.lcVisitFreq[lcIndex] += 1
        prevNode.lcTransitionWeight[lcIndex] = baseWeight + x.clickableLength + \
                                                            len(x.longClickable) + len(x.scrollableX)

    # New State that has clickable views
    prevNode = stateList[stateCount]
    stateCount = stateCount + 1
    print("New node added: " + prevNode.name)
    return


# GUI Setup
def save(entries):
    global gui
    global appName
    global numberOfInstructions
    global deviceName
    global ssLocation
    global tcLocation

    # Store App Name
    appName = "'content-desc': '" + str(entries[0].get())

    # Store number of actions
    try:
        numberOfInstructions = int(entries[1].get())

        # Check zero or negative number of actions
        if numberOfInstructions <= 0:
            print("Using default number of actions (500)")
            numberOfInstructions = 500
    except ValueError:
        showerror("Invalid input", "Enter an integer for # of Actions")
        return

    # Store device name
    deviceName = str(entries[2].get())

    # Store Screenshot location
    ssLocation = str(entries[3].get())

    # Store test_case.py location
    tcLocation = str(entries[4].get())

    showinfo("Success", "Settings Saved.")
    gui.quit()


def userInputSettings():
    global gui

    # Preset Values
    label = ['App Name (Case Sensitive):', '# of Actions:', 'Device: ', 'Screenshot Location:',
             'test_case.py Location:']
    default = ['Tricky', 500, '192.168.8.101:5555', "C:/Users/awslw/Desktop/FYP/uiAutomator Dump/Pics/",
               "C:/Users/awslw/Desktop/FYP/uiAutomator Dump/"]

    entries = []
    temp = []
    # Gui Settings
    gui.title("Settings")
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

    # Save button
    Button(gui, text="Save", command=(lambda e=entries: save(e)), width=10, relief="groove")\
        .grid(row=index + 1, column=1, pady=4, sticky=W)
    gui.mainloop()
    gui.destroy()


# Emulator Operations
def back(text):
    global prevNode
    global stateCount
    global stateList
    global backFlag
    global selectionType

    # Set back() flag to True to skip nodeCheck
    backFlag = True

    # Set selection type

    # Operation
    d.press.back()
    d.wait.update()
    time.sleep(2.5)
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
        # Re-obtain current state
        backState = d.dump(compressed=True).encode('utf-8')
        backState_h = generateHashedState(backState)

    # back() into 3rd party app
    package = checkCurrentPackage(backState)
    if package != m.package:
        back("Still in 3rd party app")
        return

    # back() into same state (Activity cannot be back() - Permissions)
    if backState_h == prevNode.state:
        # Click on the first clickable object to exit
        d(clickable=True).click()
        f.write("d(clickable=True).click()  # Within a state that cannot be back()\n")
        print("Within a state that cannot be back()")

        # Obtain new state
        backState = d.dump(compressed=True).encode('utf-8')
        backState_h = generateHashedState(backState)

    # back() to known state
    for i in range(len(stateList)):
        # If back() to known state
        if backState_h == stateList[i].state:
            print("back() into Existing State: " + stateList[i].name)
            prevNode = stateList[i]
            return

    # back() to unknown state, Add new node
    msg = "back() into Unknown State"
    selectionType = 'back'
    print(msg)
    f.write("#" + msg + "\n")
    addNode(backState)
    return


def click(xCoor, yCoor):
    global prevNode
    # Normal Operation if current state is Main screen
    if prevNode.state == m.state:
        xCoor_c = xCoor + 10
        yCoor_c = yCoor + 10
    # Get XY coordinates of center
    else:
        # Get XY Coordinates of the center (of clickable view)
        xCoor_c = int((prevNode.e_clickableXCoor[prevNode.currentIndex] - xCoor)/2) + xCoor
        yCoor_c = int((prevNode.e_clickableYCoor[prevNode.currentIndex] - yCoor)/2) + yCoor


    # Print information
    temp = 'd.click(' + str(xCoor_c) + ', ' + str(yCoor_c) + ') # At '
    info = prevNode.name + ', ' + prevNode.views[prevNode.currentIndex] + ', ' + prevNode.resourceId[
        prevNode.currentIndex]
    print(temp + info)

    # Operation
    d.click((xCoor_c), (yCoor_c))
    time.sleep(2)

    # Write to log file
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2)\n")
    d.wait.update()


def long_click(xCoor,yCoor):
    global prevNode
    # Get XY Coordinates of the center (of clickable view)
    xCoor_c = int((prevNode.e_clickableXCoor[prevNode.currentIndex] - xCoor) / 2) + xCoor
    yCoor_c = int((prevNode.e_clickableYCoor[prevNode.currentIndex] - yCoor) / 2) + yCoor

    # Print Information
    temp = 'd.long_click(' + str(xCoor_c) + ', ' + str(yCoor_c) + ') # At '
    info = prevNode.name + ', ' + prevNode.views[prevNode.currentIndex] + ', ' + prevNode.resourceId[
        prevNode.currentIndex]
    print(temp + info)

    # Operation
    d.long_click(xCoor_c, yCoor_c)
    time.sleep(1.5)

    # Write to log file
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2)\n")
    d.wait.update()


# Scroll/Swipe Operations
def scroll_up():
    global prevNode
    global selectionType
    global scrollSteps
    selectionType = "scroll"
    # Operation
    d.swipe(prevNode.c_scrollableX[prevNode.currentIndex], prevNode.c_scrollableY[prevNode.currentIndex],
            prevNode.c_scrollableX[prevNode.currentIndex], prevNode.e_scrollableY[prevNode.currentIndex] - 5,
            steps=scrollSteps)
    d.wait.update()
    time.sleep(2)

    # Print Operation details
    strTemp = str(prevNode.c_scrollableX[prevNode.currentIndex]) + ", " + \
              str(prevNode.c_scrollableY[prevNode.currentIndex]) + ", " + \
              str(prevNode.c_scrollableX[prevNode.currentIndex]) + ", " + \
              str(prevNode.e_scrollableY[prevNode.currentIndex] - 5) + ", steps=" + str(scrollSteps)

    temp = "d.swipe(" + strTemp + ")\n# Scroll up At "

    info = prevNode.name + ', ' + prevNode.scrollableView[prevNode.currentIndex] + ', ' + \
           prevNode.scrollableResourceId[prevNode.currentIndex]

    print(temp + info)
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2.5)\n")


def scroll_down():
    global prevNode
    global selectionType
    global scrollSteps
    # Change selection type
    selectionType = "scroll"
    # Operation
    d.swipe(prevNode.c_scrollableX[prevNode.currentIndex], prevNode.c_scrollableY[prevNode.currentIndex],
            prevNode.c_scrollableX[prevNode.currentIndex], prevNode.scrollableY[prevNode.currentIndex] + 5,
            steps=scrollSteps)
    d.wait.update()
    time.sleep(2)
    # Print Operation details
    strTemp = str(prevNode.c_scrollableX[prevNode.currentIndex]) + ", " + \
              str(prevNode.c_scrollableY[prevNode.currentIndex]) + ", " + \
              str(prevNode.c_scrollableX[prevNode.currentIndex]) + ", " + \
              str(prevNode.scrollableY[prevNode.currentIndex] + 5) + ", steps=" + str(scrollSteps)

    temp = "d.swipe(" + strTemp + ")\n# Scroll down At "

    info = prevNode.name + ', ' + prevNode.scrollableView[prevNode.currentIndex] + ', ' + \
           prevNode.scrollableResourceId[prevNode.currentIndex]

    print(temp + info)
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2.5)\n")


def swipe_left():
    global prevNode
    global selectionType
    global scrollSteps
    # Change selection type
    selectionType = "swipe"
    # Operation
    d.swipe(prevNode.c_scrollableX[prevNode.currentIndex], prevNode.c_scrollableY[prevNode.currentIndex],
            prevNode.scrollableX[prevNode.currentIndex] + 5, prevNode.c_scrollableY[prevNode.currentIndex],
            steps=scrollSteps)
    d.wait.update()
    time.sleep(2)
    # Print Operation details
    strTemp = str(prevNode.c_scrollableX[prevNode.currentIndex]) + ", " + \
              str(prevNode.c_scrollableY[prevNode.currentIndex]) + ", " + \
              str(prevNode.scrollableX[prevNode.currentIndex] + 5) + ", " + \
              str(prevNode.c_scrollableY[prevNode.currentIndex]) + ", steps=" + str(scrollSteps)

    temp = "d.swipe(" + strTemp + ")\n# Swipe Left At "

    info = prevNode.name + ', ' + prevNode.scrollableView[prevNode.currentIndex] + ', ' + \
           prevNode.scrollableResourceId[prevNode.currentIndex]

    print(temp + info)
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2.5)\n")


def swipe_right():
    global prevNode
    global selectionType
    global scrollSteps
    # Change selection type
    selectionType = "swipe"
    # Operation
    d.swipe(prevNode.c_scrollableX[prevNode.currentIndex], prevNode.c_scrollableY[prevNode.currentIndex],
            prevNode.e_scrollableX[prevNode.currentIndex] - 5, prevNode.c_scrollableY[prevNode.currentIndex],
            steps=scrollSteps)
    d.wait.update()
    time.sleep(2)
    # Print Operation details
    strTemp = str(prevNode.c_scrollableX[prevNode.currentIndex]) + ", " + \
              str(prevNode.c_scrollableY[prevNode.currentIndex]) + ", " + \
              str(prevNode.e_scrollableX[prevNode.currentIndex] - 5) + ", " + \
              str(prevNode.c_scrollableY[prevNode.currentIndex]) + ", steps=" + str(scrollSteps)

    temp = "d.swipe(" + strTemp + ")\n# Swipe Right At "

    info = prevNode.name + ', ' + prevNode.scrollableView[prevNode.currentIndex] + ', ' + \
           prevNode.scrollableResourceId[prevNode.currentIndex]

    print(temp + info)
    f.write(temp + info + "\n")
    f.write("d.wait.update()\n")
    f.write("time.sleep(2.5)\n")


# Logic Checks
def checkEmulator():
    global deviceName
    cmd = 'adb devices'
    s = subprocess.check_output(cmd)

    if deviceName in s:
        print("Target Device Detected")
        return

    print("Target device not connected. Testing Aborted")
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

        # Did not input any text
        else:
            print("Did not input text.")

        # Decision to open/close keyboard
        decisionClose = random.choice([0] * closeKeyboard + [1] * doNotCloseKeyboard)

        # Close Keyboard
        if decisionClose == 0:
            # Manual back() (use nodeCheck() to ascertain state)
            d.press.back()
            d.wait.update()
            text = "Close Keyboard"
            print("d.press.back() - " + str(text))
            f.write("d.press.back() # " + str(text) + "\n")
            f.write("d.wait.update()\n")
            f.write("time.sleep(2.5)\n")
            time.sleep(1.5)
            return

        print("Did not close keyboard")
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
    d.screenshot(ssLocation + "Invalid State " + str(len(invalidStateList)) + '.png')
    return ''


def checkUnvisitedView(node):
    total = 0

    # Check unvisited clickable view
    for i in range(len(node.cVisitFreq)):
        if node.cVisitFreq[i] == 0:
            total += 1

    # Check unvisited longclickable view
    for i in range(len(node.lcVisitFreq)):
        if node.lcVisitFreq[i] == 0:
            total += 1

    # Check # of scrollable views
    total += len(node.scrollableX)

    return total


def checkNode():
    global stateList
    global prevNode
    global stateCount
    global selfTransitionCount
    global crashNum
    global lcIndex
    global definedInvalidState
    global notAllowedWeight

    # Get hashed versions of current State
    currentState = d.dump(compressed=True).encode('utf-8')
    currentState_h = generateHashedState(currentState)
    temp = checkCurrentPackage(currentState)

    # Check if app has crashed
    if checkCrash(currentState_h) is True:
        return

    # Check current state's package
    if temp != m.package:
        # Current state package is empty
        if temp == '':
            # Adjust weights of previous node's index based on selection type
            if selectionType == 'click':
                prevNode.cVisitFreq[prevNode.currentIndex] += 1
                prevNode.cTransitionWeight[prevNode.currentIndex] = noPackageWeight

            if selectionType == 'long-click':
                prevNode.lcVisitFreq[lcIndex] += 1
                prevNode.lcTransitionWeight[lcIndex] = noPackageWeight

            back("Transition into state with no package name")
            return

        # Current state package is "android" - Possible crash
        if temp == 'android':
            # Manual back() out of error message
            d.press.back()
            d.wait.update()
            time.sleep(2)
            f.write("d.press.back() # Possible Crash Detected\n")
            f.write("d.wait.update()\n")
            f.write("time.sleep(3)\n")
            print("d.press.back() - Possible Crash Detected")
            # Check if app has crashed
            if checkCrash(currentState_h) is True:
                return

        # Current state package belongs to unapproved 3rd party
        else:
            if selectionType == 'click':
                prevNode.cVisitFreq[prevNode.currentIndex] += 1
                prevNode.cTransitionWeight[prevNode.currentIndex] = invalidTransitionWeight

            if selectionType == 'long-click':
                prevNode.lcVisitFreq[lcIndex] += 1
                prevNode.lcTransitionWeight[lcIndex] = invalidTransitionWeight

            # prevNode updated in back()
            back("Transition into invalid 3rd party app")

            # Update Self transition count
            selfTransitionCount += 1
            return


    # Check if current state is allowed (Not in defined invalid list)
    for i in range(len(definedInvalidState)):
        if definedInvalidState[i] == str(currentState_h):
            # Adjust Weights
            if selectionType == 'click':
                prevNode.cVisitFreq[prevNode.currentIndex] += 1
                prevNode.cTransitionWeight[prevNode.currentIndex] = notAllowedWeight

            if selectionType == 'long-click':
                prevNode.lcVisitFreq[lcIndex] += 1
                prevNode.lcTransitionWeight[lcIndex] = notAllowedWeight

            back("Transitioned into defined invalid state")
            return

    # Check if state exists
    stateExist = False
    index = 0

    for i in range(len(stateList)):
        if currentState_h == stateList[i].state:
            stateExist = True
            break

        index = index + 1

    # Transition to new state
    if stateExist is False:
        # Add new state
        addNode(currentState)
        return

    # Transition to existing state
    else:
        # Self Transition
        if currentState_h == prevNode.state:
            # Adjust weights of previous node's index
            if selectionType == 'click':
                prevNode.cVisitFreq[prevNode.currentIndex] += 1
                prevNode.cTransitionWeight[prevNode.currentIndex] = selfTransitionWeight

            if selectionType == 'long-click':
                prevNode.lcVisitFreq[lcIndex] += 1
                prevNode.lcTransitionWeight[lcIndex] = selfTransitionWeight

            # Add self transition count
            selfTransitionCount = selfTransitionCount + 1
            temp = "Self Transition in " + prevNode.name
            print(temp)
            f.write("# " + temp + "\n")

            # prevNode stays the same
            return

        # Transition to another known state
        else:
            # Transition between known states, check if prevNode is NOT main menu
            if prevNode.state != m.state:
                # Adjust weights of previous node's index (TBC..)
                if selectionType == 'click':
                    prevNode.cVisitFreq[prevNode.currentIndex] += 1
                    # Obtain total # of unvisited clickable views
                    uTotal = checkUnvisitedView(stateList[index])
                    prevNode.cTransitionWeight[prevNode.currentIndex] = baseWeight + uTotal

                if selectionType == 'long-click':
                    prevNode.lcVisitFreq[lcIndex] += 1
                    # Obtain total # of unvisited clickable views
                    uTotal = checkUnvisitedView(stateList[index])
                    prevNode.lcTransitionWeight[lcIndex] = baseWeight + uTotal

            # Reset self transition flag
            selfTransitionCount = 0

            # Update Log file and display information
            temp = "Transition from " + prevNode.name + "(" + str(prevNode.depth) + ") to " + stateList[
                index].name + "(" + str(stateList[index].depth) + ")"
            print(temp)
            f.write("# " + temp + "\n")

            # Set current node as prevNode
            prevNode = stateList[index]

            return


def checkCrash(currentState):
    global prevNode
    global crashNum
    global selectionType
    global crashWeight
    global stateList

    # Check if app has crashed
    if currentState == m.state:
        # Adjust weights of previous node's index
        if selectionType == 'click':
            prevNode.cVisitFreq[prevNode.currentIndex] += 1
            prevNode.cTransitionWeight[prevNode.currentIndex] = crashWeight

        if selectionType == 'long-click':
            prevNode.lcVisitFreq[lcIndex] += 1
            prevNode.lcTransitionWeight[lcIndex] = crashWeight

        # Update number of possible crash
        crashNum = crashNum + 1
        temp = "-Possible Crash Occurred-"
        print(temp)
        f.write("# " + temp + "\n")
        prevNode = m
        click(m.appXCoor, m.appYCoor)
        f.write("# New Test Case \n")

        # Obtain current state after reopening app
        c_currentState = d.dump(compressed=True).encode('utf-8')
        c_currentState_h = generateHashedState(currentState)

        # Open App into known state
        for i in range(len(stateList)):
            # If back() to known state
            if c_currentState_h == stateList[i].state:
                print("Open app into Existing State: " + stateList[i].name)
                prevNode = stateList[i]
                return True

        # Open app into unknown state, Add new node
        msg = "Open app into Unknown State"
        selectionType = 'invalid'
        print(msg)
        f.write("#" + msg + "\n")
        addNode(c_currentState)
        return True

    return False


def currentIndexDecision(decision):
    global prevNode
    global selectionType
    global lcIndex
    # Index logic point for Long Click
    if decision == 'long-click':
        # Change selection type
        selectionType = "long-click"

        # Selection of index based on weight
        probabilityList = [0] * prevNode.lcTransitionWeight[0]

        for i in range(1, (len(prevNode.lcTransitionWeight))):
            probabilityList = probabilityList + ([i] * prevNode.lcTransitionWeight[i])

        lcIndex = random.choice(probabilityList)


        # Workaround for a rare bug that occurs, default to index 0
        if lcIndex >= len(prevNode.lcTransitionWeight):
            print("lcIndex > length Bug, index defaults to 0")
            lcIndex = 0

        return prevNode.longClickable[lcIndex]

    # Index logic point for Normal Click
    if decision == 'click':
        # Change selection type
        selectionType = 'click'

        # Selection of index based on weight
        probabilityList = [0]*prevNode.cTransitionWeight[0]

        for i in range(1, (len(prevNode.cTransitionWeight))):
            probabilityList = probabilityList + ([i] * prevNode.cTransitionWeight[i])

        return random.choice(probabilityList)

    # Index logic point for Swiping (Multiple)
    if decision == 'swipe':
        return random.randint(0, (len(prevNode.c_scrollableX)-1))

    # Index logic point for Scrolling (Multiple)
    if decision == 'scroll':
        return random.randint(0, (len(prevNode.c_scrollableX) - 1))


def operationDecision():
    global prevNode
    global selectionType
    global numberOfInstructions
    # Decision Point (Weighted Random Algorithm)
    choice = random.choice(['lc'] * chanceOfLongClicks + ['sc'] * chanceOfScroll + ['c'] * chanceOfNormalClicks
                           + ['sw'] * chanceOfSwipe)

    # Long Click Selected
    if choice == 'lc':
        # State has no long clicks
        if prevNode.hasLongClicks is False:
            # Re-randomise
            temp = chanceOfLongClicks / 2
            choice = random.choice(['sw'] * (chanceOfSwipe + temp) + ['c'] * (chanceOfNormalClicks + temp))

        # State has long clicks
        else:
            # Index decision
            prevNode.currentIndex = currentIndexDecision('long-click')

            # Long Click Operation
            long_click(prevNode.clickableXCoor[prevNode.currentIndex], prevNode.clickableYCoor[prevNode.currentIndex])
            return

    # Swipe Selected
    if choice == 'sw':
        # Not swipe-able, default to click
        if prevNode.isScrollable is False and prevNode.isMultiScrollable is False:
            choice = 'c'

        # State has multiple scrollable views
        elif prevNode.isMultiScrollable is True:
            # Equal Chance to swipe L/R
            multiSwipeDecision = random.randint(0,1)

            # Swipe left Decision
            if multiSwipeDecision == 0:
                # Randomly pick a scrollable view (Equal chance)
                prevNode.currentIndex = currentIndexDecision('swipe')
                try:
                    swipe_left()
                    return
                except:
                    print("Cannot swipe left, click instead")
                    choice = 'c'

            # Swipe right Decision
            else:
                # Randomly pick a scrollable view (Equal chance)
                prevNode.currentIndex = currentIndexDecision('swipe')
                try:
                    swipe_right()
                    return
                except:
                    print("Cannot swipe right, click instead")
                    choice = 'c'

        # State only has 1 swipe-able view
        elif prevNode.isScrollable is True:
            # Able to swipe left and right
            if prevNode.canSwipeLeft is True and prevNode.canSwipeRight is True:
                # Direction Decision Point
                swipeDecision = random.randint(0, 1)

                # Swipe Left decided
                if swipeDecision == 0:
                    # Bypass swipe errors
                    try:
                        pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                        prevNode.currentIndex = 0
                        swipe_left()
                    except:
                        print("Error swiping left, no action taken")
                        numberOfInstructions = numberOfInstructions - 1
                        return

                    # Check current Hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))

                    # Cannot swipe left (Self Transition)
                    if pHierarchy == cHierarchy:
                        prevNode.canSwipeLeft = False
                        print("Cannot Swipe Left")

                    return

                # Swipe Right decided
                else:
                    # Bypass swipe errors
                    try:
                        pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                        prevNode.currentIndex = 0
                        swipe_right()
                    except:
                        print("Error swiping right, no action taken")
                        numberOfInstructions = numberOfInstructions - 1
                        return

                    # Check current hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    # Cannot swipe right (Self Transition)
                    if pHierarchy == cHierarchy:
                        prevNode.canSwipeRight = False
                        print("Cannot swipe right")
                    return

            # Able to swipe only left
            elif prevNode.canSwipeLeft is True and prevNode.canSwipeRight is False:
                # Bypass swipe errors
                try:
                    pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    prevNode.currentIndex = 0
                    swipe_left()
                    # Check current Hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))

                    # Cannot swipe left (Self Transition)
                    if pHierarchy == cHierarchy:
                        print("Reached Right most view, re-enable swipe-right")
                        prevNode.canSwipeLeft = False
                        prevNode.canSwipeRight = True

                    return
                except:
                    print("Error swiping left, click instead")
                    # Defaults to click
                    choice = 'c'

            # Able to swipe only right
            elif prevNode.canSwipeRight is True and prevNode.canSwipeLeft is False:
                # Bypass swipe errors
                try:
                    pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    prevNode.currentIndex = 0
                    swipe_right()
                    # Check current Hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))

                    # Cannot swipe right (Self Transition)
                    if pHierarchy == cHierarchy:
                        print("Reached Left-most view, re-enable swipe left")
                        prevNode.canSwipeRight = False
                        prevNode.canSwipeLeft = True
                    return
                except:
                    print("Cannot swipe right, click instead")
                    # Defaults to click
                    choice = 'c'

            # Unable to swipe left or right, click instead
            else:
                # default to click
                choice = 'c'

    # Scroll Selected
    if choice == 'sc':
        # State cannot be scrolled
        if prevNode.isScrollable is False and prevNode.isMultiScrollable is False:
            choice = 'c'  # Default to normal click

        # State has multiple scrollable views
        elif prevNode.isMultiScrollable is True:
            # Equal Chance to scroll U/D
            multiScrollDecision = random.randint(0, 1)

            # Scroll down Decision
            if multiScrollDecision == 0:
                # Randomly pick a scrollable view (Equal chance)
                prevNode.currentIndex = currentIndexDecision('scroll')
                try:
                    scroll_down()
                    return
                except:
                    print("Cannot scroll down click instead")
                    choice = 'c'

            # Scroll up Decision
            else:
                # Randomly pick a scrollable view (Equal chance)
                prevNode.currentIndex = currentIndexDecision('scroll')
                try:
                    scroll_up()
                    return
                except:
                    print("Cannot scroll up, click instead")
                    choice = 'c'

        # State only has 1 scrollable view
        else:
            # State can scroll up and down
            if prevNode.canScrollDown is True and prevNode.canScrollUp is True:
                # Direction Decision Point
                scrollDecision = random.randint(0, 1)

                # Scroll up decided
                if scrollDecision == 0:
                    # Bypass scroll errors
                    try:
                        pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                        prevNode.currentIndex = 0
                        scroll_up()
                    except:
                        print("Error scrolling up, no action taken")
                        numberOfInstructions = numberOfInstructions - 1
                        return

                    # Check current Hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))

                    # Cannot scroll up (Self Transition)
                    if pHierarchy == cHierarchy:
                        prevNode.canScrollUp = False
                        print("Cannot scroll up")
                    return

                # Scroll down decided
                else:
                    # Bypass scroll errors
                    try:
                        pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                        prevNode.currentIndex = 0
                        scroll_down()
                    except:
                        print("Error scrolling down, no action taken")
                        numberOfInstructions = numberOfInstructions - 1
                        return

                    # Check current hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    # Cannot scroll down (Self Transition)
                    if pHierarchy == cHierarchy:
                        prevNode.canScrollDown = False
                        print("Cannot scroll down")

                    return

            # State can only scroll down
            elif prevNode.canScrollDown is True and prevNode.canScrollUp is False:
                # Bypass scroll errors
                try:
                    pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    prevNode.currentIndex = 0
                    scroll_down()
                    # Check current hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    # Cannot scroll down (Self Transition)
                    if pHierarchy == cHierarchy:
                        prevNode.canScrollDown = False
                        prevNode.canScrollUp = True
                        print("Reached bottom, re-enable scroll up")
                    return
                except:
                    print("Error scrolling down, click instead")
                    # Defaults to click
                    choice = 'c'

            # State can only scroll up
            elif prevNode.canScrollUp is True and prevNode.canScrollDown is False:
                # Bypass scroll errors
                try:
                    pHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    prevNode.currentIndex = 0
                    scroll_up()
                    # Check current hierarchy
                    cHierarchy = generateHashedHierarchy(d.dump(compressed=True).encode('utf-8'))
                    # Cannot scroll down (Self Transition)
                    if pHierarchy == cHierarchy:
                        prevNode.canScrollDown = True
                        prevNode.canScrollUp = False
                        print("Reached top, re-enable scroll down")
                    return
                except:
                    print("Error scrolling up, click instead")
                    # Defaults to click
                    choice = 'c'

            # State cannot scroll up or down
            else:
                # Defaults to click
                choice = 'c'

    # Normal Click Selected
    if choice == 'c':
        # Index decision
        prevNode.currentIndex = currentIndexDecision('click')

        # Normal Click Operation
        click(prevNode.clickableXCoor[prevNode.currentIndex], prevNode.clickableYCoor[prevNode.currentIndex])
        return


# Initialise default User Inputs (Global)
numberOfInstructions = 0
appName = ''
deviceName = ''

# Override (GUI)
try:
    gui = Tk()
    userInputSettings()
except:
    print("Settings not set. Testing Aborted.")
    sys.exit()

# Pre-Test Checks
checkEmulator()
setupLogFile()

# Initialization
G = nx.MultiDiGraph()       # Create Visual Graph
stateCount = 0              # Keeps track of number of States
stateList = []              # Keeps track of states
invalidStateList = []       # Keeps track of invalid states (No clickable views)
crashNum = 0                # Keeps track of number of crashes
selfTransitionCount = 0     # Keeps track of number of self transsitions
backFlag = False            # Skips checkNode() when back() is invoked
selectionType = "click"     # Keeps track of current selection Type (Eg: Click, Scroll, etc)
lcIndex = 0                 # Keeps track of current long-click index (for lcTransitionWeight[])
sTime = time.time()         # Store start time, should be the last line of initialization

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

# Random Algorithm, limited to number of instructions
instCount = 0

# Loop till every clickable view in main activity is selected
while instCount < numberOfInstructions:
    # Reset back() flag
    backFlag = False

    # Random Algorithm
    operationDecision()

    # Pre-Checks
    checkKeyboard()
    checkSelfTransLimit()

    # Transition Checks
    if backFlag is False:
        checkNode()

    # Instruction Counter
    instCount = instCount + 1

# Exiting from App
d.press.home()
d.wait.update()

# Obtain elapsed tme
eTime = time.time() - sTime

# Update console and log
print("End Test Case, Number of crashes detected: " + str(crashNum))
print("Total Actions: " + str(numberOfInstructions))
print("Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(eTime))))
f.write("d.press.home()\n")
f.write("# -End Test Case-\n")
f.write("# -Number of crashes detected: " + str(crashNum) + "\n")
f.write("# Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(eTime))) + "\n")
f.close()

