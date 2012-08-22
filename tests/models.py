from figurine import Model

class SocialData(Model):
    def __init__(self):
        print('social')
        self.tweets = ['1']

class SimplePage(Model):
    
    def __init__(self):
        print('simple')
        self.title = ""
        self.stylesheets = []
        self.javascript = []
        self.meta = {}
        self.value = 1

class HomePage(SimplePage, SocialData):
    
    def __init__(self):
        print('home')
        self.username = "lucy_the_dog"


class HomePageLoggedIn(HomePage):
    
    def __init__(self):
        print('loggedin')
        self.status = "logged in"
        self.tweets = [3]