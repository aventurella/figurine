import unittest
import context
import models
import figurine

class FigurineModelTestSuite(unittest.TestCase):

    def test_base_facebook(self):
        
        m = models.FacebookData()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.FacebookData)
        self.assertEqual(len(m.posts), 1)
        self.assertEqual(m.posts[0], 'facebook')

    def test_base_twitter(self):
        
        m = models.TwitterData()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.TwitterData)
        self.assertEqual(len(m.tweets), 1)
        self.assertEqual(m.tweets[0], 'twitter')

    def test_base_social_data(self):
        
        m = models.SocialData()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.SocialData)
        self.assertIsInstance(m, models.TwitterData)
        self.assertIsInstance(m, models.FacebookData)
        self.assertEqual(len(m.tweets), 1)
        self.assertEqual(m.tweets[0], 'twitter')
        self.assertEqual(len(m.posts), 1)
        self.assertEqual(m.posts[0], 'facebook')

    def test_simple_page(self):
        
        m = models.SimplePage()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.SimplePage)
        self.assertEqual(m.title, "")
        self.assertIsInstance(m.stylesheets, list)
        self.assertIsInstance(m.javascript, list)
        self.assertIsInstance(m.meta, dict)
        self.assertEqual(m.value, 1)

    def test_home_page(self):
        
        m = models.HomePage()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.HomePage)
        self.assertEqual(m.title, "")
        self.assertIsInstance(m.stylesheets, list)
        self.assertIsInstance(m.javascript, list)
        self.assertIsInstance(m.meta, dict)
        self.assertEqual(m.value, 1)
        self.assertEqual(m.username, "lucy_the_dog")


    def test_home_page_logged_in(self):
        
        m = models.HomePageLoggedIn()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.HomePageLoggedIn)
        self.assertEqual(m.title, "")
        self.assertIsInstance(m.stylesheets, list)
        self.assertIsInstance(m.javascript, list)
        self.assertIsInstance(m.meta, dict)
        self.assertEqual(m.value, 1)
        self.assertEqual(m.username, "lucy_the_dog")
        self.assertEqual(m.status, "logged in")


    def test_fancy_page(self):
        
        m = models.FancyPage()
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.FancyPage)
        
        self.assertIsInstance(m.stylesheets, list)
        self.assertIsInstance(m.javascript, list)
        self.assertIsInstance(m.meta, dict)
        self.assertEqual(m.value, 1)
        self.assertEqual(m.title, "fancy")
        self.assertEqual(m.username, "lucy_the_dog")
        self.assertEqual(m.status, "logged out")

        self.assertEqual(len(m.tweets), 2)
        self.assertEqual(m.tweets[0], 2)
        self.assertEqual(m.tweets[1], 3)
        
        self.assertEqual(len(m.posts), 2)
        self.assertEqual(m.posts[0], 1)
        self.assertEqual(m.posts[1], 2)


    def test_fancy_kwargs(self):
        m = models.FancyPage(title="fancy kwarg",
                             username="other",
                             status="bark!",
                             tweets=[9],
                             posts=[8],
                             stylesheets=['foo.css'],
                             value=22)
        
        self.assertIsInstance(m, figurine.base.FigurineModel)
        self.assertIsInstance(m, models.FancyPage)
        self.assertIsInstance(m, models.HomePageLoggedIn)
        self.assertIsInstance(m, models.HomePage)
        self.assertIsInstance(m, models.SimplePage)
        self.assertIsInstance(m, models.SocialData)
        self.assertIsInstance(m, models.TwitterData)
        self.assertIsInstance(m, models.FacebookData)
        
        self.assertIsInstance(m.stylesheets, list)
        self.assertIsInstance(m.javascript, list)
        self.assertIsInstance(m.meta, dict)
        self.assertEqual(m.value, 22)
        self.assertEqual(m.title, "fancy kwarg")
        self.assertEqual(m.username, "other")
        self.assertEqual(m.status, "bark!")

        self.assertEqual(len(m.tweets),1)
        self.assertEqual(m.tweets[0], 9)
        
        self.assertEqual(len(m.posts), 1)
        self.assertEqual(m.posts[0], 8)