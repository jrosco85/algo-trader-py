#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the Price value object.
"""

import unittest
from decimal import Decimal

from src.domain.value_objects.price import Price

class TestPrice(unittest.TestCase):
    """
    Test cases for the Price value object.
    """
    
    def test_price_creation(self):
        """
        Test that a Price object can be created with different types of input.
        """
        # Test with Decimal
        price1 = Price(Decimal('10.50'), 'USD')
        self.assertEqual(price1.amount, Decimal('10.50'))
        self.assertEqual(price1.currency, 'USD')
        
        # Test with float
        price2 = Price(10.50, 'EUR')
        self.assertEqual(price2.amount, Decimal('10.50'))
        self.assertEqual(price2.currency, 'EUR')
        
        # Test with int
        price3 = Price(10, 'GBP')
        self.assertEqual(price3.amount, Decimal('10'))
        self.assertEqual(price3.currency, 'GBP')
        
        # Test with string
        price4 = Price('10.50', 'JPY')
        self.assertEqual(price4.amount, Decimal('10.50'))
        self.assertEqual(price4.currency, 'JPY')
        
        # Test currency conversion to uppercase
        price5 = Price(10, 'usd')
        self.assertEqual(price5.currency, 'USD')
    
    def test_price_immutability(self):
        """
        Test that Price is immutable (frozen dataclass).
        """
        price = Price(10.50, 'USD')
        with self.assertRaises(AttributeError):
            price.amount = Decimal('20.00')
        with self.assertRaises(AttributeError):
            price.currency = 'EUR'
    
    def test_price_addition(self):
        """
        Test addition of Price objects.
        """
        price1 = Price(10.50, 'USD')
        price2 = Price(5.25, 'USD')
        result = price1 + price2
        
        self.assertEqual(result.amount, Decimal('15.75'))
        self.assertEqual(result.currency, 'USD')
        
        # Test addition with different currencies
        price3 = Price(10.50, 'USD')
        price4 = Price(5.25, 'EUR')
        with self.assertRaises(ValueError):
            result = price3 + price4
    
    def test_price_subtraction(self):
        """
        Test subtraction of Price objects.
        """
        price1 = Price(10.50, 'USD')
        price2 = Price(5.25, 'USD')
        result = price1 - price2
        
        self.assertEqual(result.amount, Decimal('5.25'))
        self.assertEqual(result.currency, 'USD')
        
        # Test subtraction with different currencies
        price3 = Price(10.50, 'USD')
        price4 = Price(5.25, 'EUR')
        with self.assertRaises(ValueError):
            result = price3 - price4
    
    def test_price_multiplication(self):
        """
        Test multiplication of Price by a scalar.
        """
        price = Price(10.50, 'USD')
        
        # Multiply by int
        result1 = price * 2
        self.assertEqual(result1.amount, Decimal('21.00'))
        self.assertEqual(result1.currency, 'USD')
        
        # Multiply by float
        result2 = price * 1.5
        self.assertEqual(result2.amount, Decimal('15.75'))
        self.assertEqual(result2.currency, 'USD')
        
        # Multiply by Decimal
        result3 = price * Decimal('0.5')
        self.assertEqual(result3.amount, Decimal('5.25'))
        self.assertEqual(result3.currency, 'USD')
    
    def test_price_comparison(self):
        """
        Test comparison operators for Price objects.
        """
        price1 = Price(10.50, 'USD')
        price2 = Price(5.25, 'USD')
        price3 = Price(10.50, 'USD')
        price4 = Price(10.50, 'EUR')
        
        # Test equality
        self.assertNotEqual(price1, price2)
        self.assertEqual(price1, price3)
        self.assertNotEqual(price1, price4)  # Different currencies
        
        # Test less than
        self.assertFalse(price1 < price2)
        self.assertTrue(price2 < price1)
        self.assertFalse(price1 < price3)  # Equal prices
        
        # Test less than or equal
        self.assertFalse(price1 <= price2)
        self.assertTrue(price2 <= price1)
        self.assertTrue(price1 <= price3)  # Equal prices
        
        # Test greater than
        self.assertTrue(price1 > price2)
        self.assertFalse(price2 > price1)
        self.assertFalse(price1 > price3)  # Equal prices
        
        # Test greater than or equal
        self.assertTrue(price1 >= price2)
        self.assertFalse(price2 >= price1)
        self.assertTrue(price1 >= price3)  # Equal prices
        
        # Test comparison with different currencies
        with self.assertRaises(TypeError):
            price1 < price4
    
    def test_string_representation(self):
        """
        Test the string representation of Price.
        """
        price = Price(10.50, 'USD')
        self.assertEqual(str(price), '10.50 USD')

if __name__ == '__main__':
    unittest.main()