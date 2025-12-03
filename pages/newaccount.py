import time

from selenium.webdriver.common.by import By
from utilities.baseutil import Base
from locators.amazon import Amazon

class NewAccountPage(Base):
    log = Base.getLogger()
    def login(self,email, password):
        time.sleep(5)
        self.sendText(Amazon.email_field,email)
        time.sleep(5)
        self.sendText(Amazon.password_field,password)
        self.click(Amazon.sign_in_btn)
        # time.sleep(5)
        # account_text = self.getText(Amazon.accountTxt)
        # self.log.info(f"captch page displayed successfully. Account element found:{account_text}")

