![Meta_Automation](https://user-images.githubusercontent.com/64031981/173302919-b92c8d86-81eb-4f82-9774-1241cb7feb66.gif)


* Framework is built using Selenium with Python Language.
* This is a Platform independent Framework. (It should run on Windows, Mac, or Linux)
* Tests will run and pass in the Chrome browser, only condition is you should be using the latest chrome version on your PC.
* The framework is built with the page object model i.e a design pattern, in which an Object Repository contains all web UI elements
* Helper methods are implemented in a separate class for all kinds of page interactions like click, sendkeys.
* Built according to data-driven testing principles i.e all data is extracted from an external source and can run on multiple test scenarios. All testdata is present inside the resource module in the project.
* For reporting allure-reporting tool is used. A report is generated in reports module inside the project after the test execution is completed
* Proper logging and screenshot on failure mechanism is implemented. Each step while the test runs is logged and logs and screenshots are then integrated with the reports.
* This project contains automation of importing wallet in MetaMask extension. The test first installs MetaMask extension to the driver instance of chrome and afterward imports Metamask wallet successfully. The GIF, at the top shows the video of the code execution.


**To run the project**

1. Clone this repo
2. Navigate to root folder i.e to the MetaMaskAutomation Folder
3. brew install allure
4. pip3 install -r requirements.txt


5. To run test cases
   py.test --alluredir=./MainPackage/reports

7. To view reports
   allure serve /*Path to root Folder*/MetaMaskAutomation/MainPackage/reports

