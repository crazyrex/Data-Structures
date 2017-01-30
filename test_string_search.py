#!python

from string_search import stringSearch
import unittest

class TestStringSearch(unittest.TestCase):
	
	def test_string_search_easy(self):
		assert stringSearch("bcd", "wwzyz") == False
		assert stringSearch("bcd", "abcde") == True

if __name__ == '__main__':
    unittest.main()
