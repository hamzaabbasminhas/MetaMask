![Meta_Automation](https://user-images.githubusercontent.com/64031981/173302919-b92c8d86-81eb-4f82-9774-1241cb7feb66.gif)


* Framework is built using Selenium with python
* This is Platform independent Framework. (It should run on Windows, Mac or linux)
* Tests will run and pass in Chrome browser only condition is you should be using the latest chrome version on your PC.
* It is build with page object model
* Helper methods are implemented for page interactions like click, sendkeys.
* Built in according to data driven testing principles i.e all data is extracted from external source and can run on multiple test scenarios

To run the project

1. Clone this repo
2. Navigate to root folder
3. pip3 install -r requirements.txt


4. To run test cases
   py.test --alluredir=./MainPackage/reports

5. To view reports
   allure serve <Path to root Folder>/MetaMaskAutomation/MainPackage/reports
