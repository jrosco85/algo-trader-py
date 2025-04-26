#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stock entity representing a financial instrument traded on an exchange.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from src.domain.value_objects.price import Price
from src.domain.value_objects.exchange import Exchange

@dataclass
class Stock:
    """
    Stock entity representing a financial instrument traded on stock exchanges.
    
    Attributes:
        symbol: The ticker symbol used to identify the stock.
        company_name: The name of the company issuing the stock.
        isin: International Securities Identification Number.
        exchange: The primary exchange where the stock is listed.
        sector: The business sector of the company.
        industry: The specific industry within the sector.
        currency: The currency in which the stock is traded.
        current_price: The current market price of the stock.
        open_price: The opening price of the trading day.
        high_price: The highest price of the trading day.
        low_price: The lowest price of the trading day.
        close_price: The previous day's closing price.
        volume: The trading volume of the day.
        market_cap: The market capitalization of the company.
        pe_ratio: The price-to-earnings ratio.
        dividend_yield: The annual dividend yield as a percentage.
        beta: The volatility measure compared to the market.
        fifty_day_avg: The 50-day moving average price.
        two_hundred_day_avg: The 200-day moving average price.
        year_high: The 52-week high price.
        year_low: The 52-week low price.
        last_updated: Timestamp of the last data update.
        id: Unique identifier for the stock entity.
    """
    symbol: str
    company_name: str
    exchange: Exchange
    current_price: Price
    currency: str
    sector: Optional[str] = None
    industry: Optional[str] = None
    isin: Optional[str] = None
    open_price: Optional[Price] = None
    high_price: Optional[Price] = None
    low_price: Optional[Price] = None
    close_price: Optional[Price] = None
    volume: Optional[int] = None
    market_cap: Optional[float] = None
    pe_ratio: Optional[float] = None
    dividend_yield: Optional[float] = None
    beta: Optional[float] = None
    fifty_day_avg: Optional[float] = None
    two_hundred_day_avg: Optional[float] = None
    year_high: Optional[float] = None
    year_low: Optional[float] = None
    last_updated: datetime = datetime.now()
    id: UUID = uuid4()
    
    def is_market_open(self) -> bool:
        """
        Check if the market for this stock is currently open.
        
        Returns:
            bool: True if the market is open, False otherwise.
        """
        return self.exchange.is_open()
    
    def calculate_price_change(self) -> float:
        """
        Calculate the price change from previous close to current price.
        
        Returns:
            float: Percentage change in price.
        """
        if self.close_price and self.close_price.amount > 0:
            return (self.current_price.amount - self.close_price.amount) / self.close_price.amount * 100
        return 0.0
    
    def update_price(self, new_price: Price) -> None:
        """
        Update the current price of the stock.
        
        Args:
            new_price: The new price to set.
        """
        self.current_price = new_price
        self.last_updated = datetime.now()
    
    def update_market_data(self, open_price: Price, high_price: Price, 
                          low_price: Price, close_price: Price, 
                          volume: int) -> None:
        """
        Update the market data for this stock.
        
        Args:
            open_price: The opening price.
            high_price: The highest price of the day.
            low_price: The lowest price of the day.
            close_price: The closing price.
            volume: The trading volume.
        """
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume
        self.last_updated = datetime.now()
    
    def __str__(self) -> str:
        return f"{self.symbol} ({self.exchange.code}): {self.current_price}"