import figurine

class FacebookData(figurine.Model):
    def __init__(self):
        self.posts = ['facebook']

class TwitterData(figurine.Model):
    def __init__(self):
            self.tweets = ['twitter']

class SocialData(FacebookData, TwitterData):
    pass

class SimplePage(figurine.Model):
    
    def __init__(self):
        self.title = ""
        self.stylesheets = []
        self.javascript = []
        self.meta = {}
        self.value = 1

class HomePage(SimplePage, SocialData):
    
    def __init__(self):
        self.username = "lucy_the_dog"


class HomePageLoggedIn(HomePage):
    
    def __init__(self):
        self.status = "logged in"


class FancyPage(HomePageLoggedIn):
    
    def __init__(self):
        self.status = "logged out"
        self.posts = [1,2]
        self.tweets = [2,3]
        self.javascript = ['jquery']
        self.title = "fancy"