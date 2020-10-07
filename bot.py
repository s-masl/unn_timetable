import telebot
import config
import function
import date
from bottons import bottons


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /start')
    bot.send_message(chat_id=message.chat.id, text='Узнать расписание нa /', reply_markup=bottons)


@bot.message_handler(commands=['today'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /today')
    bot.send_message(message.chat.id, function.timeTable(date.today()), reply_markup=bottons)


@bot.message_handler(commands=['tomorrow'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /tomorrow')
    bot.send_message(message.chat.id, function.timeTable(date.tomorrow()), reply_markup=bottons)


@bot.message_handler(commands=['other_day'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /other_day')
    bot.send_message(message.chat.id, text=config.tutorial, reply_markup=bottons)


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: {message.text}')
    bot.send_message(message.chat.id, function.timeTable(message.text), reply_markup=bottons)


bot.polling(none_stop=True)
