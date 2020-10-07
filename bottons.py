from telebot import types

bottons = types.ReplyKeyboardMarkup(resize_keyboard=True)
today = types.KeyboardButton(text='/today')
tomorrow = types.KeyboardButton(text='/tomorrow')
other_day = types.KeyboardButton(text='/other_day')
bottons.add(today, tomorrow, other_day)