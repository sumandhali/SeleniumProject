from selenium.webdriver.common.by import By

class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def username(self,username):
        textbox = self.driver.find_element(By.ID, self.textbox_username_id)
        textbox.clear()
        textbox.send_keys(username)

    def password(self,password):
        textbox = self.driver.find_element(By.ID, self.textbox_password_id)
        textbox.clear()
        textbox.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

