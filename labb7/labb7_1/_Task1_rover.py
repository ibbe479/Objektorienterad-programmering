'''
    Student shall write their names here
        1. Student 1
        2. Student 2
'''

import unittest
from Task1_rover import rovar

class test_string(unittest.TestCase):
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


    def test_null_input(self):
        self.assertIsNone(self.rv.enrove(None))
        self.assertIsNone(self.rv.derove(None))

    def test_emty_string(self):
        self.assertEqual(self.rv.enrove(''), '')
        self.assertEqual(self.rv.derove(" ")," ")


    def test_low_case(self):
        self.assertEqual(self.rv.enrove('bcdfhjklmnpqrstvwxz'), 'bobcocdodfofhohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz')

    def test_upper_c(self):
        self.assertEqual(self.rv.enrove('BCDFHJJKLMNPQRSTVWXZ'), 'BOBCOCDODFOFHOHJOJJOJKOKLOLMOMNONPOPQOQRORSOSTOTVOVWOWXOXZOZ')

    def test_low_vol(self):
        self.assertEqual(self.rv.enrove('aeiouyåäö'), 'aeiouyåäö')

    def test_up_vol(self):
        self.assertEqual(self.rv.enrove('AEIOUYÅÄÖ'), 'AEIOUYÅÄÖ')

    def test_num(self):
        self.assertEqual(self.rv.enrove('1234567890'), '1234567890')

    def test_special_char(self):
        self.assertEqual(self.rv.enrove('!@#€%&/()=?`´*+-_.,;:<>|^¨~'), '!@#€%&/()=?`´*+-_.,;:<>|^¨~')


if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)