# chennai_forecast.py
# Clean version for IDLE (no Colab commands)
# Fetches and visualizes Chennai weather forecast using OpenWeather API

import os
import sys
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Optional: prettier plots if seaborn installed
try:
    import seaborn as sns
    sns.set(style="whitegrid")
except Exception:
    pass

# -----------------------------
# 1. Set up the API key
# -----------------------------
# Preferred: set an environment variable OPENWEATHER_API_KEY
# Example (before running):  set OPENWEATHER_API_KEY=your_key_here
api_key = "9e1e01b6f46a67ef6a01fa1bf1fb4ad6"


# You may paste your key here temporarily (not recommended for sharing):
# api_key = "your_actual_key_here"

if not api_key:
    sys.exit(
        "❌ No API key found. Set it using:\n"
        "   set OPENWEATHER_API_KEY=your_key_here  (in CMD)\n"
        "or paste it into this script above."
    )

# -----------------------------
# 2. Fetch weather data for Chennai
# -----------------------------
lat, lon = 13.0827, 80.2707
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"

print("📡 Fetching data from OpenWeather...")
resp = requests.get(url)
if not resp.ok:
    sys.exit(f"❌ Error {resp.status_code}: {resp.text[:200]}")

data = resp.json()
if "list" not in data:
    sys.exit("❌ Unexpected API response — check your API key or quota.")

# -----------------------------
# 3. Convert JSON to DataFrame
# -----------------------------
df = pd.json_normalize(data["list"])

df_short = df[["dt_txt", "main.temp", "main.humidity", "weather"]].copy()
df_short.rename(columns={"main.temp": "Temperature", "main.humidity": "Humidity"}, inplace=True)
df_short["dt_txt"] = pd.to_datetime(df_short["dt_txt"])
df_short.sort_values("dt_txt", inplace=True)
df_short["Condition"] = df_short["weather"].apply(
    lambda x: x[0]["main"] if isinstance(x, list) and x else np.nan
)

print("\n✅ First few rows of data:")
print(df_short.head().to_string(index=False))

# -----------------------------
# 4. Plot temperature and humidity
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(df_short["dt_txt"], df_short["Temperature"], marker="o", label="Temperature (°C)")
plt.title("Temperature Forecast - Chennai")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df_short["dt_txt"], df_short["Humidity"], color="orange", marker="o", label="Humidity (%)")
plt.title("Humidity Forecast - Chennai")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Frequency of conditions
# -----------------------------
plt.figure(figsize=(8, 4))
df_short["Condition"].value_counts().plot(kind="bar")
plt.title("Weather Condition Frequency")
plt.xlabel("Condition")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -----------------------------
# 6. KPIs
# -----------------------------
avg_temp = df_short["Temperature"].mean()
max_temp = df_short["Temperature"].max()
min_temp = df_short["Temperature"].min()
avg_humidity = df_short["Humidity"].mean()
date_max_temp = df_short.loc[df_short["Temperature"].idxmax(), "dt_txt"]
date_min_temp = df_short.loc[df_short["Temperature"].idxmin(), "dt_txt"]
most_common_condition = (
    df_short["Condition"].mode().iloc[0] if not df_short["Condition"].isna().all() else "N/A"
)
rainy_periods = (df_short["Condition"] == "Rain").sum()
cloudy_periods = (df_short["Condition"] == "Clouds").sum()

summary = pd.DataFrame(
    {
        "Average Temp (°C)": [avg_temp],
        "Max Temp (°C)": [max_temp],
        "Min Temp (°C)": [min_temp],
        "Average Humidity (%)": [avg_humidity],
        "Date of Max Temp": [date_max_temp],
        "Date of Min Temp": [date_min_temp],
        "Rainy Periods": [rainy_periods],
        "Cloudy Periods": [cloudy_periods],
        "Most Frequent Condition": [most_common_condition],
    }
)

print("\n📊 Key Weather Statistics:")
print(summary.to_string(index=False))

# -----------------------------
# 7. Save CSV
# -----------------------------
output_file = "chennai_forecast.csv"
df_short.to_csv(output_file, index=False)
print(f"\n💾 Data saved to {output_file}")
5
