Why we will use real devices with Linkedin app installed rather than similutors in the setup?
We need the trustable.apk file and .ipa , .apk file available in the internet has an issue and for .ipa we need Testflight or trustable sources to install in Apple

Pre requisite :<br>
_ **Install Java Latest version and set "JAVA_HOME" in environment variable**<br>
_ **Connect your iPhone**<br>
_ **Install Python latest version**<br>
_ **Install Pycharm IDE**<br> \* **Install the LinkedIn app in the Mobile**

# Xcode Setup for IOS automation in Real Device

#### Step-1: check brew is installed

First you need check brew is installed or not by using the following command on terminal

```
“brew doctor”
//output: “your system is ready to brew”
```

#### Step-2: Install brew if not installed

If not you need to install brew by entering it in your terminal or go to homebrew site and copy the command and paste it in your terminal
If it is showing permission denied enter **“sudo”** at the start

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)”
```

After installation complete repeat “Step-1” to verify brew installation

#### Step-3: Install Nodejs

1. Open Nodejs official site in browser then download and install
2. Install Nodejs using terminal

```
// install nodejs
brew install node
```

```
// check node version
node -v
```

```
//check npm version
npm -v
```

#### Step-4: Install and check “appium” version by using below command

```
//install appium
npm install -g appium
```

```
//check appium version
appium -v
```

#### Step-5 : Get XCode from AppStore

#### Step 6: Install XCode command line tools

Open terminal and run

```
xcode-select --install
```

#### Step 7: Create Apple ID

<pre>
1. Goto Xcode - settings - Accounts
2. Click + icon at the bottom
3. Select the Apple id and click Continue
4. Enter Apple mail id and password
5. Click Save button
6. In Accounts tab verify the apple mail id
</pre>

#### Step 8: Install Carthage

brew install Carthage<br>
Note : In order to launch WebDriverAgent, your macOS will need to have Carthage installed
(Not needed for automation on android)

#### Step 9: Navigate to WebDriverAgent project

1. In terminal enter


    ````
    which appium
    ```` to get the appium path

2. Appium path will look like "/opt/homebrew/bin/appium"
3. Copy the path from terminal, then replace "bin/appium" to "lib". path will look like "/opt/homebrew/lib/"
4. In terminal enter cd and paste the modified path like below

   ```
      // navigate to the lib directory
      cd /opt/homebrew/lib/

      // to open this folder in finder
      open .
   ```

5. In Finder icon then click node-modules/appium/node-Modules/appium-webriveragent or webdriveragent
6. Verify the “WebDriverAgent.xcodeproj” file inside the folder.
7. open terminal in the webdriveragent folder
8. Enter the below command
   ```
     mkdir -p Resources/WebDriverAgent.bundle
   ```
   Note: this commandworks after Carthage to be installed.

#### Step 10: Click WebDriverAgent.xcodeproj file

#### Step 11: Under the project in Xcode

1. click WebDriverAgent from project navigator panel
2. Under TARGETS option, below name will display
   - WebDriverAgentLib
   - WebDriverAgentRunner
   - IntegrationApp
3. Click **WebDriverAgentLib**
   - Click “Signing & Capabilities” tabs in Dashboard
   - Select checkbox for "Automatically manage signing"
   - select your Development Team under “Team”
   - Change the Bundle Identifier
   ```
   Syntax  : com.<unique-value>.WebDriverAgentLib
   Example : from "com.facebook.WebDriverAgentLib" to "com.testing.WebDriverAgentLib"
   ```
4. Click **WebDriverAgentRunner**
   - Click “Signing & Capabilities” tabs in Dashboard
   - Select checkbox for "Automatically manage signing"
   - select your Development Team under “Team”
   - Change the Bundle Identifier
     ```
     Syntax  : com.<unique-value>.WebDriverAgentRunner
     Example : from "com.facebook.WebDriverAgentRunner" to "com.testing.WebDriverAgentRunner"
     ```
5. Click **IntegrationApp**
   - Click “Signing & Capabilities” tabs in Dashboard
   - Select checkbox for "Automatically manage signing"
   - select your Development Team under “Team”
   - Change the Bundle Identifier
     ```
     Syntax  : com.<unique-value>.IntegrationApp
     Example : from "com.facebook.IntegrationApp" to "com.testing.IntegrationApp"
     ```
6. Now Click Product > Run, it will install **WebDriverAgent** app in your real device
7. In Finder icon then click node-modules/appium/node-Modules/appium-webriveragent or webdriveragent
8. Verify the “WebDriverAgent.xcodeproj” file inside the folder.
9. open terminal in the webdriveragent folder and enter below command

```
  //give id= your device udid
  xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id=<your-device-udid> test -allowProvisioningUpdates
```

# Appium Server and Appium Inspector installation Mac

1. Download Appium inspector from the official git repository https://github.com/appium/appium-inspector.git
2. Download Appium Server GUI from the official git repository https://github.com/appium/appium-desktop.git
3. Install both Appium inspector and Appium Server GUI in your machine.
4. Open Installed Appium Server
5. Click **Start the server** button, it will show your server running console
6. Now open Installed Appium inspector, enter below capabilities
   ```
   {
     "appium:platformVersion": "16.2",
     "appium:deviceName": "iPhone 8 Plus",
     "appium:udid": "<your-device-udid>",
     "platformName": "iOS"
   }
   ```
7. Click Start session button, In iphone device, Goto settings > General > VPN & Device management > click trust for **Integration App**
8. Connected Device Screen will display in Appium inspector.<br>
   Note: Using Appium Inspector, we can get the locators of the element we want to perform actions in automation
9. After finish getting locators, you can close the Appium Inspector.

# IOS Automation using Pycharm

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
3. After Installation, Navigate to **test/test_ios/conftest.py** file and you will able to see the below code line
   ```
     caps = {"appium:platformVersion": "16.2", "appium:deviceName": "iPhone 8 Plus",
          "appium:udid": "<device-udid>", "platformName": "iOS",
          "appium:app": "com.in.LinkedIn", "appium:includeSafariInWebviews": True,
          "appium:newCommandTimeout": 3600, "appium:connectHardwareKeyboard": True}
   ```
4. Change the platformName, deviceName, osVersion values corresponding to the connected device
5. Navigate to **test/test_ios/** folder.
6. Open **linkedIn_login_ios_test.py**.
7. Click the green color Play icon in the script screen and select **Run** option
8. Execution will start, and you can see the connected device is getting automate
9. Follow the below step to run via Terminal
   - Open command prompt from the project root folder
   - enter the below command
     ```
      pytest test/test_ios/linkedIn_login_ios_test.py
     ```
10. Execution will start and connected device will automate
