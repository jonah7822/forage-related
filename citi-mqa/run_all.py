from scipy.stats import norm
import numpy as np

S_t = 1.20
X = 1.25
r = 0.02
d = 0.01
T = 0.5
sigma = 0.25

# cost of carry model

F_t = S_t * np.exp((r + d) * T)

print(f"The fair price of the coffee futures contract is ${F_t:.3f} per pound.")

# Black-Scholes model

d1 = (np.log(S_t / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

C = S_t * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)

print(f"The price of the call option is ${C:.3f}.")

# Monte Carlo simulation

num_simulations = 10000
num_steps = 252

dt = T / num_steps

np.random.seed(42)
price_paths = np.zeros((num_steps, num_simulations))
price_paths[0] = S_t

for t in range(1, num_steps):
    z = np.random.standard_normal(num_simulations)
    price_paths[t] = price_paths[t-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)

average_simulated_price = np.mean(price_paths[-1])

print(f"The average simulated price of the coffee futures contract at maturity is ${average_simulated_price:.3f}.")