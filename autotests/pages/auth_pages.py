from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    def __init__(self,driver): self.driver=driver
    def open(self,route):self.driver.get('http://127.0.0.1:5000'+route);return self
    def fill(self,**values):
        for name,value in values.items():
            field=self.driver.find_element(By.NAME,name);field.clear();field.send_keys(value)
        return self
    def submit(self):self.driver.find_element(By.CSS_SELECTOR,'button[type=submit]').click();return self
    def has_text(self,text):return text in self.driver.page_source
    def wait_text(self,text):
        WebDriverWait(self.driver,7).until(lambda d:text in d.page_source)
        return True
