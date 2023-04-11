import pygame
import os
import sys
import json

symbol_font = pygame.font.SysFont(None, 36)

filename = 'word_list.json'
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
    print(os.listdir(sys._MEIPASS))
    filename= os.path.join(sys._MEIPASS, 'word_list.json')
else:
    print('running in a normal Python process')
data = open(filename)
dictionary = json.load(data)

class Word():
    def __init__(self, *args):
        self.letters = args[0]
        self.word_exists = False
        self.word_across = args[1]
        self.row = None if self.word_across == False else args[2]
        self.col = None if self.word_across == True else args[2]
        
    def check_word(self):
        word_found = False
        word_string = ""
        for letter in self.letters:
            if letter.text == None:
                self.word_exists = False
                break
            else:
                word_string = word_string + letter.text
        if len(word_string) == len(self.letters):
            try:
                word_found = True if dictionary[word_string.lower()] == 1 else False  
            except:
                word_found = False
        for letter in self.letters:
            if word_found == True:
                self.word_exists = True
                if self.word_across:
                    letter.in_word_across = True
                else:
                    letter.in_word_down = True
            else:
                self.word_exists = False
                if self.word_across:
                    letter.in_word_across = False
                else:
                    letter.in_word_down = False
        return word_found
    
    def render_check(self, screen, index):
        if self.word_exists == True:
            icon = pygame.image.load('green_check.png')
            
            x_val = 20 if self.word_across == True else index * 85 + 73
            y_val = index*85 + 115 if self.word_across == True else 60
            screen.blit(icon, (x_val, y_val))

        