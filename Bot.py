#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import telebot
from Frontend import Bot_inline_btns, Bot_text
from Backend import User_data
############static variables#####################
TG_api = '6473206457:AAGDDCArrBFIXTdFT1rGJqPVR1CjXqhugeM'
admins = [818895144, 1897256227]
#zzsxd - 1897256227
#sbr - 818895144
#################################################

bot = telebot.TeleBot(TG_api)


@bot.message_handler(commands=['start', 'admins'])
def start(message):
    buttons = Bot_inline_btns()
    command = message.text.replace('/', '')
    if command == 'start':
        user_data.init(message.chat.id)
        bot.send_message(message.chat.id, 'Hello! Choose language!\nПривет! Выберите язык!', reply_markup=buttons.start_btns())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    buttons = Bot_inline_btns()
    if call.data == 'rus':
        pass
    elif call.data == 'eng':
        pass





phrase = Bot_text()
user_data = User_data()

bot.polling(none_stop=True)