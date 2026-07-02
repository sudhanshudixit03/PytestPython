from .dashboard import DashboardPage


class LoginPage:

    def __init__(self,page):                         #for using extra objects in the class we use constructor
        self.page = page

    def navigate(self):
        self.page.goto("https://www.rahulshettyacademy.com/client")




    def login(self,userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.fill("#userPassword", userPassword)
        self.page.click("#login")
        dashboardPage = DashboardPage(self.page)
        return dashboardPage