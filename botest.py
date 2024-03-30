import telebot
from portal import main
from format_res import *


API_TOKEN = "7125049821:AAFsDn1W5LgeAn1hmSreM_HDLvbI9d3SWNs"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start_msg(message):
    first_name = message.from_user.first_name
    wellcome_msg = f"👋 {first_name}, Welcome to the Addis Ababa University Portal Bot.\n Curruntly avaliable commands\n /register"
    bot.send_message(message.chat.id, wellcome_msg)

@bot.message_handler(commands=["register"])
def register(message):
    ask_id_msg = "Please Send Me Your ID Number"
    bot.send_message(message.chat.id, ask_id_msg)
    bot.register_next_step_handler(message, check_id)

def check_id(message):
    ID = (message.text).split("/")
    if len(ID) == 3 and str(ID[0]).isalpha() and str(ID[1]).isnumeric() and str(ID[2]).isnumeric() and len(ID[0]) == 3 and len(ID[1]) == 4 and len(ID[2]) == 2:
        ask_id_password = "Please Send Me Your Password"
        bot.send_message(message.chat.id, ask_id_password)
        bot.register_next_step_handler(message, check_password, ID)
    else:
        bot.send_message(message.chat.id, "Invalid ID Number")
        ask_id_msg = "Please send me your ID number as it on your ID CARD"
        bot.send_message(message.chat.id, ask_id_msg)
        bot.register_next_step_handler(message, check_id)

def check_password(message, ID):
    PASSWORD = message.text
    if PASSWORD:
        get_grades(ID, PASSWORD, message)
    else:
        bot.send_message(message.chat.id, "Invalid Password")
        bot.register_next_step_handler(message, check_password, ID)
        #TODO: what will happen if it is invalid?

def get_grades(ID, PASSWORD, message):
    tables = main(ID, PASSWORD)
    ava_semesters = find_semisters(tables)
    
    bot.send_message(message.chat.id, "Which semester do you want?")
    bot.register_next_step_handler(message, choose_semester, ava_semesters, tables)

def choose_semester(message, ava_semesters, tables):
    semester = message.text
    if semester in ava_semesters:
        formater(tables)
        bot.send_message(message.chat.id, create_table(semester), parse_mode="Markdown")

    else:
        bot.send_message(message.chat.id, "Unavaliable semester")
        bot.send_message(message.chat.id, f"please choose from \n{ava_semesters}")
        bot.register_next_step_handler(message, choose_semester, ava_semesters, tables)

bot.polling()


