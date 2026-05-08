import yfinance as yf

# Human-readable name → Yahoo Finance ticker
TICKERS = {
    "Gold": "GC=F",
    "Silver": "SI=F",
    "S&P 500": "^GSPC",
}

def fetch_data(start_date="2021-01-01"):
    """
    Downloads closing prices for each asset in TICKERS from start_date to today.
    Returns a dictionary {name: pandas Series}.
    """
    data = {}
    for name, ticker in TICKERS.items():
        df = yf.Ticker(ticker).history(start=start_date)["Close"]
        df = df.dropna()
        data[name] = df
    return data