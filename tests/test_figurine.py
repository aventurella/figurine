import unittest
import context
import models

class FigurineModelTestSuite(unittest.TestCase):

    # def test_base_model(self):
        
    #     m = models.SimplePage()
    #     print('SimplePage: ', m)
    # #     self.assertEqual(m.title, "")
    # #     self.assertIsInstance(m.stylesheets, list)
    # #     self.assertIsInstance(m.javascript, list)
    # #     self.assertIsInstance(m.meta, dict)
    # #     self.assertEqual(m.value, 1)

    def test_base_model_3(self):
        
        m = models.HomePageLoggedIn()
        print('HomePageLoggedIn: ', m)
        # self.assertEqual(m.title, "")
        # self.assertIsInstance(m.stylesheets, list)
        # self.assertIsInstance(m.javascript, list)
        # self.assertIsInstance(m.meta, dict)
        # self.assertEqual(m.value, 1)

    # def test_base_model_inheritance(self):
    #     m = models.HomePage()
    #     print('HomePage: ', m)
    # #     # # Base tests
    # #     # self.assertEqual(m.title, "")
    # #     # self.assertIsInstance(m.stylesheets, list)
    # #     # self.assertIsInstance(m.javascript, list)
    # #     # self.assertIsInstance(m.meta, dict)
    # #     # self.assertEqual(m.value, 1)

    # #     # # HomePage Tests
    # #     # self.assertIsInstance(m.tweets, list)
    # #     # self.assertEqual(m.username, "lucy_the_dog")