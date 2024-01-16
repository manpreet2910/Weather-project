import requests
from dotenv import load_dotenv
import os

load_dotenv()

class City:
    def __init__(self, name, units="metric"):
        self.name = name
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        
        try:
            responsel = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={self.name}&count=1&language=en&format=json")
        except:
            print("No Internet Access..!!")
            
        responsejso = responsel.json()
        self.lat = responsejso["results"][0]["latitude"]
        self.lan = responsejso["results"][0]["longitude"]
        self.units = units
        self.mydata(api_key)

    def mydata(self, api_key):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lan}&appid={api_key}")
        except:
            print("No Internet Access..!!")
            
        self.responsejs = response.json()
        self.temp = self.responsejs["main"]["temp"]
        self.pres = self.responsejs["main"]["pressure"]
        self.wind = self.responsejs["wind"]["speed"]
        self.cloud = self.responsejs["clouds"]["all"]
        self.weather = self.responsejs["weather"][0]["description"]
        self.humid = self.responsejs["main"]["humidity"]

    def tempprint(self):
        unitsymbol = "C"
        if self.units == "imperial":
            unitsymbol = "F"
        print(f"Current temperature: {self.temp} {unitsymbol}")
        print(f"Current weather: {self.weather}")
        print(f"Humidity: {self.humid}%")
        print(f"Cloudiness: {self.cloud}%")
        print(f"Wind speed: {self.wind} meter/second")
        print(f"Pressure: {self.pres} hPa")

# Get the city name from user input
city_name = input("Enter city name: ")
city_instance = City(city_name)
city_instance.tempprint()
