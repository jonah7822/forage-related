import numpy as np

S_t = 1.20 # Spot price ($1.20) - can obtain this from sites like Bloomberg, Reuters, or ICO
r = 0.02 # Risk-free rate (2%) - Used the current yield on a six-month US Treasury bill as a proxy
d = 0.01 # Storage cost (1%) - This might be available in commodity market reports / industry publications
T = 0.5 # Time to maturity in years

# Calculating futures price

F_t = S_t * np.exp((r + d) * T)

print(f"The fair price of the coffee futures contract is ${F_t:.3f} per pound.")