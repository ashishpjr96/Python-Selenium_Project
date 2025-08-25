import time
import sys
import os



from pageObjects.homePage import homePage
from pageObjects.selectProduct import selectProduct

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))





def test_e2e(browserInstance):
    driver=browserInstance
    driver.get("https://www.flipkart.com/")
    home=homePage(driver)
    home.productSelection()
    productSelction=selectProduct(driver)
    productSelction.selectProd()





