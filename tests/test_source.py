import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('KTN', 'KTN-NEWS', 'Home of News', 'https://ktn.co.ke', 'general', 'en', 'ke')

    def test_instance(self):
        '''
        Test to check if new_source instance exists
        '''
        self.assertTrue(isinstance(self.new_source,Source))
