import json

from datetime import date
import json


data = open('current_session.json')
try:
    session_data = json.load(data)
except:
    session_data = None
data.close()

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
        with open('current_session.json', 'w') as outfile:
            json.dump(session_dict, outfile)


        
        
    