#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import sqlite3
import os
import json


class User_data:
    def __init__(self):
        super(User_data, self).__init__()
        self.__user_data = {}


    def init(self, user_id):
        self.__user_data.update({user_id: []})

class Data_base:
    def __init__(self, path):
        super(Data_base, self).__init__()
        self.__db_path = path
        self.cursor = None
        self.db = None
        self.init()
    def init(self):
        if not os.path.exists(self.__db_path):
            self.db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.cursor = self.db.cursor()
            self.cursor.execute('''CREATE TABLE users(
            id int,
            lang text
            )
            ''')
            self.db.commit()
        else:
            self.db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.cursor = self.db.cursor()