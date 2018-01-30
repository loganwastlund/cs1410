"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest
import caloric_balance


class TestCaloricBalanceInit(unittest.TestCase):
    def test001_CaloricBalanceExists(self):
        self.assertTrue('CaloricBalance' in dir(caloric_balance),
                        'Function "CaloricBalance" is not defined, check your spelling')
        

    def test002_twoOrMoreDataMembers(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        datamembers = cb.__dict__
        self.assertGreaterEqual(len(datamembers), 2, 'You did not save enough datamembers. You should have at least `weight` and `balance`')


    def test003_weightIsSaved(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        datamembers = cb.__dict__

        weightFlag = False
        for k in datamembers:
            if datamembers[k] == 130.0:
                weightFlag = True
        self.assertTrue(weightFlag, 'The value of weight was not saved in a datamember.')


if __name__ == '__main__':
    unittest.main()
