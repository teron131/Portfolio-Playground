import numpy as np


# Sharpe Ratio (SR)
def sharpe_ratio(mu, sigma, w):
    return np.dot(mu, w) / np.sqrt(np.dot(w.T, np.dot(sigma, w)))


# Relative Risk Contribution (RRC)
def relative_risk_contribution(sigma, w):
    return w * np.dot(sigma, w) / np.dot(w.T, np.dot(sigma, w))


# Vanilla backtesting
# Cumulative returns
def backtest(test_data, portfolio):
    test_daily_returns = test_data.pct_change()
    cumulative_returns = (1 + (test_daily_returns @ portfolio)).cumprod()
    return cumulative_returns


# Drawdown
def drawdown_time(cumulative_returns):
    peak = cumulative_returns.expanding(min_periods=1).max()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown


# Alpha and Beta
def alpha_beta(test_data, portfolio):
    test_daily_returns = test_data.pct_change()
    portfolio_returns = test_daily_returns @ portfolio
    benchmark_daily_returns = test_daily_returns.mean(axis=1)
    covariance_matrix = np.cov(portfolio_returns[1:], benchmark_daily_returns[1:])
    beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
    alpha = np.mean(portfolio_returns) - beta * np.mean(benchmark_daily_returns)
    return alpha, beta
