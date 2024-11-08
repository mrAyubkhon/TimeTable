import telebot
from telebot import types
import CS1
import CS2
import CS3
import CS4
import CS5
import SportHall

bot = telebot.TeleBot('7365761529:AAGeLl5-88qaJEMF3dQAJp78JNet-ImrtLA')

@bot.message_handler(commands=['start'])
def start(message):
    # Main menu with buttons
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Wassup Button')
    btn2 = types.KeyboardButton('CS1')
    btn3 = types.KeyboardButton('CS2')
    btn4 = types.KeyboardButton('CS3')
    btn5 = types.KeyboardButton('CS4')
    btn6 = types.KeyboardButton('CS5')
    btn7 = types.KeyboardButton('Sport Hall')
    btn8 = types.KeyboardButton('EduPlus website')
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)
    markup.add(btn6)
    markup.add(btn7, btn8)

    bot.send_message(
        message.chat.id,
        f'Hi, how can I help you, miss/mister {message.from_user.first_name} {message.from_user.last_name}. '
        f'Choose a group or activity:',
        parse_mode='HTML', reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == 'Wassup Button')
def wassup(message):
    bot.send_message(message.chat.id, f"Wassup, {message.from_user.first_name}")

# Handlers for each group
@bot.message_handler(func=lambda message: message.text == 'CS1')
def cs1_options(message):
    CS1.send_cs1_buttons(bot, message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'CS2')
def cs2_options(message):
    CS2.send_cs2_buttons(bot, message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'CS3')
def cs3_options(message):
    CS3.send_cs3_buttons(bot, message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'CS4')
def cs4_options(message):
    CS4.send_cs4_buttons(bot, message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'CS5')
def cs5_options(message):
    CS5.send_cs5_buttons(bot, message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'Sport Hall')
def sporthall_options(message):
    SportHall.send_sporthall_buttons(bot, message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'Back to Main Menu')
def back_to_main_menu(message):
    start(message)

# Register sport hall handlers
SportHall.register_sporthall_handlers(bot)

@bot.message_handler(func=lambda message: message.text.startswith('CS1 '))
def send_schedule_cs1(message):
    day = message.text.split()[1]
    schedule = CS1.get_schedule_cs1(day)
    bot.send_message(message.chat.id, schedule, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text.startswith('CS2 '))
def send_schedule_cs2(message):
    day = message.text.split()[1]
    schedule = CS2.get_schedule_cs2(day)
    bot.send_message(message.chat.id, schedule, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text.startswith('CS3 '))
def send_schedule_cs3(message):
    day = message.text.split()[1]
    schedule = CS3.get_schedule_cs3(day)
    bot.send_message(message.chat.id, schedule, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text.startswith('CS4 '))
def send_schedule_cs4(message):
    day = message.text.split()[1]
    schedule = CS4.get_schedule_cs4(day)
    bot.send_message(message.chat.id, schedule, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text.startswith('CS5 '))
def send_schedule_cs5(message):
    day = message.text.split()[1]
    schedule = CS5.get_schedule_cs5(day)
    bot.send_message(message.chat.id, schedule, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == 'EduPlus website')
def site(message):
    bot.send_message(message.chat.id, "Here is the link to the EduPlus: https://lms.eduplus.uz/login")

bot.polling(none_stop=True)
