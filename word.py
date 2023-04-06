import pygame

import json

data = open('word_list.json')
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
            print(word_string)
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