from telebot import types

def send_sporthall_buttons(bot, chat_id):
    # Creates a keyboard with sports options
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('GYM')
    btn2 = types.KeyboardButton('Swimming Pool')
    btn3 = types.KeyboardButton('Ping Pong')
    btn_back = types.KeyboardButton('Back to Main Menu')
    markup.add(btn1, btn2, btn3)
    markup.add(btn_back)

    bot.send_message(
        chat_id,
        "Choose an option for the Sport Hall:",
        reply_markup=markup
    )

def get_schedule_sporthall(option):
    schedules = {
        "GYM": "<b>9:00-13:00</b>, <b>14:00-18:00</b> you can enter\nMonday - Friday",
        "Swimming Pool": "<b>9:00-13:00</b>, <b>14:00-18:00</b> you can enter\nMonday - Friday\n"
                         "<b>Warning:</b> Males can enter on <b>Monday, Wednesday, and Friday</b> from <b>14:00 - 18:00</b>\n"
                         "On <b>Tuesday</b> and <b>Thursday</b>, entry is from <b>9:00 - 12:50</b>",
        "Ping Pong": "<b>9:00-13:00</b>, <b>14:00-18:00</b> you can enter"
    }
    return schedules.get(option, "No schedule available for this option.")

def register_sporthall_handlers(bot):
    @bot.message_handler(func=lambda message: message.text in ["GYM", "Swimming Pool", "Ping Pong"])
    def handle_sporthall_option(message):
        schedule = get_schedule_sporthall(message.text)
        bot.send_message(message.chat.id, schedule, parse_mode='HTML')
