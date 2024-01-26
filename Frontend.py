#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from telebot import types

class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=2)
    def start_btns(self):
        rusbtn = types.InlineKeyboardButton('🇷🇺', callback_data='rus')
        engbtn = types.InlineKeyboardButton('🇺🇸', callback_data='eng')
        self.__markup.add(rusbtn, engbtn)
        return self.__markup