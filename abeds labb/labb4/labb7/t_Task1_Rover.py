'''
    Student shall write their names here
        1. Student 1
        2. Student 2
'''

import unittest
from Task1_Rover import rovar

class test_string( unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
        _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    
    def setUp(self):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        self.rv = rovar()

    # Example test case to check lower case rover
    def test_enrove_small(self):
       self.assertEqual(self.rv.enrove('b'), 'bob')

    # You can continue writing your test cases here based on the assignment description

    def test_enrove_null(self):
        self.assertIsNone(self.rv.enrove(None))

    def test_enrove_empty(self):
        self.assertEqual(self.rv.enrove(''), '')

    def test_enrove_lower_constants(self):
        self.assertEqual(self.rv.enrove('bcdfghjklmnpqrstvwxz'), 'bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz')
    
    def test_enrove_upper_constants(self):
        self.assertEqual(self.rv.enrove('BCDFGHJKLMNPQRSTVWXZ'), 'BOBCOCDODFOFGOGHOHJOJKOKLOLMOMNONPOPQOQRORSOSTOTVOVWOWXOXZOZ')
    
    def test_enrove_lower_vowels(self):
        self.assertEqual(self.rv.enrove('aeiouyåäö'), 'aeiouyåäö')

    def test_enrove_upper_vowels(self):
        self.assertEqual(self.rv.enrove('AEIOUYÅÄÖ'), 'AEIOUYÅÄÖ')

    def test_enrove_numbers(self):
        self.assertEqual(self.rv.enrove('0123456789'), '0123456789')

    def test_enrove_special_characters(self):   
        self.assertEqual(self.rv.enrove('!@#$%^&*()_+-=[]'), '!@#$%^&*()_+-=[]')



if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)