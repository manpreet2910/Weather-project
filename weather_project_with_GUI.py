import requests
from tkinter import Tk, Label, Entry, Button, StringVar
from dotenv import load_dotenv
import os

load_dotenv()

class CityWeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x300")

        self.city_label = Label(root, text="Enter City:")
        self.city_label.pack()

        self.city_entry = Entry(root)
        self.city_entry.pack()

        self.result_var = StringVar()
        self.result_label = Label(root, textvariable=self.result_var)
        self.result_label.pack()

        self.fetch_button = Button(root, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack()

    def fetch_weather(self):
        city_name = self.city_entry.get()
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        if city_name:
            try:
                response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json")
                response_json = response.json()
                latitude = response_json["results"][0]["latitude"]
                longitude = response_json["results"][0]["longitude"]

                units = "metric"
                response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={units}&lat={latitude}&lon={longitude}&appid={api_key}")
                responsejs = response.json()

                temperature = responsejs["main"]["temp"]
                weather = responsejs["weather"][0]["description"]
                humidity = responsejs["main"]["humidity"]
                wind = responsejs["wind"]["speed"]
                cloud=responsejs["clouds"]["all"]
                pres=responsejs["main"]["pressure"]


                result_text = f"Temperature: {temperature}°C\nWeather: {weather}\nHumidity: {humidity}%\nPressure: {pres} hPa\nCloudiness: {cloud}%\nWind Speed: {wind} meter/second"
                self.result_var.set(result_text)
            except Exception as e:
                self.result_var.set(f"Error fetching weather: {str(e)}")
        else:
            self.result_var.set("Please enter a city name")

if __name__ == "__main__":
    root = Tk()
    app = CityWeatherApp(root)
    root.mainloop()
