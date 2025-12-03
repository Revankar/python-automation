from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def setup(request):

    url = "https://www.amazon.in/"

    chrome_option = Options()

    # Required for GitHub Actions Linux headless execution
    # chrome_option.add_argument("--headless=new")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    chrome_option.add_argument("--disable-gpu")
    chrome_option.add_argument("--window-size=1920,1080")

    # Chrome + ChromeDriver will be auto-detected
    driver = webdriver.Chrome(options=chrome_option)

    driver.implicitly_wait(20)
    driver.get(url)

    # Assign driver to class
    if hasattr(request, "cls") and request.cls is not None:
        request.cls.driver = driver

    print("\n[Test Started at]:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    yield driver
    driver.quit()
