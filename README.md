# Introduction:<br> 
This project is designed to automate the login scenario of the LinkedIn mobile application using the Page Object Model (POM) design pattern using Appium and python. my focus on this design pattern helps reduce flakiness, enhance robustness, and simplify future expansions of the test suite. This README provides an overview of the project setup, design pattern benefits, and instructions for both iOS and Android environments. 

# Project Structure:<br>
* /test: Contains the test directory of both android and ios.
* /utils: Helper functions and utilities.
* /test_android: Contains the setup for android and PO model structure of
  * /pages: Contains the Page Object classes.
  * /config: Contains configuration files for android environment.
  and test files 
* /test_ios: Contains the setup for IOS and PO model structure of
  * /pages: Contains the Page Object classes.
  * /config: Contains configuration files for IOS environment.
  and test files 

# Why Page Object Model (POM):<br>
The Page Object Model is a design pattern that creates an abstraction layer between the test scripts and code for page-specific functionalities. This means each page will have its own class file, which serves as an interface to that page of the app.

# General setup: Please read the following documents to setup and launch the appium automation:<br>
* Readme_Android.md [test/test_android/Readme_Android.md](https://github.com/PriscillaStephan/appium-python-Mbition/blob/main/test/test_android/Readme_Android.md)
* Readme_Ios.md [test/test_ios/Readme_IOS.md](https://github.com/PriscillaStephan/appium-python-Mbition/blob/main/test/test_ios/Readme_IOS.md)
