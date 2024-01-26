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


class Bot_text:
    def __init__(self):
        super(Bot_text, self).__init__()
        self.__rus = {'info': ['негор']}
        self.__eng = {'info': ['BBC']}

    def get_rus(self, type_):
        return self.__rus[type_]

    def get_eng(self, type_):
        return self.__eng[type_]
