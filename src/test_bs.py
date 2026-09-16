from config import S0, K, T, r, sigma
from black_scholes import prix_call_black_scholes

def main():
    prix = prix_call_black_scholes(S0, K, T, r, sigma)
    print(f"Prix théorique (Black-Scholes) : {prix:.2f} €")

if __name__ == "__main__":
    main()