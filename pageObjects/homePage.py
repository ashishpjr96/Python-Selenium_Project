
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class homePage:


   def __init__(self,driver):
      self.driver=driver
      self.mouseAction=(By.XPATH, "//div[@aria-label='Fashion']")
      self.productList=(By.XPATH, "//a[contains(@class,'_1BJVlg')]")




   def productSelection(self):
      actions = ActionChains(self.driver)
      actions.move_to_element(self.driver.find_element(*self.mouseAction)).perform()
      products = self.driver.find_elements(*self.productList)
      for product in products:
         if product.text == "Men Footwear":
            product.click()
            clicked = True
            break


