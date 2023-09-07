import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DragDropTest(unittest.TestCase):
    """DragDropTest"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://the-internet.herokuapp.com/drag_and_drop'
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)


    def test_drag_drop_a(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        actions = ActionChains(driver)
        time.sleep(2)
        box_a = driver.find_element(By.ID, "column-a")
        self.assertTrue(box_a)
        time.sleep(2)
        box_b = driver.find_element(By.ID, "column-b")
        self.assertTrue(box_b)
        time.sleep(2)
        actions.click_and_hold(box_a).move_by_offset(150,0).release().perform()
        self.assertTrue(box_a.get_attribute("header").text, "B")
        driver.save_screenshot("drag_drop_success.png")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
