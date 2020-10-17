from telebot import types

buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
today = types.KeyboardButton(text='/today')
tomorrow = types.KeyboardButton(text='/tomorrow')
other_day = types.KeyboardButton(text='/other_day')

buttons.add(today, tomorrow, other_day)

markup_inline = types.InlineKeyboardMarkup()
item0 = types.InlineKeyboardButton(text='382003-0', callback_data='28659')
item1 = types.InlineKeyboardButton(text='382003-1', callback_data='28655')
item2 = types.InlineKeyboardButton(text='382003-2', callback_data='28656')
item3 = types.InlineKeyboardButton(text='382003-3', callback_data='28657')
item4 = types.InlineKeyboardButton(text='382003-4', callback_data='28658')
item5 = types.InlineKeyboardButton(text='382003-1м', callback_data='29799')
item6 = types.InlineKeyboardButton(text='382003-2м', callback_data='29794')
item7 = types.InlineKeyboardButton(text='382003-3м', callback_data='29798')
item8 = types.InlineKeyboardButton(text='382003-4м', callback_data='29800')
item9 = types.InlineKeyboardButton(text='382003-в1', callback_data='28713')
item10 = types.InlineKeyboardButton(text='382003-в2', callback_data='28714')


markup_inline.add(item0, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
