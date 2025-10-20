
# Weather API Integration

## 📋 Project Description
A Python application that integrates with the OpenWeatherMap API to fetch and display real-time weather data for any city in the world. Features both command-line and GUI interfaces.

## ✨ Features
- ✅ Real-time weather data fetching
- ✅ Temperature, humidity, wind speed display
- ✅ Weather conditions and descriptions
- ✅ City search functionality
- ✅ Error handling for invalid cities and API failures
- ✅ Beautiful GUI with weather icons
- ✅ Temperature conversion (Celsius/Fahrenheit)
- ✅ User-friendly interface

## 🛠️ Technologies Used
- Python 3.x
- `requests` library for API calls
- `tkinter` for GUI
- OpenWeatherMap API
- JSON data parsing

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/codveda-python-internship.git
cd codveda-python-internship/Level-2-API-Integration
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Get your free API key:
   - Visit https://openweathermap.org/api
   - Sign up for a free account
   - Copy your API key

4. Create a `config.py` file:
```python
API_KEY = "replace with your api key"
```

## 🚀 Usage

### Command-Line Version:
```bash
python weather_cli.py
```

### GUI Version:
```bash
python weather_gui.py
```

## 📸 Screenshots
![Weather App Screenshot](screenshot.png)
*Weather Application GUI Interface*

## 🎯 API Endpoints Used
- Current Weather Data: `https://api.openweathermap.org/data/2.5/weather`

## 🎯 Learning Outcomes
- Making GET requests to external APIs
- Parsing JSON responses
- Error handling for API failures
- Working with environment variables
- User input validation
- GUI development with real-time data

## ⚠️ Important Notes
- Keep your API key secure (never commit it to GitHub)
- Free tier has rate limits (60 calls/minute)
- API key activation may take a few minutes

## 👨‍💻 Author
**Duncan Kimuli Kigozi**
- Internship: Codveda Technology
- LinkedIn: https://www.linkedin.com/in/duncan-kigozi-101923215
- GitHub: https://github.com/DoneKan

## 📝 License
This project is part of the Codveda Technology Python Development Internship.

---

**#CodvedaJourney #CodvedaExperience #PythonDevelopment #APIIntegration**
