#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main module for the algorithmic trading platform.

This file serves as the entry point for the application.
"""

from src.adapters.input.cli.cli_controller import start_cli
from src.adapters.input.api.api_controller import start_api

def main():
    """
    Main function that starts the application.
    
    This function initializes the necessary components and starts
    the selected interface (CLI or API).
    """
    print("Starting Algorithmic Trading Platform...")
    
    # Uncomment one of these to choose the interface:
    # start_cli()
    # start_api()
    
    print("Welcome to your Algorithmic Trading Platform")

if __name__ == "__main__":
    main()
