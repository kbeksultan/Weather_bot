from constants import TOKEN, WEATHERAPI, APPID, photos, cities
from messages import HELLO, CHOOSE, DEVELOPERS, COMMANDS
from telebot import types
import telebot
import requests
import time

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, " +
                     message.from_user.first_name + HELLO)
    bot.send_message(message.chat.id, CHOOSE)
    bot.send_message(message.chat.id, "Press: /help to show commands")


@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.chat.id, COMMANDS)


@bot.message_handler(commands=['dev'])
def developers(message):
    bot.send_message(message.chat.id, DEVELOPERS)


@bot.message_handler(commands=['city'])
def get_city(message):
    photo = '{}'.format(photos['Kazakhstan'])
    markup = types.ReplyKeyboardMarkup(row_width=4)
    markup.row(*cities[-4:])
    markup.row(*cities[7:10])
    markup.row(*cities[3:7])
    markup.row(*cities[:3])
    bot.send_photo(message.chat.id, photo, caption="Here the list of Kazakhstan Cities", reply_markup=markup)


@bot.message_handler(regexp='[A-Za-z]')
def send_weather(message):
    city = message.text
    f = open("history.txt", "a")
    text = "{} wanted {}. UserID: {}\n".format(
        message.from_user.first_name, message.text, message.from_user.id)
    f.write(text)
    f.close()
    if city in cities:
        photo = '{}'.format(photos[city])
        r = requests.get(WEATHERAPI.format(city, APPID))
        text = r.json()
        weather = (text['weather'][0]['description'])
        temp_c = int(text['main']['temp']) - 273
        pres = int(text['main']['pressure'])
        hum = int(text['main']['humidity'])
        vis = int(text['visibility'])
        wind = int(text['wind']['speed'])
        sunrise = int(text['sys']['sunrise'])
        sunset = int(text['sys']['sunset'])
        bot.send_photo(message.chat.id, photo, caption =  "Weather: " + weather + "\nTemp: " + str(temp_c) + " °С" +
                         "\nPressure: " + str(pres) + " Pa" + "\nHumidity: " + str(hum) + " %" + "\nVisibility: " + str(
            vis) + " m" +
            "\nWind Speed: " + str(wind) + " km/h" + "\nSunrise: " + str(
            time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunrise))) +
            "\nSunset: " + str(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(sunset))))


if __name__ == '__main__':
    print('Starting WeatherBot')
bot.polling()
