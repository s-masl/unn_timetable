import telebot
import config
import function
import date
from buttons import buttons, markup_inline


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /start')
    bot.send_message(chat_id=message.chat.id, text='Выберите вашу группу.', reply_markup=markup_inline)


@bot.message_handler(commands=['set_group'])
def process_command_1(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /change_group')
    bot.send_message(chat_id=message.chat.id, text='Выберите вашу группу.', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(call)}\n{function.groupID_to_name(int(call.data))}')
    function.make_user(user_id=call.from_user.id, group_id=call.data)
    bot.send_message(chat_id=call.from_user.id, text=f'Вы выбрали группу {function.groupID_to_name(int(call.data))}.')
    bot.send_message(chat_id=call.from_user.id, text='Чтобы сменить группу используйте комманду /set_group.')
    bot.send_message(chat_id=call.from_user.id, text='Узнать расписание на /', reply_markup=buttons)


@bot.message_handler(commands=['today'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /today')
    bot.send_message(message.chat.id, function.timeTable(date.today(), function.read_user(str(message.chat.id))), reply_markup=buttons)


@bot.message_handler(commands=['tomorrow'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /tomorrow')
    bot.send_message(message.chat.id, function.timeTable(date.tomorrow(), function.read_user(str(message.chat.id))), reply_markup=buttons)


@bot.message_handler(commands=['other_day'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: /other_day')
    bot.send_message(message.chat.id, text=config.tutorial, reply_markup=buttons)


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(chat_id=config.info_id, text=f'{function.getInfo(message)}command: {message.text}')
    bot.send_message(message.chat.id, function.timeTable(message.text, function.read_user(str(message.chat.id))), reply_markup=buttons)


bot.polling(none_stop=True)
