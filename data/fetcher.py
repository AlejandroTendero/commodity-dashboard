import yfinance as yf

# ETFs mapped to their commodity — physical or futures-based ETFs only
# (no mining company ETFs, as they track equities not commodity prices)
TICKERS = {
    # Precious metals futures
    "Gold": "GC=F",
    "Silver": "SI=F",
    #"Platinum": "PL=F",
    #"Palladium": "PA=F",
    # Industrial metals futures
    "Copper": "HG=F",
    # Energy futures-based ETFs
    "Oil (WTI)": "CL=F",
    "Natural Gas": "NG=F",
    # Equities index — for comparison
    "S&P 500": "^GSPC",
}

VALID_PERIODS = ["1mo", "6mo", "1y", "2y", "5y", "10y"]

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
    Downloads closing prices for all assets across all available periods.
    Returns a dictionary {period: {name: pandas Series}}.
    """
    all_data = {}
    for period in VALID_PERIODS:
        all_data[period] = fetch_data(period=period)
    return all_data