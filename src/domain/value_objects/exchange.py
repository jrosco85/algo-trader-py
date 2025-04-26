#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exchange value object representing a stock exchange.
"""

from dataclasses import dataclass
from datetime import datetime, time, timezone
from typing import Optional

@dataclass(frozen=True)
class Exchange:
    """
    Value object representing a stock exchange.
    
    Attributes:
        name: The full name of the exchange.
        code: The exchange code (e.g., 'NYSE', 'NASDAQ').
        country: The country where the exchange is located.
        currency: The primary currency used for trading.
        timezone: The timezone of the exchange (e.g., 'America/New_York').
        open_time: The standard opening time of the exchange.
        close_time: The standard closing time of the exchange.
    """
    name: str
    code: str
    country: str
    currency: str
    timezone: str
    open_time: time
    close_time: time
    
    def is_open(self, reference_time: Optional[datetime] = None) -> bool:
        """
        Check if the exchange is currently open for trading.
        
        Args:
            reference_time: The time to check against. Defaults to current time.
            
        Returns:
            bool: True if the exchange is open, False otherwise.
        """
        # Use provided time or current time
        if reference_time is None:
            reference_time = datetime.now(timezone.utc)
        
        # Extract the time component
        current_time = reference_time.time()
        
        # Simple check for now - doesn't account for holidays or special hours
        return self.open_time <= current_time <= self.close_time
    
    def __str__(self) -> str:
        return f"{self.name} ({self.code})"