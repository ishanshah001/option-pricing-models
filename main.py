import streamlit as st
from utils import black_scholes_price, monte_carlo_price

st.set_page_config(page_title="Option Pricing", layout="centered")

st.title("📈 Option Pricing: Black-Scholes vs Monte Carlo")

st.sidebar.header("Option Parameters")
S = st.sidebar.number_input("Current Stock Price (S)", value=100.0)
K = st.sidebar.number_input("Strike Price (K)", value=110.0)
T = st.sidebar.number_input("Time to Expiration (years, T)", value=1.0)
r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2)
simulations = st.sidebar.slider("Monte Carlo Simulations", 1000, 50000, 10000, step=1000)
option_type = st.sidebar.selectbox("Option Type", ["call", "put"])

if st.button("Calculate Option Prices"):
    bs = black_scholes_price(S, K, T, r, sigma, option_type)
    mc = monte_carlo_price(S, K, T, r, sigma, option_type, simulations)

    st.success(f"📘 Black-Scholes {option_type.title()} Price: **${bs:.4f}**")
    st.success(f"🎲 Monte Carlo {option_type.title()} Price: **${mc:.4f}**")

    st.bar_chart({
        "Black-Scholes": [bs],
        "Monte Carlo": [mc]
    })

st.markdown("---")
st.markdown("Made by [Ishan Shah] • [GitHub Repo](https://github.com/ishanshah001/option-pricing-models)")
