from config import S0, K, T, r, sigma

def main():
    print("--- Paramètres du modèle financier ---")
    print(f"Prix de l'action (S0) : {S0} €")
    print(f"Strike (K)            : {K} €")
    print(f"Maturité (T)          : {T} année(s)")
    print(f"Taux sans risque (r)  : {r*100}%")
    print(f"Volatilité (sigma)    : {sigma*100}%")
    print("--------------------------------------")
    print("L'importation des paramètres fonctionne correctement !")

if __name__ == "__main__":
    main()