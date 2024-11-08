from telebot import types

def send_cs1_buttons(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('CS1 Monday')
    btn2 = types.KeyboardButton('CS1 Tuesday')
    btn3 = types.KeyboardButton('CS1 Wednesday')
    btn4 = types.KeyboardButton('CS1 Thursday')
    btn5 = types.KeyboardButton('CS1 Friday')
    btn_back = types.KeyboardButton('Back to Main Menu')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    markup.add(btn_back)

    bot.send_message(chat_id, "Choose an option for CS1:", reply_markup=markup)

def get_schedule_cs1(day):
    schedules = {
        "Monday": "9:30-10:50 Statistics for Data Science in 205 room\n"
                  "11:00-12:20 Software Engineering in 104 room\n "
                  "13:30-14:50 Algorithms in 202 room",

        "Tuesday": "9:30-10:50 Software Engineering in 202 room\n"
                   "11:00-12:20 Physics CS in 205 room",

        "Wednesday": "9:30-10:50 Software Engineering in 102 room\n"
                     "11:00-12:20 Physics CS in 105 room\n"
                     "13:30-14:50 Algorithms in PC 312",

        "Thursday": "9:30-10:50 Algorithms in PC 309\n"
                    "11:00-12:20 Statistics for Data Science in 117 room",

        "Friday": "9:30-10:50 Statistics for Data Science in 304 room\n"
                  "11:00-12:20 Physics CS in 412 room"
    }
    return schedules.get(day, "No schedule available for this day.")
