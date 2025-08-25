import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class selectProduct:


    def __init__(self,driver):
        self.driver=driver
        self.MenSneaker=(By.XPATH, "//a[text()='Sneakers For Men']")
        self.verifyLogin=(By.XPATH, "//*[@class='wsejfv']")


    def selectProd(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.MenSneaker)).click()
        time.sleep(3)
        msg = self.driver.find_element(*self.verifyLogin).text
        assert 'Login' in msg
