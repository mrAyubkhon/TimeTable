from telebot import types

def send_cs5_buttons(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('CS5 Monday')
    btn2 = types.KeyboardButton('CS5 Tuesday')
    btn3 = types.KeyboardButton('CS5 Wednesday')
    btn4 = types.KeyboardButton('CS5 Thursday')
    btn5 = types.KeyboardButton('CS5 Friday')
    btn_back = types.KeyboardButton('Back to Main Menu')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    markup.add(btn_back)

    bot.send_message(chat_id, "Choose an option for CS5:", reply_markup=markup)

def get_schedule_cs5(day):
    schedules = {
        "Monday": "9:30-10:50 Linear Algebra in 202 room\n"
                  "11:00-12:20 Calculus in 105 room\n"
                  "13:30-14:50 Discrete Math in 107 room",

        "Tuesday": "9:30-10:50 Discrete Math in 202 room\n"
                   "11:00-12:20 Calculus in 104 room\n"
                   "13:30-14:50 Statistics in 205 room",

        "Wednesday": "9:30-10:50 Physics in 101 room\n"
                     "11:00-12:20 Data Science in 310 room",

        "Thursday": "9:30-10:50 AI in 207 room\n"
                    "11:00-12:20 Computer Vision in 309 room",

        "Friday": "9:30-10:50 Ethics in Technology in 306 room\n1"
                  "1:00-12:20 Blockchain Fundamentals in 305 room"
    }
    return schedules.get(day, "No schedule available for this day.")
