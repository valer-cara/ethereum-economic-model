import diskcache
import yfinance as yf

from dotenv import load_dotenv

load_dotenv()
cache = diskcache.Cache(".api.cache")

@cache.memoize(expire=(24 * 60 * 60))
def get_market_prices(start_date, end_date, interval, ohlc="Open"):
    """Retrieves ETH/USD price via YFinance


    The available data resolution is 1 day.

    Args:
        start_date, end_date : str
            Download start date string (YYYY-MM-DD) or _datetime.
            Default is 1900-01-01
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
    """

    eth_prices = yf.download(
        tickers="ETH-USD",
        start=start_date,
        end=end_date,
        interval=interval,
        group_by = "ticker",
        auto_adjust=True,
        rounding=True,
    )

    return eth_prices[ohlc]

