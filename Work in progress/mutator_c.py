
# Made by: Aaron
# Name: Mutator
# Description: Mutate Culebra test cases to detect problems in apps
#              [Work in progress, currently a prototype with limited functionality]


import subprocess
from uiautomator import device as d
import numpy as np
import time
from Tkinter import *
from tkMessageBox import *
from dill.source import getsource

# Static Values
rotationDelay = 1.5


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


# GUI Interface
def save(entries, checkboxes):
    global gui
    global testCasePath
    global testCaseName
    global package
    global startMutation
    global enableMutation

    # Package Name
    package = str(entries[0].get())

    # Test Case path
    testCasePath = str(entries[1].get())

    # Test Case name
    testCaseName = str(entries[2].get())

    # Start Mutation
    startMutation = int(entries[3].get())
    # Negative startMutation
    if startMutation < 0:
        startMutation = 0

    # Enable Mutation
    temp = str(checkboxes[0].get())
    if temp == '0':
        enableMutation = False
    else:
        enableMutation = True

    # Close GUI
    showinfo("Success", "Settings Saved.")
    gui.quit()


def setupGUI():
    global gui

    # Preset Values
    label = ["App Package Name: ", 'Test Case Path: ', 'Test Case name: ', 'Start Mutation: \n(0 - After S0)']
    default = ['it.feio.android.omninotes.foss', 'C:/Users/awslw/Desktop/FYP/AndroidViewClient-master/tools',
               'myTestCase', 0]
    checkboxLabel = ['Enable Mutation']

    # Widget Storage
    entries = []
    checkbox = []  # Container for all checkboxes
    vars = []  # Keeps track of integer values of checkboxes (0 - False, 1 - True)

    # Gui Settings
    gui.title("mutator_C Setup")
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


# Not all culebra operations added
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


# Not all possible culebration detection methods added
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


# Mutation Decision Point
def mutationSelect():
    rotation()


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


# (Default) User defined inputs
testCasePath = ''
testCaseName = ''
package = ''
startMutation = 0
enableMutation = False

# Override (GUI)
try:
    gui = Tk()
    setupGUI()
except:
    print("Settings not set. Testing Aborted.")
    sys.exit()

#  Initialization
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

# Add each instruction as a new object
for i in range(len(instList)):
    newNode = UserNode(instList[i], i)
    nodeList.append(newNode)

# User defined test case without mutations
if enableMutation is False:
    print("Start Normal Testing")
    # Benchmark
    sTime = time.time()
    # Test
    for i in range(len(nodeList)):
        # Normal Operation
        nodeList[i].action()

    # Obtain elapsed time
    eTime = time.time() - sTime
    print("Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(eTime))))
    print("- Test Completed -")

# User defined test case with mutations
else:
    print("Start Mutation-based Testing after S" + str(startMutation))
    # Benchmark
    sTime = time.time()

    # User defined operation
    for i in range(len(nodeList)):
        nodeList[i].action()
        # Mutation from user defined start state
        if i >= startMutation:
            mutationSelect()

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

    # Force close app upon
    cmd = "adb shell am force-stop " + package
    subprocess.call(cmd)
    time.sleep(1)
    # Obtain elapsed time
    eTime = time.time() - sTime
    print("Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(eTime))))
    print("- Test Completed -")
