import json

from datetime import date


data = open('word_list.json')
session_data = json.load(data)

class SessionData():
    def __init__(self, *args):
        self.today = date.today()
        self.session_data = session_data