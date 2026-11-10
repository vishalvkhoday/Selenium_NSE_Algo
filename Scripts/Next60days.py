import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Fetch GSFC data
ticker = "GSFC.NS"
data = yf.download(ticker, period="6mo", interval="1d")

# Step 2: Calculate volatility & moving averages
data['MA20'] = data['Close'].rolling(20).mean()
volatility = data['Close'].pct_change().std() * np.sqrt(252)

# Step 3: Scenario modeling
last_price = data['Close'].iloc[-1]

scenarios = {
    "Bull": last_price * (1 + 0.12),   # +12% over 60 days
    "Base": last_price * (1 + 0.06),   # +6% over 60 days
    "Bear": last_price * (1 - 0.05)    # -5% over 60 days
}

# Step 4: Visualization
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label="GSFC Price")
for case, target in scenarios.items():
    plt.axhline(y=target, linestyle="--", label=f"{case} Target: {target:.2f}")
plt.legend()
plt.title("GSFC 60-Day Scenario Forecast")
plt.show()
