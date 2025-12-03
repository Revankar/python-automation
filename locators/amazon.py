from selenium.webdriver.common.by import By


class Amazon:
    sign_in_btn = (By.ID,"nav-link-accountList")
    email_field = (By.ID, "ap_email_login")
    continue_btn = (By.ID, "continue")
    password_field = (By.ID, "ap_password")
    submit = (By.ID, "signInSubmit")
    accountTxt = (By.ID, "aacb-captcha-header")




