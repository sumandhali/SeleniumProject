from selenium.webdriver.common.by import By


class SearchProduct:
    lnkCatalog_menu_xpath = "//i[@class='nav-icon fas fa-book']"
    lnkProducts_menuitem_xpath = "//a[@href='/Admin/Product/List']//p[contains(text(),'Products')]"
    txtProduct_id = "SearchProductName"
    btnSearch_id = "search-products"
    table_Xpath = "//table[@id='products-grid']"
    tableRows_xpath = "//table[@id='products-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='products-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCatalogMenu(self):
        action = self.driver.find_element(By.XPATH, self.lnkCatalog_menu_xpath)
        action.click()
    def clickOnCatalogMenuItems(self):
        action=self.driver.find_element(By.XPATH, self.lnkProducts_menuitem_xpath)
        action.click()

    def setProductName(self, name):
        self.driver.find_element(By.ID,self.txtProduct_id).clear()
        self.driver.find_element(By.ID,self.txtProduct_id).send_keys(name)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchProductsbyName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH,self.table_Xpath)
            productId = table.find_element(By.XPATH,"//table[@id='products-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if productId == name:
                flag = True
                break
        return flag
