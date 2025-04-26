#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the Exchange value object.
"""

import unittest
from datetime import datetime, time, timezone

from src.domain.value_objects.exchange import Exchange

class TestExchange(unittest.TestCase):
    """
    Test cases for the Exchange value object.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        self.nyse = Exchange(
            name="New York Stock Exchange",
            code="NYSE",
            country="United States",
            currency="USD",
            timezone="America/New_York",
            open_time=time(9, 30),  # 9:30 AM
            close_time=time(16, 0),  # 4:00 PM
        )
    
    def test_exchange_creation(self):
        """
        Test that an Exchange can be created with the correct attributes.
        """
        self.assertEqual(self.nyse.name, "New York Stock Exchange")
        self.assertEqual(self.nyse.code, "NYSE")
        self.assertEqual(self.nyse.country, "United States")
        self.assertEqual(self.nyse.currency, "USD")
        self.assertEqual(self.nyse.timezone, "America/New_York")
        self.assertEqual(self.nyse.open_time, time(9, 30))
        self.assertEqual(self.nyse.close_time, time(16, 0))
    
    def test_exchange_immutability(self):
        """
        Test that Exchange is immutable (frozen dataclass).
        """
        with self.assertRaises(AttributeError):
            self.nyse.name = "NYSE"
        with self.assertRaises(AttributeError):
            self.nyse.code = "NEW-NYSE"
    
    def test_is_open(self):
        """
        Test the is_open method with different times.
        """
        # Create a datetime that should be during open hours
        open_datetime = datetime.combine(
            datetime.now().date(),
            time(12, 0)  # Noon, which is between 9:30 AM and 4:00 PM
        ).replace(tzinfo=timezone.utc)
        
        # Create a datetime that should be outside open hours
        closed_datetime = datetime.combine(
            datetime.now().date(),
            time(8, 0)  # 8:00 AM, which is before 9:30 AM
        ).replace(tzinfo=timezone.utc)
        
        # Test with explicit times
        self.assertTrue(self.nyse.is_open(open_datetime))
        self.assertFalse(self.nyse.is_open(closed_datetime))
        
        # Test edge cases
        open_edge = datetime.combine(
            datetime.now().date(),
            time(9, 30)  # Exactly opening time
        ).replace(tzinfo=timezone.utc)
        
        close_edge = datetime.combine(
            datetime.now().date(),
            time(16, 0)  # Exactly closing time
        ).replace(tzinfo=timezone.utc)
        
        self.assertTrue(self.nyse.is_open(open_edge))
        self.assertTrue(self.nyse.is_open(close_edge))
    
    def test_string_representation(self):
        """
        Test the string representation of Exchange.
        """
        expected_str = "New York Stock Exchange (NYSE)"
        self.assertEqual(str(self.nyse), expected_str)

if __name__ == '__main__':
    unittest.main()