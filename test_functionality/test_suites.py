import pytest
from pages.newaccount import NewAccountPage

class TestAmazon(NewAccountPage):

    @pytest.mark.regression
    def test_login_invalidcredential_facebook(self):
        self.login_invalidcredential(email="vidyarevankar22@gmail.com",password='dont know')

    @pytest.mark.regression
    def test_login_addadmin_facebook(self):
        self.login_validcredential1(email="standard_user",password='secret_sauce')
        self.add_itemtocart()

    @pytest.mark.regression
    def test_login_validcredential_instagram(self):
        self.login_validcredential(email="standard_user",password='secret_sauce')

    @pytest.mark.regression
    def test_login_validcredential1_instagram(self):
        self.login_validcredential1(email="Admin",password='admin123')

    @pytest.mark.regression
    def test_login_checkalert_instagram(self):
        self.login_validcredential(email="Admin", password='admin123')

    @pytest.mark.regression
    def test_login_addadmin_instagram(self):
        self.login_validcredential1(email="standard_user",password='secret_sauce')
        self.add_itemtocart()

