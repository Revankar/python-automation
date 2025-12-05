import pytest
from pages.newaccount import NewAccountPage

class TestAmazon(NewAccountPage):

    @pytest.mark.p1
    def test_login_invalidcredential(self):
        self.login_invalidcredential(email="vidyarevankar22@gmail.com",password='dont know')

    @pytest.mark.p2
    def test_login_validcredential(self):
        self.login_validcredential(email="Admin",password='admin123')

    @pytest.mark.p3
    def test_login_checkalert(self):
        self.login_validcredential(email="Admin", password='admin123')

