"""
Weather API Integration - GUI Version with Tkinter
Codveda Technology - Python Development Internship
Task: Level 2 - API Integration

Beautiful weather application with graphical interface
"""

import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
import sys

# Import configuration
try:
    from config import API_KEY, BASE_URL, DEFAULT_UNITS, TIMEOUT
except ImportError:
    print("❌ Error: config.py not found!")
    print("📝 Please create config.py with your API key.")
    sys.exit(1)

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App - Codveda")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e3a5f")
        
        # Check API key
        if API_KEY == "your_api_key_here":
            messagebox.showerror(
                "Configuration Error",
                "API key not configured!\n\nPlease:\n"
                "1. Visit https://openweathermap.org/api\n"
                "2. Sign up for free\n"
                "3. Add your API key to config.py"
            )
            root.destroy()
            return
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create all UI widgets"""
        
        # Header
        header_frame = tk.Frame(self.root, bg="#1e3a5f")
        header_frame.pack(pady=20)
        
        title = tk.Label(
            header_frame,
            text="🌤️ WEATHER APP",
            font=("Arial", 24, "bold"),
            bg="#1e3a5f",
            fg="#ffffff"
        )
        title.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="Real-time Weather Information",
            font=("Arial", 10),
            bg="#1e3a5f",
            fg="#b0c4de"
        )
        subtitle.pack()
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg="#1e3a5f")
        search_frame.pack(pady=20, padx=30, fill=tk.X)
        
        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            bg="#2c5282",
            fg="#ffffff",
            insertbackground="#ffffff",
            bd=0,
            relief=tk.FLAT
        )
        self.city_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=10, padx=(0, 10))
        self.city_entry.insert(0, "Enter city name...")
        self.city_entry.bind("<FocusIn>", self.clear_placeholder)
        self.city_entry.bind("<FocusOut>", self.restore_placeholder)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())
        
        search_btn = tk.Button(
            search_frame,
            text="🔍 Search",
            font=("Arial", 12, "bold"),
            bg="#4299e1",
            fg="#ffffff",
            activebackground="#3182ce",
            activeforeground="#ffffff",
            bd=0,
            cursor="hand2",
            command=self.get_weather,
            padx=20,
            pady=10
        )
        search_btn.pack(side=tk.RIGHT)
        
        # Weather Display Frame
        self.weather_frame = tk.Frame(self.root, bg="#2c5282", bd=0)
        self.weather_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        # Initial message
        self.show_initial_message()
        
        # Footer
        footer = tk.Label(
            self.root,
            text="#CodvedaJourney | Python Internship | Powered by OpenWeatherMap",
            font=("Arial", 8),
            bg="#1e3a5f",
            fg="#64748b"
        )
        footer.pack(pady=10)
    
    def clear_placeholder(self, event):
        """Clear placeholder text on focus"""
        if self.city_entry.get() == "Enter city name...":
            self.city_entry.delete(0, tk.END)
            self.city_entry.config(fg="#ffffff")
    
    def restore_placeholder(self, event):
        """Restore placeholder text if empty"""
        if not self.city_entry.get():
            self.city_entry.insert(0, "Enter city name...")
            self.city_entry.config(fg="#b0c4de")
    
    def show_initial_message(self):
        """Show initial welcome message"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        msg_frame = tk.Frame(self.weather_frame, bg="#2c5282")
        msg_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        icon = tk.Label(
            msg_frame,
            text="🌍",
            font=("Arial", 60),
            bg="#2c5282"
        )
        icon.pack()
        
        msg = tk.Label(
            msg_frame,
            text="Search for a city to see weather",
            font=("Arial", 12),
            bg="#2c5282",
            fg="#b0c4de"
        )
        msg.pack(pady=10)
    
    def show_loading(self):
        """Show loading animation"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        loading_frame = tk.Frame(self.weather_frame, bg="#2c5282")
        loading_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        loading = tk.Label(
            loading_frame,
            text="🔄 Loading...",
            font=("Arial", 16),
            bg="#2c5282",
            fg="#ffffff"
        )
        loading.pack()
        
        self.root.update()
    
    def get_weather(self):
        """Fetch and display weather data"""
        city = self.city_entry.get().strip()
        
        if not city or city == "Enter city name...":
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        self.show_loading()
        
        try:
            # API request
            params = {
                'q': city,
                'appid': API_KEY,
                'units': DEFAULT_UNITS
            }
            
            response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 404:
                self.show_error(f"City '{city}' not found!\nPlease check the spelling.")
            elif response.status_code == 401:
                self.show_error("Invalid API key!\nPlease check config.py")
            else:
                self.show_error(f"Error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            self.show_error("Request timed out!\nCheck your internet connection.")
        except requests.exceptions.ConnectionError:
            self.show_error("Connection failed!\nCheck your internet connection.")
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def show_error(self, message):
        """Show error message"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        error_frame = tk.Frame(self.weather_frame, bg="#2c5282")
        error_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        icon = tk.Label(
            error_frame,
            text="❌",
            font=("Arial", 50),
            bg="#2c5282"
        )
        icon.pack()
        
        msg = tk.Label(
            error_frame,
            text=message,
            font=("Arial", 11),
            bg="#2c5282",
            fg="#ff6b6b",
            justify="center"
        )
        msg.pack(pady=10)
    
    def display_weather(self, data):
        """Display weather information"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Extract data
        city = data['name']
        country = data['sys']['country']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        temp_min = round(data['main']['temp_min'])
        temp_max = round(data['main']['temp_max'])
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_main = data['weather'][0]['main']
        weather_desc = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']
        clouds = data['clouds']['all']
        
        # Weather emoji
        weather_emojis = {
            'Clear': '☀️', 'Clouds': '☁️', 'Rain': '🌧️',
            'Drizzle': '🌦️', 'Thunderstorm': '⛈️',
            'Snow': '🌨️', 'Mist': '🌫️', 'Fog': '🌫️'
        }
        emoji = weather_emojis.get(weather_main, '🌡️')
        
        # Main display
        main_frame = tk.Frame(self.weather_frame, bg="#2c5282")
        main_frame.pack(pady=30)
        
        # Location
        location = tk.Label(
            main_frame,
            text=f"📍 {city}, {country}",
            font=("Arial", 18, "bold"),
            bg="#2c5282",
            fg="#ffffff"
        )
        location.pack()
        
        # Weather emoji and description
        weather_emoji = tk.Label(
            main_frame,
            text=emoji,
            font=("Arial", 70),
            bg="#2c5282"
        )
        weather_emoji.pack(pady=10)
        
        description = tk.Label(
            main_frame,
            text=weather_desc,
            font=("Arial", 14),
            bg="#2c5282",
            fg="#b0c4de"
        )
        description.pack()
        
        # Temperature
        temp_frame = tk.Frame(main_frame, bg="#2c5282")
        temp_frame.pack(pady=15)
        
        temp_label = tk.Label(
            temp_frame,
            text=f"{temp}°C",
            font=("Arial", 50, "bold"),
            bg="#2c5282",
            fg="#ffffff"
        )
        temp_label.pack()
        
        feels = tk.Label(
            temp_frame,
            text=f"Feels like {feels_like}°C",
            font=("Arial", 11),
            bg="#2c5282",
            fg="#b0c4de"
        )
        feels.pack()
        
        # Details grid
        details_frame = tk.Frame(self.weather_frame, bg="#2c5282")
        details_frame.pack(pady=20, padx=40, fill=tk.X)
        
        details = [
            ("🌡️ Min/Max", f"{temp_min}°C / {temp_max}°C"),
            ("💧 Humidity", f"{humidity}%"),
            ("🌪️ Pressure", f"{pressure} hPa"),
            ("💨 Wind", f"{wind_speed} m/s"),
            ("☁️ Clouds", f"{clouds}%")
        ]
        
        for i, (label, value) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_frame = tk.Frame(details_frame, bg="#1e3a5f", bd=0)
            detail_frame.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            
            lbl = tk.Label(
                detail_frame,
                text=label,
                font=("Arial", 10),
                bg="#1e3a5f",
                fg="#b0c4de",
                anchor="w"
            )
            lbl.pack(fill=tk.X, padx=10, pady=(5, 0))
            
            val = tk.Label(
                detail_frame,
                text=value,
                font=("Arial", 12, "bold"),
                bg="#1e3a5f",
                fg="#ffffff",
                anchor="w"
            )
            val.pack(fill=tk.X, padx=10, pady=(0, 5))
        
        details_frame.columnconfigure(0, weight=1)
        details_frame.columnconfigure(1, weight=1)

def main():
    """Main function to run the weather app"""
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
