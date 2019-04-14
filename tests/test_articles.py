import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Christine', 'Kenyan Foods', 'The variety and rich culture that exists in Kenyan cuisines', 'https://ktn.co.ke', 'https://ktn.co.ke/image1', '24/06/2012', 'kenyan food is the best')

    def test_instance(self):
        '''
        Test to check if new_Article instance exists
        '''
        self.assertTrue(isinstance(self.new_article,Article))
