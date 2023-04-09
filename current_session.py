import json
from datetime import date
import os
import sys

filename = 'current_session.json'
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    path = os.path.expanduser('~')
    filename= os.path.join(os.path.expanduser('~'), '.current_session.json')
else:
    print('running in a normal Python process')
print(filename)


try:
    data = open(filename)
except:
    data = None
print(data)
if data != None:
    print("data isn't none")
    session_data = json.load(data)
    data.close()

else:
    print("data is none")
    session_data = None



class SessionData():
    def __init__(self, *args):
        self.today = date.today()
        self.session_data = session_data if session_data else None

    def save_session(self, letters, time_elapsed, game_finished=False):
        session_letters = []
        for i in range(len(letters)):
            for j in range (len(letters[i])):
                this_letter = {"row":letters[i][j].row,
                        "col": letters[i][j].col,
                        "text": letters[i][j].text,
                        "static": letters[i][j].static}
                session_letters.append(this_letter)
        session_dict = {
            "seed": self.today.year*10000 + self.today.month * 100 + self.today.day,
            "letters": session_letters,
            "time_elapsed": time_elapsed,
            "game_finished": game_finished
        }
        print(session_dict)
        with open(filename, 'w') as outfile:
            json.dump(session_dict, outfile)


        
        
    