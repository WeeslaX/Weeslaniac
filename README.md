# Weeslaniac Fuzzing Tool


## Description
**Weeslaniac** is a pure python based script that uses both static and dynamic weighted random selection algorithm to fuzz an android application's GUI to primarily detect crashes and potentially other GUI related vulerabilities.


## Features

- Compatible only with **Android** devices and emulators.
- Compatible with any OS that can run Python.
- Crash detection and continuation capabilities. 
- Outputs a python script that replicates all actions performed by the fuzzing tool for crash analysis.
- Takes screenshot of unique screen states for crash analysis.


## Pre-requisites

Required:
- [Python 2.7](https://www.python.org/downloads/release/python-2713/)
- [SDK Tools](https://developer.android.com/studio/)

Recommended Emulator:
- [Genymotion](https://www.genymotion.com/)


## Installation

### SDK Tools

Create an environment variable **ANDROID_HOME** (Full Path to: ..\SDK\platform-tools) and add it to **PATH**.
[(Guide)](https://www.360logica.com/blog/how-to-set-path-environmental-variable-for-sdk-in-windows/)



### Essential Libraries

These libraries can be downloaded using the package manager [pip](https://pip.pypa.io/en/stable/):

```bash
pip install uiautomator
```

The list of libraries that requires installation (if not already done so) are as follows:

```
1. uiautomator
2. numpy
```


## Usage

1. Start the device/emulator. 
- Ensure that the target App is installed and can be seen on the device's screen
- Virtual keyboard is turned on (for emulator).

2. Download and run the script on the OS Terminal.

```bash
weeslaniac.py
```

3. A "Settings" pop-up will be displayed:

- "App Name" refers to the target app to be tested. (A unique substring of the app name required)
- "# of actions" refers to the maximum number of actions (Eg: click, swipe, etc) before the testing terminates.
- "Device" refers to the target device's name that is currently connected. You can check the device name using:
```bash
adb devices
```
- "Screenshot Location" refers to the location where screenshots that are taken during fuzzing are saved.
- "test_case.py Location" refers to the location where the output python script will be saved.

4. Select "Save" to start fuzzing.


## Future Enhancements (In order of priorities)

- Adding more user options to the "Settings" pop-up box, such as UI event percentage and customized input text.
- Simple Terminal interface that provides all the neccessary tools to manage and run the fuzzing tool.
- Mutator_W: Run through test case once (store hashed version) before commencing mutation testing. 
- Implement drag capability.
- Allows interaction with 3rd party apps.
- Explore account registration capabilities.
