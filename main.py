from constants import TOKEN
from messages import HELLO,asd,Developers,Commands
from telebot import types
import database
import telebot
import requests
import time
#weatherbot

bot = telebot.TeleBot(TOKEN)

markup  = types.ReplyKeyboardMarkup(row_width=4)
itembtn1 = types.KeyboardButton('Almaty')
itembtn2 = types.KeyboardButton('Astana')
itembtn3 = types.KeyboardButton('Pavlodar')
itembtn4 = types.KeyboardButton('Atyrau')
itembtn5 = types.KeyboardButton('Aktau')
itembtn6 = types.KeyboardButton('Semey')
itembtn7 = types.KeyboardButton('Petropavlosk')
itembtn8 = types.KeyboardButton('Shymkent')
itembtn9 = types.KeyboardButton('Karaganda')
itembtn10 = types.KeyboardButton('Aktobe')
itembtn11 = types.KeyboardButton('Kyzyl-Orda')
itembtn12 = types.KeyboardButton('Oskemen')
itembtn13 = types.KeyboardButton('Uralsk')
itembtn14 = types.KeyboardButton('Taraz')
markup.row(itembtn14,itembtn13,itembtn12,itembtn11)
markup.row(itembtn10,itembtn9,itembtn8,itembtn7)
markup.row(itembtn6,itembtn5,itembtn4,itembtn2)
markup.row(itembtn3,itembtn1)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hello, " + message.from_user.first_name + HELLO)
	bot.send_message(message.chat.id, asd)
	bot.send_message(message.chat.id, "Press: /help to show commands")

@bot.message_handler(commands = ['help'])
def help_user(message):
	bot.send_message(message.chat.id,Commands)

@bot.message_handler(commands= ['dev'])
def developers(message):
	bot.send_message(message.chat.id,Developers)

@bot.message_handler(commands=['city'])
def get_city(message):
	photo = open('photos/kaz.jpg', 'rb')
	bot.send_message(message.chat.id,"Here the list of Kazakhstan Cities",reply_markup= markup)
	bot.send_photo(message.chat.id,photo)
	photo.close()


@bot.message_handler(regexp = 'Pavlodar')
def Pavlodar(message):
	photo = open('photos/Pavlodar.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=Pavlodar&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Almaty')
def Almaty(message):
	photo = open('photos/almaty.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=Almaty&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Astana')
def Astana(message):
	photo = open('photos/astana.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=Astana&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	wea = int(text['clouds']['all'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Atyrau')
def Atyrau(message):
	photo = open('photos/atyrau.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=atyrau&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Aktau')
def Aktau(message):
	photo = open('photos/Aktau.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=Aktau&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Semey')
def Semey(message):
	photo = open('photos/Semey.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=semey&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Petropavlosk')
def Petropavlosk(message):
	photo = open('photos/Petr.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=petropavl&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	wea = int(text['clouds']['all'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Shymkent')
def Shymkent(message):
	photo = open('photos/shymkent.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=shymkent&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Karaganda')
def Karaganda(message):
	photo = open('photos/karaganda.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=karaganda&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Aktobe')
def Aktobe(message):
	photo = open('photos/aktobe.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=aktobe&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Kyzyl-Orda')
def KyzylOrda(message):
	photo = open('photos/kyzylorda.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=kyzylorda&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Oskemen')
def Oskemen(message):
	photo = open('photos/oskemen.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=oskemen&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Uralsk')
def Uralsk(message):
	photo = open('photos/uralsk.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=oral&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

@bot.message_handler(regexp = 'Taraz')
def Taraz(message):
	photo = open('photos/taraz.jpg','rb')
	bot.send_photo(message.chat.id,photo)
	r = requests.get('http://openweathermap.org/data/2.5/weather?q=taraz&appid=b6907d289e10d714a6e88b30761fae22')
	text = r.json()
	weather = (text['weather'][0]['description'])
	temp_c = int(text['main']['temp'])
	pres = int(text['main']['pressure'])
	hum = int(text['main']['humidity'])
	vis = int(text['visibility'])
	wind = int(text['wind']['speed'])
	sunrise = int(text['sys']['sunrise'])
	sunset =  int(text['sys']['sunset'])
	bot.send_message(message.chat.id,"Weather: " + weather +"\nTemp: "+str(temp_c)+" *C"+
	"\nPressure: "+str(pres)+" Pa" + "\nHumidity: "+ str(hum)+ " %" +"\nVisibility: "+str(vis)+ " m" +
	"\nWind Speed: "+str(wind)+" km/h" + "\nSunrise :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
	"\nSunset :"+ str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))
	photo.close()

if __name__ == '__main__':
    print('Starting WeatherBot')
bot.polling()

			
