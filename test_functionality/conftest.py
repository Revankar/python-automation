from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from datetime import datetime


@pytest.fixture
def setup(request):
    url = "https://www.amazon.in/"

    chrome_option = webdriver.ChromeOptions()

    # Required for CI environments
    chrome_option.add_argument("--headless=new")  # Headless mode
    chrome_option.add_argument("--no-sandbox")  # Disable sandbox
    chrome_option.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
    chrome_option.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_option.add_argument("--window-size=1920,1080")
    chrome_option.add_argument("--lang=en-IN")
    chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_option.add_experimental_option("useAutomationExtension", False)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_option)
    driver.implicitly_wait(10)
    driver.get(url)

    # Assign driver to test class
    if hasattr(request, "cls") and request.cls is not None:
        request.cls.driver = driver

    start_time = datetime.now()
    print(f"\n[Test Started at]: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    yield driver

    driver.quit()
