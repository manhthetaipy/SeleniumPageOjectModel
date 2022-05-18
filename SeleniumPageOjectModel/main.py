import unittest
from selenium import webdriver
import page
import time
from lib2to3.pgen2 import driver



class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
        executable_path='C:/Users/Mr Hip/Desktop/TestCase/page-object-model-selenium-python-master/chromedriver.exe')
        self.driver.get("http://www.python.org")
        time.sleep(2)

    def test_search_in_python_org(self):
        main_page = page.MainPage(self.driver)
        time.sleep(2)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        time.sleep(2)




if __name__ == "__main__":
    unittest.main()
