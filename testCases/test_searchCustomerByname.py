import time
import pytest
from PageObjects.LoginPage import Login
from PageObjects.addNewCustomers import AddCustomers
from PageObjects.searchcustomers import SearchCustomer
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Username **********")
        self.addcust = AddCustomers(self.driver)
        time.sleep(10)
        self.addcust.clickOnCustomersMenu()
        time.sleep(10)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(5)

        self.logger.info("************* searching customer by Username **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(10)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByname_005 Finished  *********** ")