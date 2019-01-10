#####################################################################################################################
# Made by:      Aaron                                                                                               #
# Desciption:   A python script that uses uiAutomator python wrapper to generate XY coordinates of                  #
#               clickable/scrollable views, which is crucial for simulating and automating basic user actions,      #
#               such as pressing, scrolling, etc. This script only prints coordinates and other useful information  #
#               obtained from uiAutomator's dump().                                                                 #
#               Additional uiAutomator's methods (Eg: d.click(x,y)) can be added at the bottom of the program.      #
#####################################################################################################################

import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
from uiautomator import device as d
import numpy as np
import sys
import random as rd
import time
import hashlib


# To generate hashed states
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


def generateHashedHierachy(state):
    return hashlib.md5(state).digest().encode("base64")


# Use uiAutomator's dump to get screen details
state1 = d.dump(compressed=True).encode('utf-8')
time.sleep(1.5)

# Initialise all required arrays/variables
view = []
resourceId = []
clickableXCoor = np.array([])
clickableYCoor = np.array([])
eClickableXCoor = np.array([])
eClickableYCoor = np.array([])
cVisitFreq = []
package = ''
state = ''
longClickable = []
longClickableIndex = []
lcVisitFreq = []
scrollableX = []
scrollableY = []
e_scrollableX = []
e_scrollableY = []
c_scrollableX = []
c_scrollableY = []
scrollableResourceId = []
scrollableView = []
invalidStateList = []
text = []


# Various conditional statements to extract info
condition = "'clickable': 'true'"
condition2 = "'long-clickable': 'true'"
condition3 = "'scrollable': 'true'"
scrollCondition = "'text': 'true'"
enabledCondition = "'enabled': 'true'"
root = ET.fromstring(state1)
longClickIndex = 0

# Iterate through hierarchy (from d.dump) to obtain XY coordinates, etc
for elem in root.iter():
    strAttrib = str(elem.attrib)
    # clickable
    if condition in strAttrib:
        # Obtain XY Coordinates of clickable coordinates (Start)
        start = strAttrib.find("'bounds': '") + 12
        end = strAttrib.find('[', start)
        temp = strAttrib[start:end]
        start = temp.find("[") + 1
        end = temp.find(",", start)
        xCoordinate = int(temp[start:end])
        clickableXCoor = np.append(clickableXCoor, xCoordinate)
        start = temp.find(",") + 1
        end = temp.find("]", start)
        yCoordinate = int(temp[start:end])
        clickableYCoor = np.append(clickableYCoor, yCoordinate)
        # Obtain XY Coordinates of clickable Coordinates (End)
        start = strAttrib.find("[") + len(str(yCoordinate)) + len(str(xCoordinate)) + 3
        end = strAttrib.find(" '", start)
        temp = strAttrib[start:end]
        start = temp.find("[") + 1
        end = temp.find(",", start)
        eClickableXCoor = np.append(eClickableXCoor, int(temp[start:end]))
        start = temp.find(",") + 1
        end = temp.find("]", start)
        eClickableYCoor = np.append(eClickableYCoor, int(temp[start:end]))
        # Obtain package names
        start = strAttrib.find("'package': '") + 12
        end = strAttrib.find("'", start)
        package = strAttrib[start:end]
        # Obtain view names
        start = strAttrib.find("'class': '") + 10
        end = strAttrib.find("'", start)
        temp = strAttrib[start:end]
        temp = str(temp)
        view.append(temp)
        # Obtain resource id
        start = strAttrib.find("'resource-id': '") + 16
        end = strAttrib.find("'", start)
        temp = strAttrib[start:end]
        if temp == '':
            temp = '(No resource.id)'
            resourceId.append(temp)
        else:
            resourceId.append(temp)
        # Obtain text
        start = strAttrib.find("'text': '") + 9
        end = strAttrib.find("'", start)
        temp = strAttrib[start:end]
        # Text is empty
        if temp == '':
            temp = '(No text)'
            text.append(temp)
        else:
            text.append(temp)

        # Update cVisitFreq
        cVisitFreq.append(0)

        # Long clickable
        if condition2 in strAttrib:
            longClickable.append(str(True))
            longClickableIndex.append(longClickIndex)
            lcVisitFreq.append(0)
        else:
            longClickable.append(str(False))
        longClickIndex = longClickIndex + 1

    # scrollable
    if condition3 in strAttrib and enabledCondition in strAttrib:
        # Obtain Start XY Coordinates of scrollable views
        start = strAttrib.find("'bounds': '") + 12
        end = strAttrib.find('[', start)
        temp = strAttrib[start:end]
        start = temp.find("[") + 1
        end = temp.find(",", start)
        xCoordinate = int(temp[start:end])
        scrollableX.append(xCoordinate)
        start = temp.find(",") + 1
        end = temp.find("]", start)
        yCoordinate = int(temp[start:end])
        scrollableY.append(yCoordinate)
        # Obtain End XY Coordinates of scrollable views
        start = strAttrib.find("[") + len(str(yCoordinate)) + len(str(xCoordinate)) + 3
        end = strAttrib.find(" '", start)
        temp = strAttrib[start:end]
        start = temp.find("[") + 1
        end = temp.find(",", start)
        e_scrollableX.append(int(temp[start:end]))
        start = temp.find(",") + 1
        end = temp.find("]", start)
        e_scrollableY.append(int(temp[start:end]))
        # Obtain view names
        start = strAttrib.find("'class': '") + 10
        end = strAttrib.find("'", start)
        temp = strAttrib[start:end]
        temp = str(temp)
        scrollableView.append(temp)
        # Obtain resource id
        start = strAttrib.find("'resource-id': '") + 16
        end = strAttrib.find("'", start)
        temp = strAttrib[start:end]
        if temp == '':
            temp = '(No resource.id)'
            scrollableResourceId.append(temp)
        else:
            scrollableResourceId.append(temp)

