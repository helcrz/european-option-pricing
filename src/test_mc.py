from config import S0, K, T, r, sigma
from monte_carlo import prix_call_monte_carlo
from black_scholes import prix_call_black_scholes

def main():
    N = 100000
    
    prix_bs = prix_call_black_scholes(S0, K, T, r, sigma)
    prix_mc = prix_call_monte_carlo(S0, K, T, r, sigma, N)
    
    erreur = abs(prix_mc - prix_bs)
    
    print(f"Prix théorique (Black-Scholes) : {prix_bs:.2f} €")
    print(f"Prix estimé (Monte-Carlo, N={N}) : {prix_mc:.2f} €")
    print(f"Erreur absolue : {erreur:.4f} €")

if __name__ == "__main__":
    main()