import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
BASE='http://127.0.0.1:5000'
@pytest.fixture
def driver():
    opts=Options()
    opts.add_argument('--window-size=1280,900')
    browser=webdriver.Chrome(options=opts)
    yield browser
    browser.quit()
