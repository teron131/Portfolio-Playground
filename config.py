"""
Configuration parameters for portfolio optimization.
"""

# Stock selection
STOCKS = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "GOOGL",  # Alphabet Inc.
    "AMZN",  # Amazon.com Inc.
    "META",  # Meta Platforms Inc.
    "BRK-B",  # Berkshire Hathaway Inc.
    "JPM",  # JPMorgan Chase & Co.
    "JNJ",  # Johnson & Johnson
    "V",  # Visa Inc.
    "PG",  # Procter & Gamble Co.
    "XOM",  # Exxon Mobil Corporation
]

# Time period settings
START_YEAR = 2023
ADJUST_PERIOD = 60  # days
ROLLING_WINDOW = 60  # days