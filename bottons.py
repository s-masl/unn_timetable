from telebot import types

bottons = types.ReplyKeyboardMarkup(resize_keyboard= True)
today = types.KeyboardButton(text='/today')
tommorow = types.KeyboardButton(text='/tommorow')
other_day = types.KeyboardButton(text='/other_day')
bottons.add(today, tommorow, other_day)