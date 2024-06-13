import pytest
import time

from selenium.webdriver.common.by import By

from PageObjects.LoginPage import Login
from PageObjects.addNewCustomers import AddCustomers
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomers(self.driver)
        time.sleep(10)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.logger.info("@@@@@@Clicking add new button@@@@@@@")
        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        time.sleep(5)
        self.addcust.setEmail(self.email)
        time.sleep(5)
        self.addcust.setPassword("test123")
        time.sleep(5)
        self.addcust.setManagerOfVendor("Vendor 2")
        time.sleep(5)
        self.addcust.setGender("Female")
        time.sleep(5)
        self.addcust.setFirstName("Sumangala")
        time.sleep(5)
        self.addcust.setLastName("Dhali")
        time.sleep(5)
        self.addcust.setCustomerRoles("Registered")
        time.sleep(5)
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        time.sleep(5)
        self.addcust.setCompanyName("Msys")
        time.sleep(5)
        self.addcust.setAdminContent("This is for testing.........")
        time.sleep(5)
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))