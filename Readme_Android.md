Why we will use real devices with Linkedin app installed rather than similutors in the setup?
We need the trustable.apk file and .ipa , .apk file available in the internet has an issue and for .ipa we need Testflight or trustable sources to install in Apple

Pre requisite :<br>

- **Install Java Latest version and set "JAVA_HOME" in environment variable**<br>
- **Connect your Android mobile**<br>
- **Install Python latest version and pip latest version**<br>
- **Install Pycharm IDE**<br>
- **Extract Android-Sdk Zip folder**<br>
- **In connected Android mobile enable the following options**
  - **goto settings > Developer option > Enable "_USB Debugger_"**
  - **goto settings > Developer option > Enable "_Disable Permission monitoring_"**
  - **Install the LinkedIn app in the Mobile**

# Android SDK download and setup

- download the Android Studio and setup - https://developer.android.com/studio

# Appium Server and Appium Inspector installation Android

1. Download Appium inspector from the official git repository https://github.com/appium/appium-inspector.git
2. Download Appium Server GUI from the official git repository https://github.com/appium/appium-desktop.git
3. Install both Appium inspector and Appium Server GUI in your machine.
4. Open Installed Appium Server
5. Click **Start the server** button, it will show your server running console
6. Now open Installed Appium inspector, enter **/wd/hub** in **Remote Path** field
7. In **Desired Capabilities** tab, click edit icon in **JSON Representation**
8. Enter below capabilities in Desired Capabilities tab
   ```
   {
     "appium:platformVersion": "12",
     "appium:deviceName": "Samsung J7",
     "platformName": "android"
   }
   ```
9. Click Start session button
10. Connected Device Screen will display in Appium inspector.<br>
    **Note**: Using Appium Inspector, we can get the locators of the element we want to perform actions in automation
11. After finish getting locators, you can close the Appium Inspector.

# Android Automation using Pycharm

### Step 1 : Open Project in Pycharm IDE

1. Extract the project in your machine
2. Open Pycharm IDE, Click File > open. it will open the file explorer pop-up
3. In Opened File explorer pop-up, Navigate to your extracted project
4. Select Project root folder
5. Click Open button. It will open the project in Pycharm IDE.

### Step 2: Install required Libraries

1. Open **Terminal** in Pycharm IDE.
2. Enter the below command
   ```
   // it will install packages mentioned in the file
   pip install -r requirements. txt
   //or
   pip3 install -r requirements.txt
   ```
3. After Installation, Navigate to **test/test_android/conftest.py** file and you will able to see the below code line
   ```
     dc = {'platformName': 'android', 'deviceName': 'Nokia G20', 'osVersion': '12'}
   ```
4. Change the platformName, deviceName, osVersion values corresponding to the connected device
5. Then, Navigate to **test/test_android/** folder.
6. Open **linkedIn_login_android_test.py**.
7. Click the green color Play icon in the script screen and select **Run** option
8. Execution will start, and you can see the connected device is getting automate
9. Follow the below step to run via Terminal
   - Open command prompt from the project root folder
   - enter the below command
     ```
      pytest test/test_android/linkedIn_login_android_test.py
     ```
10. Execution will start and connected device will automate
