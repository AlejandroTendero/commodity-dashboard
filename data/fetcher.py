import yfinance as yf

# ETFs mapped to their commodity — physical or futures-based ETFs only
# (no mining company ETFs, as they track equities not commodity prices)
TICKERS = {
    # Precious metals futures
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Platinum": "PL=F",
    #"Palladium": "PA=F",
    # Industrial metals futures
    "Copper": "HG=F",
    # Energy futures-based ETFs
    "Oil (WTI)": "CL=F",
    "Natural Gas": "NG=F",
    # Equities index — for comparison
    "S&P 500": "^GSPC",
}

VALID_PERIODS = ["1mo", "6mo", "1y", "2y", "5y"]

def fetch_data(period="5y"):
    """
    Downloads closing prices for all assets for the given period.
    Period must be one of: 1y, 2y, 5y, 10y, max.
    Returns a dictionary {name: pandas Series}.
    """
    if period not in VALID_PERIODS:
        raise ValueError(f"Invalid period '{period}'. Must be one of {VALID_PERIODS}")

    data = {}
    for name, ticker in TICKERS.items():
        df = yf.Ticker(ticker).history(period=period)["Close"]
        data[name] = df.dropna()
    return data

def fetch_all_periods():
    """
    Downloads data for all valid periods.
    Returns a dict {period: {name: Series}} ready for normalized_chart().
    """
    # Why a separate function instead of doing this in main.py:
    # fetcher.py already knows TICKERS and VALID_PERIODS.
    # Duplicating that logic in main.py would mean two places to update
    # when you add a ticker or a period — a classic source of bugs.
    return {period: fetch_data(period) for period in VALID_PERIODS}