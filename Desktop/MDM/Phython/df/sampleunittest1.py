import random
import unittest
from unittest.test import test_runner
import HtmlTestRunner




class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

outfile = open("Report.html", "w")
testRunner=HtmlTestRunner.HTMLTestRunner(output=outfile,)
