from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def setup(request):
    url = "https://www.saucedemo.com/"

    chrome_options = webdriver.ChromeOptions()

    # CI-friendly options
    # chrome_options.add_argument("--headless=new")          # Latest headless mode
    chrome_options.add_argument("--no-sandbox")            # Required in GitHub Actions
    chrome_options.add_argument("--disable-dev-shm-usage") # Avoid limited /dev/shm errors
    chrome_options.add_argument("--disable-gpu")           # Disable GPU
    chrome_options.add_argument("--window-size=1920,1080") # Avoid mobile layout
    chrome_options.add_argument("--lang=en-IN")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("ignore-certificate-errors")
    chrome_options.add_argument("disable-notifications")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize ChromeDriver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)

    # Assign driver to test class
    if hasattr(request, "cls") and request.cls is not None:
        request.cls.driver = driver

    start_time = datetime.now()
    print(f"\n[Test Started at]: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    yield driver

    driver.quit()
