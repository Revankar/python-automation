import pytest
from pages.newaccount import NewAccountPage

class TestAmazon(NewAccountPage):

    def test_login_invalidcredential(self):
        self.login_invalidcredential(email="vidyarevankar22@gmail.com",password='dont know')

    def test_login_validcredential(self):
        self.login_validcredential(email="Admin",password='admin123')

    def test_login_validcredential1(self):
        self.login_validcredential1(email="Admin",password='admin123')

    def test_login_checkalert(self):
        self.login_validcredential(email="Admin", password='admin123')

