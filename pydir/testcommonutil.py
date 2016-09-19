import unittest
import commonutil

class TestCommonUtil(unittest.TestCase):
    def test_isapath_whenisapth(self):
        print(commonutil.isapath.__doc__)
        self.assertTrue(commonutil.isapath('.'))
    
    def test_isapath_whenisnotapath(self):
        print(commonutil.isapath.__doc__)
        self.assertFalse(commonutil.isapath('test.py'))

    def test_

if __name__ == '__main__':
    unittest.main()
    
