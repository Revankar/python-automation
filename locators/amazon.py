from selenium.webdriver.common.by import By


class Amazon:
    sign_in_btn = (By.XPATH,"//button[@type='submit']")
    email_field = (By.XPATH,"//input[@name='username']")
    password_field = (By.XPATH,"//input[@name='password']")
    alert = (By.XPATH,"//div[@class='oxd-alert-action']//preceding::p")




