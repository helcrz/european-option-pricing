# Pricing d'options européennes — Black-Scholes & Monte-Carlo

Projet Python de valorisation d'une option européenne de type **Call**.

L'objectif est de calculer le prix d'une option de deux manières :

1. Avec la formule analytique de **Black-Scholes**
2. Avec une simulation **Monte-Carlo**

Les deux méthodes sont ensuite comparées afin d'étudier la convergence de Monte-Carlo vers le prix théorique de Black-Scholes.

---

## 🎯 Objectif du projet

Le projet cherche à répondre à la question suivante :

> **Monte-Carlo permet-il de retrouver le prix donné par Black-Scholes ?**

Pour cela, nous allons :

- calculer le prix théorique avec Black-Scholes ;
- simuler plusieurs futurs possibles du prix de l'action ;
- calculer le prix de l'option avec Monte-Carlo ;
- augmenter progressivement le nombre de simulations ;
- calculer l'erreur entre les deux méthodes ;
- analyser la convergence ;
- visualiser les résultats avec des graphiques.

---

## 📚 Notions utilisées

Le projet utilise plusieurs notions de probabilités, statistiques et analyse numérique :

- Variable aléatoire
- Loi normale
- Espérance
- Moyenne empirique
- Variance et écart-type
- Loi des grands nombres
- Erreur numérique
- Convergence

---

## 💰 Modèle financier

Nous considérons une option européenne de type **Call**.

Le payoff à l'échéance est :

```text
Payoff = max(S_T - K, 0)