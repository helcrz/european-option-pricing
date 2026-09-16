import numpy as np

def prix_call_monte_carlo(S0, K, T, r, sigma, N):
    Z = np.random.standard_normal(N)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    payoffs = np.maximum(ST - K, 0)
    
    call_price = np.exp(-r * T) * np.mean(payoffs)
    return call_price