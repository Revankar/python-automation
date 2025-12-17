from selenium.webdriver.common.by import By


class Amazon:
    sign_in_btn = (By.ID,"login-button")
    email_field = (By.XPATH,"//input[@name='user-name']")
    password_field = (By.XPATH,"//input[@name='password']")
    alert = (By.XPATH,"//div[@class='oxd-alert-action']//preceding::p")

    addtocart = (By.XPATH,"(//button[text()='Add to cart'])[1]")
    cartlink = (By.XPATH,'//a[@class="shopping_cart_link"]')
    checkout = (By.ID,"checkout")
    firstname = (By.ID,"first-name")
    lastname = (By.ID,"last-name")
    zipcode = (By.ID,"postal-code")
    continuebtn = (By.ID,'continue')
    finish = (By.ID,'finish')
    backbtn = (By.ID,'back-to-products')





