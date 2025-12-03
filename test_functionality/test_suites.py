from pages.newaccount import NewAccountPage

class TestAmazon(NewAccountPage):
    def test_login(self):
        self.login(email="vidyarevankar22@gmail.com",password='dont know')

