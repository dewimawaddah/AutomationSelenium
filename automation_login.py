from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_berhasil_login_dengan_email_terdaftar(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("testingqasanbercode@gmail.com")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("testing123")
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

    def test_gagal_login_dengan_email_tidak_terdaftar(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("testingqa@gmail.com")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("testing123")
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()