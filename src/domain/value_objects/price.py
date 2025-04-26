#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Price value object representing a monetary amount.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Union

@dataclass(frozen=True)
class Price:
    """
    Value object representing a monetary price amount.
    
    Attributes:
        amount: The decimal amount of the price.
        currency: The currency code (e.g., 'USD', 'EUR').
    """
    amount: Decimal
    currency: str
    
    def __init__(self, amount: Union[Decimal, float, int, str], currency: str):
        """
        Create a new Price instance.
        
        Args:
            amount: The amount as Decimal, float, int, or string.
            currency: The currency code (e.g., 'USD', 'EUR').
        """
        # Convert amount to Decimal if it's not already
        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))
        
        # Since the class is frozen, we need to use object.__setattr__
        object.__setattr__(self, 'amount', amount)
        object.__setattr__(self, 'currency', currency.upper())
    
    def __add__(self, other):
        """
        Add two Price objects with the same currency.
        
        Args:
            other: Another Price object.
            
        Returns:
            A new Price object with the sum of the amounts.
            
        Raises:
            ValueError: If currencies don't match.
        """
        if not isinstance(other, Price):
            return NotImplemented
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot add prices with different currencies: {self.currency} and {other.currency}")
        
        return Price(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        """
        Subtract another Price object from this one.
        
        Args:
            other: Another Price object.
            
        Returns:
            A new Price object with the difference of the amounts.
            
        Raises:
            ValueError: If currencies don't match.
        """
        if not isinstance(other, Price):
            return NotImplemented
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract prices with different currencies: {self.currency} and {other.currency}")
        
        return Price(self.amount - other.amount, self.currency)
    
    def __mul__(self, multiplier: Union[int, float, Decimal]):
        """
        Multiply the price by a scalar.
        
        Args:
            multiplier: A number to multiply the price by.
            
        Returns:
            A new Price object with the multiplied amount.
        """
        if not isinstance(multiplier, (int, float, Decimal)):
            return NotImplemented
        
        return Price(self.amount * Decimal(str(multiplier)), self.currency)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def __lt__(self, other):
        if not isinstance(other, Price) or self.currency != other.currency:
            return NotImplemented
        return self.amount < other.amount
    
    def __le__(self, other):
        if not isinstance(other, Price) or self.currency != other.currency:
            return NotImplemented
        return self.amount <= other.amount
    
    def __gt__(self, other):
        if not isinstance(other, Price) or self.currency != other.currency:
            return NotImplemented
        return self.amount > other.amount
    
    def __ge__(self, other):
        if not isinstance(other, Price) or self.currency != other.currency:
            return NotImplemented
        return self.amount >= other.amount