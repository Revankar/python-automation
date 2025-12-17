import time

from selenium.webdriver.common.by import By
from utilities.baseutil import Base
from locators.amazon import Amazon

class NewAccountPage(Base):
    log = Base.getLogger()


    def login_invalidcredential(self,email, password):
        time.sleep(5)
        self.sendText(Amazon.email_field,email)
        time.sleep(5)
        self.sendText(Amazon.password_field,password)
        self.click(Amazon.sign_in_btn)
        alert = self.getText(Amazon.alert)
        self.log.info(f"alert message:{alert}.")

    def add_itemtocart(self):
        self.click(Amazon.addtocart)
        self.click(Amazon.cartlink)
        self.click(Amazon.checkout)
        self.sendText(Amazon.firstname,'test')
        self.sendText(Amazon.lastname,'test')
        self.sendText(Amazon.zipcode,'560017')
        self.click(Amazon.continuebtn)
        self.click(Amazon.finish)
        self.click(Amazon.backbtn)



    def login_validcredential(self,email,password):
        time.sleep(5)
        self.sendText(Amazon.email_field, email)
        time.sleep(5)
        self.sendText(Amazon.password_field, password)
        self.click(Amazon.sign_in_btn)
        self.log.info(f"signed in successfully.")

    def login_validcredential1(self,email,password):
        time.sleep(5)
        self.sendText(Amazon.email_field, email)
        time.sleep(5)
        self.sendText(Amazon.password_field, password)
        self.click(Amazon.sign_in_btn)
        self.driver.switch_to.alert.accept()
        self.log.info(f"signed in successfully.")

    def login_checkalert(self,email,password):
        time.sleep(5)
        self.sendText(Amazon.email_field, email)
        time.sleep(5)
        self.sendText(Amazon.password_field, password)
        self.click(Amazon.sign_in_btn)
        try:
            self.driver.switch_to.alert.accept()
        except:
            self.log.info(f"No alerts..")
