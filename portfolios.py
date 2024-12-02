import cvxpy as cp
import numpy as np
from scipy.optimize import minimize


## Heuristic Portfolios
# Equally Weighted Portfolio (EWP)
def EWP(mu, sigma):
    N = len(mu)
    w_EWP = np.ones(N) / N
    return w_EWP


## Risk-Based Portfolios
# Risk Parity Portfolio (RPP) with Convex Formulation
def RPP(mu, sigma):
    N = len(mu)
    b = np.ones(N) / N

    # Objective function
    def fn_convex(x, Sigma, b):
        return 0.5 * x.T @ Sigma @ x - np.sum(b * np.log(x))

    # Optimize with general-purpose solver
    x0 = np.ones(N) / N
    result = minimize(fn_convex, x0, args=(sigma, b), method="BFGS")
    w_RPP = result.x / np.sum(result.x)

    return w_RPP


# Mean-CVaR portfolio (CVaRP)
def CVaR(X, lmd=0.5, alpha=0.99):
    X = X.values
    T, N = np.shape(X)
    mu = np.mean(X, axis=0)
    w = cp.Variable(N)
    z = cp.Variable(T)
    zeta = cp.Variable(1)
    problem = cp.Problem(
        cp.Maximize(w @ mu - lmd * zeta - (lmd / (T * (1 - alpha))) * cp.sum(z)),
        [z >= 0, z >= -X @ w - zeta, w >= 0, cp.sum(w) == 1],
    )
    problem.solve()
    return w.value
