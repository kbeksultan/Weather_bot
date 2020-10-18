import os
TOKEN = os.getenv("TOKEN")
APPID = os.getenv("APPID")

WEATHERAPI = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'