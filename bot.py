import telebot
import config
import function
import date
from bottons import bottons


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text='Узнать расписание нa /', reply_markup=bottons)


@bot.message_handler(commands=['today'])
def answer(message):
    bot.send_message(message.chat.id, function.timeTable(date.today), reply_markup=bottons)


@bot.message_handler(commands=['tommorow'])
def answer(message):
    bot.send_message(message.chat.id, function.timeTable(date.tommorow), reply_markup=bottons)


@bot.message_handler(commands=['other_day'])
def answer(message):
    bot.send_message(message.chat.id, text=config.tutorial, reply_markup=bottons)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, function.timeTable(message.text), reply_markup=bottons)


bot.polling(none_stop=True)
