Chennai Weather Forecast Analysis (OpenWeather API)

Overview:

This Python project fetches **real-time 5-day weather forecast data** for **Chennai, India** using the **OpenWeather API** and visualizes it through temperature and humidity trends.
It’s built to work smoothly in **IDLE (Python 3.x)** without needing Google Colab.

---

 Features:

* Fetches live forecast data from the **OpenWeather REST API**
* Displays temperature and humidity variations over time
* Shows the frequency of weather conditions (e.g., Clear, Rain, Clouds)
* Calculates **key weather KPIs**, including:

  * Average, maximum, and minimum temperature
  * Average humidity
  * Date/time of hottest and coolest forecast periods
  * Most frequent weather condition
  * Rainy and cloudy time slots
* Automatically saves the processed forecast as a CSV file
* Generates multiple line and bar charts with **Matplotlib / Seaborn**

---

 Technologies Used:

| Category             | Library                 |
| -------------------- | ----------------------- |
| Data Processing      | `pandas`, `numpy`       |
| API Requests         | `requests`              |
| Visualization        | `matplotlib`, `seaborn` |
| Environment Handling | `os`, `sys`             |

---

 Setup & Usage:

1️⃣ Install dependencies

```bash
pip install pandas numpy matplotlib requests seaborn
```

2️⃣ Set your OpenWeather API key

Either export it as an environment variable:

```bash
set OPENWEATHER_API_KEY=your_api_key_here      # Windows CMD
```

or paste it directly into the script:

```python
api_key = "your_api_key_here"
```

3️⃣ Run the script

```bash
python chennai_forecast.py
```

or open it in IDLE → press F5 to run.

---

Output:

The program will:

* Print the first few rows of the forecast data
* Generate line plots for Temperature and Humidity
* Generate a bar chart for Weather Condition Frequency
* Display a summary table of KPIs
* Save the complete forecast to a CSV file:

  ```
  chennai_forecast.csv
  ```

---

Example Files Generated:

* `chennai_forecast.py` – main script
* `chennai_forecast.csv` – saved forecast data
* (Optional) PNG graphs if you add `plt.savefig()` in the script

---

Example Output Preview


Future Enhancements:

* Add city input dynamically via command line or GUI
* Include wind speed & pressure analysis
* Automate daily data fetch with task scheduler
* Add historical data comparison

---

 Author:

Anusuya Rajaram
Weather Analytics Project — Powered by Python & OpenWeather API

---
