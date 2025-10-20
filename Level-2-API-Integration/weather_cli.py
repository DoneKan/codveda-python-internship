"""
Weather API Integration - Command Line Interface
Codveda Technology - Python Development Internship
Task: Level 2 - API Integration

Fetches and displays real-time weather data using OpenWeatherMap API
"""

import requests
import sys
from datetime import datetime

# Import configuration
try:
    from config import API_KEY, BASE_URL, DEFAULT_UNITS, TIMEOUT
except ImportError:
    print("❌ Error: config.py not found!")
    print("📝 Please create config.py with your API key.")
    print("   Visit: https://openweathermap.org/api to get a free API key")
    sys.exit(1)

# Weather emoji mapping
WEATHER_EMOJIS = {
    'clear': '☀️',
    'clouds': '☁️',
    'rain': '🌧️',
    'drizzle': '🌦️',
    'thunderstorm': '⛈️',
    'snow': '🌨️',
    'mist': '🌫️',
    'fog': '🌫️',
    'haze': '🌫️'
}

def get_weather_emoji(weather_main):
    """Get emoji for weather condition"""
    return WEATHER_EMOJIS.get(weather_main.lower(), '🌡️')

def fetch_weather(city_name):
    """
    Fetch weather data from OpenWeatherMap API
    
    Args:
        city_name (str): Name of the city
        
    Returns:
        dict: Weather data or None if request fails
    """
    try:
        # Prepare API request parameters
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': DEFAULT_UNITS
        }
        
        # Make GET request to API
        print(f"\n🔄 Fetching weather data for {city_name}...")
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("❌ Error: Invalid API key!")
            print("📝 Please check your API key in config.py")
            return None
        elif response.status_code == 404:
            print(f"❌ Error: City '{city_name}' not found!")
            print("📝 Please check the spelling and try again.")
            return None
        else:
            print(f"❌ Error: API request failed with status code {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out!")
        print("📝 Please check your internet connection and try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: Connection failed!")
        print("📝 Please check your internet connection.")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def display_weather(data):
    """
    Display weather data in a user-friendly format
    
    Args:
        data (dict): Weather data from API
    """
    if not data:
        return
    
    # Extract data
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    weather_main = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description'].capitalize()
    wind_speed = data['wind']['speed']
    clouds = data['clouds']['all']
    
    # Get sunrise and sunset times
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')
    
    # Get weather emoji
    emoji = get_weather_emoji(weather_main)
    
    # Display formatted weather information
    print("\n" + "="*60)
    print(f"🌍  WEATHER REPORT: {city}, {country}  {emoji}".center(60))
    print("="*60)
    
    print(f"\n📊 Current Conditions:")
    print(f"   Weather: {weather_desc} {emoji}")
    print(f"   Temperature: {temp}°C")
    print(f"   Feels Like: {feels_like}°C")
    print(f"   Min/Max: {temp_min}°C / {temp_max}°C")
    
    print(f"\n💧 Atmospheric Conditions:")
    print(f"   Humidity: {humidity}%")
    print(f"   Pressure: {pressure} hPa")
    print(f"   Cloud Cover: {clouds}%")
    
    print(f"\n💨 Wind:")
    print(f"   Speed: {wind_speed} m/s")
    
    print(f"\n🌅 Sun:")
    print(f"   Sunrise: {sunrise}")
    print(f"   Sunset: {sunset}")
    
    print("\n" + "="*60)
    
    # Temperature conversion option
    temp_f = (temp * 9/5) + 32
    print(f"\n💡 Tip: {temp}°C = {temp_f:.1f}°F")
    print("="*60 + "\n")

def main():
    """Main function to run the weather app"""
    print("\n" + "="*60)
    print("🌤️  WEATHER APP - API INTEGRATION  🌤️".center(60))
    print("="*60)
    print("\n📍 Powered by OpenWeatherMap API")
    print("🔗 Codveda Technology - Python Internship\n")
    
    # Check if API key is configured
    if API_KEY == "DoneKan":
        print("❌ Error: API key not configured!")
        print("\n📝 Please follow these steps:")
        print("   1. Visit: https://openweathermap.org/api")
        print("   2. Sign up for a free account")
        print("   3. Get your API key")
        print("   4. Add it to config.py\n")
        return
    
    while True:
        try:
            # Get city name from user
            city = input("🏙️  Enter city name (or 'quit' to exit): ").strip()
            
            if city.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using Weather App! Goodbye! 👋\n")
                break
            
            if not city:
                print("❌ City name cannot be empty!")
                continue
            
            # Fetch and display weather
            weather_data = fetch_weather(city)
            if weather_data:
                display_weather(weather_data)
            
            # Ask if user wants to check another city
            another = input("❓ Check another city? (y/n): ").strip().lower()
            if another != 'y':
                print("\n👋 Thank you for using Weather App! Goodbye! 👋\n")
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using Weather App! Goodbye! 👋\n")
            break

if __name__ == "__main__":
    main()
