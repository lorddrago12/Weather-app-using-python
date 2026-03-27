# 🌤️ Weather App

A simple command-line Python application that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## 📋 Features

- Get current weather conditions for any city worldwide
- Displays temperature in **Celsius**
- Handles invalid or misspelled city names gracefully

---

## 🛠️ Prerequisites

- Python 3.x
- `requests` library
- An [OpenWeatherMap API key](https://home.openweathermap.org/users/sign_up) (free tier works)

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/lorddrago12/DA-Card.git
   cd DA-Card
   ```

2. **Install dependencies**

   ```bash
   pip install requests
   ```

3. **Add your API key**

   Open `Weather_app.py` and replace the placeholder with your own key:

   ```python
   api_key = 'your_api_key_here'
   ```

---

## 🚀 Usage

Run the script from your terminal:

```bash
python Weather_app.py
```

You'll be prompted to enter a city name:

```
Enter city name: Jaipur
The weather in Jaipur is Clear with a temperature of 32°C.
```

If an invalid city is entered:

```
Enter city name: Xyzabc
City not found. Please check the city name and try again.
```

---

## 📁 Project Structure

```
DA-Card/
└── Weather_app.py   # Main application script
```

---

## 🔑 API Reference

This app uses the **OpenWeatherMap Current Weather API**:

```
GET http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric
```

Sign up for a free API key at [openweathermap.org](https://openweathermap.org/api).

---

## ⚠️ Note

Avoid hardcoding your API key in production. Consider using environment variables instead:

```python
import os
api_key = os.getenv('OPENWEATHER_API_KEY')
```

---
