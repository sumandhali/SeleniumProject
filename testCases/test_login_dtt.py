import time

import pytest

from PageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLutils


class Test_002_DDT_Login:
    BaseURl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login1_ddt(self,setup):
        self.logger.info("Test_002_DDT_Login")
        self.driver = setup
        self.driver.get(self.BaseURl)
        self.lp = Login(self.driver)

        self.rows = XLutils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)

        list_status = []
        for r in range(2,self.rows+1):
            self.username = XLutils.readData(self.path,'Sheet1', r,1)
            self.password = XLutils.readData(self.path,'Sheet1', r,2)
            self.exp = XLutils.readData(self.path,'Sheet1',r,3)
            self.driver = setup
            self.driver.get(self.BaseURl)
            self.lp = Login(self.driver)
            self.lp.username(self.username)
            self.lp.password(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp == "Pass":
                    self.logger.info("Passed")
                    self.lp.logout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("failed")
                    self.lp.logout()
                    list_status.append("Fail")

            elif actual_title != expected_title:
                if self.exp == "Pass":
                    self.logger.info("Failed")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Passed")
                    list_status.append("pass")

        if "Fail" not in list_status:
            self.logger.info("Login DDT Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Failed")
            self.driver.close()
            assert False








