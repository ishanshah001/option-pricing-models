# 📈 Option Pricing Models: Black-Scholes vs Monte Carlo

This interactive Streamlit app compares two popular methods for pricing European call and put options:

- ✅ **Black-Scholes Formula**: A closed-form analytical solution
- 🎲 **Monte Carlo Simulation**: A numerical approach based on random paths

---

## 🚀 Features

- Input key option parameters (stock price, strike, volatility, time, etc.)
- Calculate both call and put prices
- Compare prices using both models
- Visualize results side-by-side in a bar chart
- Built using Python + Streamlit for simplicity and interactivity

---

## 📋 Inputs

- **S**: Stock Price  
- **K**: Strike Price  
- **T**: Time to Expiry (in years)  
- **σ**: Volatility (standard deviation of returns)  
- **r**: Risk-free Interest Rate  
- **N**: Number of Monte Carlo simulations  
<!--
---

## 📸 Screenshots

| Black-Scholes vs Monte Carlo | Price Comparison Chart |
|------------------------------|-------------------------|
| ![UI](screenshots/ui.png)    | ![Chart](screenshots/chart.png) |

-->
---

## ⚙️ Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/option-pricing-models.git
   cd option-pricing-models
