from telebot import types

def send_cs3_buttons(bot, chat_id):
    # Creates a keyboard with CS3 day options, prefixed with 'CS3' for each button
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('CS3 Monday')
    btn2 = types.KeyboardButton('CS3 Tuesday')
    btn3 = types.KeyboardButton('CS3 Wednesday')
    btn4 = types.KeyboardButton('CS3 Thursday')
    btn5 = types.KeyboardButton('CS3 Friday')
    btn_back = types.KeyboardButton('Back to Main Menu')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    markup.add(btn_back)

    bot.send_message(chat_id, "Choose an option for CS3:", reply_markup=markup)

def get_schedule_cs3(day):
    # Schedule for each day with updated rooms
    schedules = {
        "Monday": (
            "9:30-10:50 <b>Statistics for Data Science</b> in <b>205 room</b>\n"
            "11:00-12:20 <b>Software Engineering</b> in <b>104 room</b>\n"
            "13:30-14:50 <b>Algorithms</b> in <b>202 room</b>"
        ),
        "Tuesday": (
            "9:30-10:50 <b>Software Engineering</b> in <b>202 room</b>\n"
            "11:00-12:20 <b>Physics CS</b> in <b>205 room</b>"
        ),
        "Wednesday": (
            "9:30-10:50 <b>Software Engineering</b> in <b>102 room</b>\n"
            "11:00-12:20 <b>Physics CS</b> in <b>105 room</b>"
        ),
        "Thursday": (
            "9:30-10:50 <b>Algorithms</b> in <b>PC 310</b>\n"
            "11:00-12:20 <b>Statistics for Data Science</b> in <b>117 room</b>\n"
            "13:30-14:50 <b>Physics CS</b> in <b>209 room</b>"
        ),
        "Friday": (
            "9:30-10:50 <b>Statistics for Data Science</b> in <b>304 room</b>\n"
            "11:00-12:20 <b>Algorithms</b> in <b>312 room</b>"
        )
    }
    return schedules.get(day, "No schedule available for this day.")
