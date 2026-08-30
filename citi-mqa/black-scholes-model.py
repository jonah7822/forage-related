from scipy.stats import norm
import numpy as np

S_0 = 1.20 # Spot price ($1.20) - can obtain this from sites like Bloomberg, Reuters, or ICO
X = 1.25 # Strike price ($1.25) - using market conditions and option contracts info on exchanges like ICE
r = 0.02 # Risk-free rate (2%) - Used the current yield on a six-month US Treasury bill as a proxy
T = 0.5 # Time to maturity in years
sigma = 0.25 # Volatility (25%) - calculate or find the historical volatility of coffee prices

# Calculating d1 and d2

d1 = (np.log(S_0 / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

# Calculating call option price using Black-Scholes formula

C = S_0 * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)

print(f"The price of the call option is ${C:.3f}.")
