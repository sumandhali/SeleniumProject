import time
import pytest
from PageObjects.LoginPage import Login
from PageObjects.productsearch import SearchProduct
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

@pytest.mark.regression
class Test_SearchCustomerByName_006:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_searchProductsByName(self,setup):
        self.logger.info("************* SearchCustomerByEmail_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Product By Name **********")
        addpro = SearchProduct(self.driver)
        time.sleep(10)
        addpro.clickOnCatalogMenu()
        time.sleep(10)
        addpro.clickOnCatalogMenuItems()
        time.sleep(5)

        self.logger.info("************* searching products by name **********")
        addpro.setProductName("Apple MacBook Pro 13-inch")
        addpro.clickSearch()
        time.sleep(10)
        status=addpro.searchProductsbyName("Apple MacBook Pro 13-inch")
        self.driver.close()
        assert True== status