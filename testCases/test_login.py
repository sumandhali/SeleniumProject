import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class Test_001:
    BaseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.BaseURl)
        self.actual_title = self.driver.title
        self.logger.info(f"title--->{self.actual_title}")

        if self.actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Test Case Passed!")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("TestCase Failed!")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login1(self,setup):
        self.driver = setup
        self.driver.get(self.BaseURl)
        self.lp = Login(self.driver)
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.clickLogin()
        self.actual_title = self.driver.title
        self.logger.info(f"title--->{self.actual_title}")

        if self.actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("Test Case Passed!")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login1.png")
            self.logger.info("TestCase Failed!")
            self.driver.close()
            self.logger.info("TestCase Failed!")
            assert False

