from datetime import datetime

import numpy as np
import yfinance as yf
from scipy.stats.mstats import winsorize

from config import ROLLING_WINDOW, START_YEAR, STOCKS
from portfolios import EWP, RPP, CVaR


def log_return(data):
    """
    Calculate log returns from price data, handling missing values.

    Args:
        data (pd.DataFrame): Price data

    Returns:
        pd.DataFrame: Log returns
    """
    data = data.copy()
    data.interpolate(inplace=True)
    data.fillna(1, inplace=True)

    log_return = data.apply(np.log).diff()
    log_return.dropna(inplace=True)

    return log_return


def winsorization(data, lower=0.025, upper=0.975):
    """
    Winsorize data between specified percentiles.

    Args:
        data (pd.DataFrame): Data to winsorize
        lower (float): Lower percentile bound
        upper (float): Upper percentile bound

    Returns:
        pd.DataFrame: Winsorized data
    """
    winsorized_data = data.copy()
    for col in data.columns:
        winsorized_data[col] = winsorize(data[col], limits=(lower, 1 - upper))
    return winsorized_data


def winsor_mean_cov(log_return):
    """
    Calculate winsorized mean and covariance.

    Args:
        log_return (pd.DataFrame): Log return data

    Returns:
        tuple: (winsorized mean, winsorized covariance)
    """
    winsorized_data = winsorization(log_return)
    mu = winsorized_data.mean()
    sigma = winsorized_data.cov()
    return mu, sigma
