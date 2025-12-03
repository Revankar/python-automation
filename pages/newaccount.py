import time

from utilities.baseutil import Base
from locators.amazon import Amazon

class NewAccountPage(Base):
    log = Base.getLogger()
    def login(self,email, password):
        time.sleep(5)
        try:
            self.driver.find_element(By.ID, "sp-cc-accept").click()
        except:
            pass
        self.click(Amazon.sign_in_btn)
        self.clearAndSendText(Amazon.email_field,email)
        self.click(Amazon.continue_btn)
        self.sendText(Amazon.password_field,password)
        self.click(Amazon.submit)
        time.sleep(5)
        account_text = self.getText(Amazon.accountTxt)
        self.log.info(f"captch page displayed successfully. Account element found:{account_text}")

