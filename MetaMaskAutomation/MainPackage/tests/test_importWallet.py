import time

import pytest
from selenium.webdriver.common.keys import Keys
import pyperclip
import MainPackage.utilities.customLogger as cl
from MainPackage.pageObjects.metaMaskPage import MetaMaskPage
from MainPackage.utilities.BaseClass import BaseClass
from MainPackage.utilities.Data import Data
from MainPackage.helper.helperclass import HelperClass


class Test_importWallet(BaseClass):

    @pytest.fixture(autouse="true")
    def classObjects(self):
        cl.allureLogs("Check Price of Cart Test Started")
        self.hp = HelperClass(self.driver)
        self.log = cl.customLogger()
        self.mp = MetaMaskPage(self.driver)
        self.da = Data()

    def test_importWallet(self):

        try:
            cl.allureLogs("Test Started")
            self.log.info("Get All Window Handles")
            main_window = self.driver.window_handles[0]
            new_window = self.driver.window_handles[1]

            self.driver.switch_to.window(new_window)

            self.log.info("Close Extra Tab")
            self.driver.close()

            self.log.info("Switch Control to MetaMask Tab")
            self.driver.switch_to.window(main_window)

            self.log.info("Click on Get Started Button")
            self.hp.click(self.mp.get_StartedButton())

            self.log.info("Click On Import Wallet Button")
            self.hp.click(self.mp.get_importWalletButton())

            self.log.info("Click on No thanks Button")
            self.hp.click(self.mp.get_noThanksButton())

            inputData = self.da.getTestData("TC1")

            self.log.info("Copy Recovery Phase to clipboard")
            pyperclip.copy(inputData[0]["Recover Phrase"])

            self.log.info("Paste The recovery phrase in recovery phrase field")
            self.hp.send_keys(self.mp.get_recoveryPhraseField(), Keys.COMMAND + "v")

            self.log.info("Enter Password in password field")
            self.hp.send_keys(self.mp.get_passwordField(), inputData[0]["Password"])

            self.log.info("Enter Password in confirm password field")
            self.hp.send_keys(self.mp.get_confirmPasswordField(), inputData[0]["Password"])

            self.log.info("Accept Terms and Conditions")
            self.hp.click(self.mp.get_termsAndAgreementCheckBox())

            self.log.info("Click on Import Button")
            self.hp.click(self.mp.get_importButton())

            self.log.info("Click on All done Button")
            self.hp.click(self.mp.get_allDoneButton())

            self.log.info("Click on cross button of popover")
            try:
                self.hp.click(self.mp.get_crossButton())
            except:
                self.hp.click(self.mp.get_crossButton())

            self.log.info("Click On Ethereum Mainnet button")
            self.hp.click(self.mp.get_EthereumMainnetButton())

            self.log.info("Click on Show/Hide Button")
            self.hp.click(self.mp.get_showHideButton())

            self.log.info("Turn on Test Network Switch")
            self.hp.click(self.mp.get_testNetworkSwitch())

            cl.allureLogs("Test Finished")

        except Exception as e:
            time.sleep(2)
            self.log.info("Take screenshot of failed scenario")

            self.takeScreenshot()
            cl.allureLogs("Error occurred in Verifying order creation test")

            self.log.info(str(e))
            self.assertTrue(False, "Test Case Failed")
