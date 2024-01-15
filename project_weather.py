import requests 
class City:
    def __init__(self,name,units="metric"):
        self.name=name
        try:
            responsel=requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={self.name}&count=1&language=en&format=json")
        except:
            print("No Internet Access...!!!")
        responsejso= responsel.json()
        self.lat= responsejso["results"][0]["latitude"] 
        self.lan= responsejso["results"][0]["longitude"] 
        self.units= units
        self.mydata()
    def mydata(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lan}&appid=3ea29c60c26ec5ae28dad8c4827c79f6")
        except:
            print("No Internet Access..!!!")
        self.responsejs= response.json()
        self.temp=self.responsejs["main"]["temp"]
        self.pres= self.responsejs["main"]["pressure"]
        self.wind=self.responsejs["wind"]["speed"]
        self.cloud=self.responsejs["clouds"]["all"]
        self.weather=self.responsejs["weather"][0]["description"]
        self.humid=self.responsejs["main"]["humidity"]
    def tempprint(self):
        unitsymbol="C"
        if self.units=="imperial":
            unitsymbol="F"
        print(f"Current temperature: {self.temp} {unitsymbol}")
        print(f"Current weather: {self.weather}")
        print(f"Humidity: {self.humid}%")
        print(f"Cloudiness: {self.cloud}%")
        print(f"Wind speed: {self.wind} meter/second")
        print(f"Pressure: {self.pres} hPa")
cityname= input("Enter city name: ")
ncity= City(cityname)
ncity.tempprint()