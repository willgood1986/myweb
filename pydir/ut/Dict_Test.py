# -*- coding: utf-8 -*-

import unittest
from Dict import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='abc')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'abc')

    def test_Key(self):
        d = Dict()
        d['key'] = 'val'
        self.assertTrue('key' in d)
        self.assertEqual(d.key, 'val')

    def test_attr(self):
        d = Dict()
        d['key'] = 'val'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'val')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            val = d['empty']    

    def test_attributeerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
             val = d.empty

    def setUp(self):
        print('setUp is called')

    def tearDown(self):
        print('tearDown is called')

if __name__ == '__main__':
    print('''
    import unittest
    inherit from unittest.TestCase
    every test method must start with test_
    run the test use unittest.main()
    ''')
       
    unittest.main()
