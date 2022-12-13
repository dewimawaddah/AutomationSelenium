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
        respon_welcome = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, 'Welcome QAsanbercode')
        self.assertEqual(respon_berhasil, 'Anda Berhasil Login')

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
        respon_berhasil = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_berhasil, 'Email atau Password Anda Salah')

    def test_gagal_login_dengan_email_password_tidak_diisi(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)
        respon_berhasil = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_berhasil, 'Email atau Password Anda Salah')

    def test_gagal_login_email_terdaftar_password_salah(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("testingqasanbercode@gmail.com")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("testing546")
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)
        respon_berhasil = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_berhasil, 'Email atau Password Anda Salah')

    def test_gagal_login_email_salah_password_benar(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("qatesting77@gmail.com")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("testing123")
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)
        respon_berhasil = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_berhasil, 'Email atau Password Anda Salah')

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()