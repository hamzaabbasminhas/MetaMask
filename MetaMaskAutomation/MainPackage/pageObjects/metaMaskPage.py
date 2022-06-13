class MetaMaskPage:

    def __init__(self, driver):
        self.driver = driver

    _getStartedButton = '//button[text()="Get Started"]'
    _importWalletButton = '//button[text()="Import wallet"]'
    _noThanksButton = '//button[text()="No Thanks"]'
    _recoveryPhraseField = '//input[@id="import-srp__srp-word-0"]'
    _passwordField = '//input[@id="password"]'
    _confirmPasswordField = '//input[@id="confirm-password"]'
    _termsAndAgreementCheckBox = '//input[@id="create-new-vault__terms-checkbox"]'
    _importButton = '//button[text()="Import"]'
    _allDoneButton = '//button[text()="All Done"]'
    _crossButton = '//button[@title="Close"]'
    _EthereumMainnetButton = '//span[text()="Ethereum Mainnet"]'
    _showHideButton = '//a[text()="Show/hide"]'
    _testNetworkSwitch = '//div[@class="settings-page__content__modules"]//div[2]//div[7]//div[2]//div[1]//label[1]//div[1]//div[2]//div'

    def get_StartedButton(self):
        return self.driver.find_element_by_xpath(self._getStartedButton)

    def get_importWalletButton(self):
        return self.driver.find_element_by_xpath(self._importWalletButton)

    def get_noThanksButton(self):
        return self.driver.find_element_by_xpath(self._noThanksButton)

    def get_recoveryPhraseField(self):
        return self.driver.find_element_by_xpath(self._recoveryPhraseField)

    def get_passwordField(self):
        return self.driver.find_element_by_xpath(self._passwordField)

    def get_confirmPasswordField(self):
        return self.driver.find_element_by_xpath(self._confirmPasswordField)

    def get_termsAndAgreementCheckBox(self):
        return self.driver.find_element_by_xpath(self._termsAndAgreementCheckBox)

    def get_importButton(self):
        return self.driver.find_element_by_xpath(self._importButton)

    def get_allDoneButton(self):
        return self.driver.find_element_by_xpath(self._allDoneButton)

    def get_crossButton(self):
        return self.driver.find_element_by_xpath(self._crossButton)

    def get_EthereumMainnetButton(self):
        return self.driver.find_element_by_xpath(self._EthereumMainnetButton)

    def get_showHideButton(self):
        return self.driver.find_element_by_xpath(self._showHideButton)

    def get_testNetworkSwitch(self):
        return self.driver.find_element_by_xpath(self._testNetworkSwitch)
