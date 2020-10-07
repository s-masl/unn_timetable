import telebot

you_token = '1239700114:AAErIGLaNKqaJUgB9NCXkOA9QY7yD8pnBcU'

bot = telebot.TeleBot(you_token)


bot.send_message(chat_id='-1001293756633', text='hello world')

