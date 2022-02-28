"""
Name: Dave Taveras
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Date: February 21st, 2022
Assignment: Homework 4
Course: SSW 555
Professor: Ens
"""

import unittest
import Homework4

class TestHomework4(unittest.TestCase):

	def test_dateBeforeCurrent1(self):
		result = Homework4.dateBeforeCurrent("31 AUG 2000")
		self.assertTrue(result)

	def test_dateBeforeCurrent2(self):
		result = Homework4.dateBeforeCurrent("9 DEC 2025")
		self.assertFalse(result)

	def test_dateBeforeCurrent3(self):
		result = Homework4.dateBeforeCurrent("28 FEB 1990")
		self.assertTrue(result)

	def test_dateBeforeCurrent4(self):
		result = Homework4.dateBeforeCurrent("21 FEB 2022")
		self.assertEqual(result, True)

	def test_dateBeforeCurrent5(self):
		result = Homework4.dateBeforeCurrent("11 MAR 2022")
		self.assertEqual(result, False)