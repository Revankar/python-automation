import pytest
from pages.newaccount import NewAccountPage

class TestAmazon(NewAccountPage):

    @pytest.mark.smoke
    def test_login_invalidcredential(self):
        self.login_invalidcredential(email="vidyarevankar22@gmail.com",password='dont know')

    @pytest.mark.regression
    def test_login_addadmin(self):
        self.login_validcredential1(email="standard_user",password='secret_sauce')
        self.add_itemtocart()

    @pytest.mark.regression
    def test_login_validcredential(self):
        self.login_validcredential(email="standard_user",password='secret_sauce')

    @pytest.mark.regression
    def test_login_validcredential1(self):
        self.login_validcredential1(email="Admin",password='admin123')

    @pytest.mark.sanity
    def test_login_checkalert(self):
        self.login_validcredential(email="Admin", password='admin123')

