#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import telebot
from Frontend import Bot_inline_btns
############static variables#####################
TG_api = '6473206457:AAGDDCArrBFIXTdFT1rGJqPVR1CjXqhugeM'
admins = [818895144, 1897256227]
#################################################

bot = telebot.TeleBot(TG_api)


@bot.message_handler(commands=['start', 'admins'])
def start(message):
    buttons = Bot_inline_btns()
    command = message.text.replace('/', '')
    if command == 'start':
        bot.send_message(message.chat.id, 'Hello! Choose language!', reply_markup=buttons.start_btns())




bot.polling(none_stop=True)