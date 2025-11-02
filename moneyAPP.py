# moneyAPP.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="fe3nzy EA Dashboard", layout="wide")

st.title("💰 fe3nzy EA Dashboard")
st.markdown("Real-time trading stats from your EA's CSV log (`EA_Stats.csv`)")

# Load trading data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("EA_Stats.csv")
        return df
    except FileNotFoundError:
        st.warning("EA_Stats.csv not found! Make sure your EA is exporting trades to CSV.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.subheader("📊 Recent Trades")
    st.dataframe(df.tail(10))

    st.subheader("📈 Trades Overview")
    # Total Profit per Symbol
    profit_by_symbol = df.groupby("Symbol")["Profit"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(profit_by_symbol["Symbol"], profit_by_symbol["Profit"], color='green')
    ax.set_ylabel("Total Profit")
    ax.set_title("Profit by Symbol")
    st.pyplot(fig)

    st.subheader("⚡ Summary")
    st.markdown(f"- Total Trades: {len(df)}")
    st.markdown(f"- Total Profit: {df['Profit'].sum():.2f}")
    st.markdown(f"- Average Profit per Trade: {df['Profit'].mean():.2f}")
else:
    st.info("No trading data available yet.")