# Logic used for scrolling/swiping
if len(scrollableX) >= 1:
    # Obtain center of scrollable views
    for n in range(len(scrollableX)):
        # X-Center coordinates
        temp = int(((e_scrollableX[n] - scrollableX[n]) / 2) + scrollableX[n])
        c_scrollableX.append(temp)
        # Y-Center coordinates
        temp = (((e_scrollableY[n] - scrollableY[n]) / 2) + scrollableY[n])
        c_scrollableY.append(temp)

# Use MD5 hashing to speed up state matching process
print("Hashed Hierarchy")
print(generateHashedHierachy(state1))

# Use MD5 hashing to speed up state matching process
print("Hashed state")
print(generateHashedState(state1))

# Clickable Views
print("Clickable views")
print(view)
print("\n")
print("Clickable package")
print(package)
print("\n")
print("Clickable resource-id")
print(resourceId)
print("\n")
print("Clickable text")
print(text)
print("\n")
print("Clickable XY coordinates (Top-left bounds)")
print(clickableXCoor)
print(clickableYCoor)
print("\n")
print("Clickable XY coordinates (bottom-right bounds)")
print(eClickableXCoor)
print(eClickableYCoor)
print("\n")
print("Clickable # of visits")
print(cVisitFreq)
print("\n")

# Long-clickable views
print("Long Clickable indexes")
# Refers XY coordinates of clickable views that are also long-clickable
print(longClickable)
# Refers to index of clickable XY coordinates that are also long-clickable
print(longClickableIndex)
print("\n")
print("Long-clickable # of visits")
print(lcVisitFreq)
print("\n")


print("Scrollable views Details")
# XY Coordinates of scrollable views (Top-left)
print(scrollableX)
print(scrollableY)
# XY Coordinates of scrollable views (Bottom-right)
print(e_scrollableX)
print(e_scrollableY)
# Xy Coordinates of scrollable views (Centre)
print(c_scrollableX)
print(c_scrollableY)
print("\n")
print("Scrollable view's name")
print(scrollableView)
print("\n")
print("Scrollable view's resource id")
print(scrollableResourceId)
print("\n")

# Tally of clickable, scrollable views (Limited to uiAutomator dump)
print("Tally:")
print("Number of clickable views:" + str(len(clickableXCoor)))
print("Number of scrollable views:" + str(len(scrollableX)))
count = 0
for i in longClickable:
    if i is str(True):
        count = count+1
print("Number of long-clickable views:" + str(count))

# Add your operations here:

