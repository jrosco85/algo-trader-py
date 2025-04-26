#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the Stock entity.
"""

import unittest
from datetime import datetime, time
from decimal import Decimal
from unittest.mock import patch

from src.domain.entities.stock import Stock
from src.domain.value_objects.price import Price
from src.domain.value_objects.exchange import Exchange

class TestStock(unittest.TestCase):
    """
    Test cases for the Stock entity.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        # Create a mock exchange
        self.exchange = Exchange(
            name="New York Stock Exchange",
            code="NYSE",
            country="United States",
            currency="USD",
            timezone="America/New_York",
            open_time=time(9, 30),  # 9:30 AM
            close_time=time(16, 0),  # 4:00 PM
        )
        
        # Create a basic stock for testing
        self.stock = Stock(
            symbol="AAPL",
            company_name="Apple Inc.",
            exchange=self.exchange,
            current_price=Price(150.0, "USD"),
            currency="USD",
            sector="Technology",
            industry="Consumer Electronics",
            isin="US0378331005",
            close_price=Price(148.5, "USD"),
            volume=1000000
        )
    
    def test_stock_creation(self):
        """
        Test that a stock can be created with the correct attributes.
        """
        self.assertEqual(self.stock.symbol, "AAPL")
        self.assertEqual(self.stock.company_name, "Apple Inc.")
        self.assertEqual(self.stock.exchange.code, "NYSE")
        self.assertEqual(self.stock.current_price.amount, Decimal('150.0'))
        self.assertEqual(self.stock.current_price.currency, "USD")
        self.assertEqual(self.stock.currency, "USD")
        self.assertEqual(self.stock.sector, "Technology")
        self.assertEqual(self.stock.industry, "Consumer Electronics")
        self.assertEqual(self.stock.isin, "US0378331005")
    
    def test_calculate_price_change(self):
        """
        Test the calculation of price change percentage.
        """
        # Current price is 150.0, close price is 148.5
        expected_change = (150.0 - 148.5) / 148.5 * 100  # 1.01%
        self.assertAlmostEqual(self.stock.calculate_price_change(), expected_change)
        
        # Test with no close price
        stock_no_close = Stock(
            symbol="MSFT",
            company_name="Microsoft Corporation",
            exchange=self.exchange,
            current_price=Price(250.0, "USD"),
            currency="USD"
        )
        self.assertEqual(stock_no_close.calculate_price_change(), 0.0)
    
    def test_update_price(self):
        """
        Test updating the stock price.
        """
        new_price = Price(155.0, "USD")
        
        # Store the original last_updated time
        old_time = self.stock.last_updated
        
        # Wait a tiny bit to ensure the timestamp changes
        import time as time_module
        time_module.sleep(0.001)
        
        # Update the price
        self.stock.update_price(new_price)
        
        # Check that the price was updated
        self.assertEqual(self.stock.current_price.amount, Decimal('155.0'))
        
        # Check that the last_updated timestamp was updated
        self.assertGreater(self.stock.last_updated, old_time)
    
    def test_update_market_data(self):
        """
        Test updating market data for the stock.
        """
        open_price = Price(149.0, "USD")
        high_price = Price(152.0, "USD")
        low_price = Price(148.0, "USD")
        close_price = Price(151.0, "USD")
        volume = 1500000
        
        # Store the original last_updated time
        old_time = self.stock.last_updated
        
        # Wait a tiny bit to ensure the timestamp changes
        import time as time_module
        time_module.sleep(0.001)
        
        # Update the market data
        self.stock.update_market_data(
            open_price=open_price,
            high_price=high_price,
            low_price=low_price,
            close_price=close_price,
            volume=volume
        )
        
        # Check that the data was updated
        self.assertEqual(self.stock.open_price, open_price)
        self.assertEqual(self.stock.high_price, high_price)
        self.assertEqual(self.stock.low_price, low_price)
        self.assertEqual(self.stock.close_price, close_price)
        self.assertEqual(self.stock.volume, volume)
        
        # Check that the last_updated timestamp was updated
        self.assertGreater(self.stock.last_updated, old_time)
    
    @patch('src.domain.value_objects.exchange.Exchange.is_open')
    def test_is_market_open(self, mock_is_open):
        """
        Test the is_market_open method.
        """
        # Test when market is open
        mock_is_open.return_value = True
        self.assertTrue(self.stock.is_market_open())
        
        # Test when market is closed
        mock_is_open.return_value = False
        self.assertFalse(self.stock.is_market_open())
    
    def test_string_representation(self):
        """
        Test the string representation of the stock.
        """
        expected_str = "AAPL (NYSE): 150.0 USD"
        self.assertEqual(str(self.stock), expected_str)

if __name__ == '__main__':
    unittest.main()