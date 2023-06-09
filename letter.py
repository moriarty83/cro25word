import pygame

pygame.init()
font = pygame.font.SysFont(None, 56)
static_font = pygame.font.SysFont(None, 56)
static_font.underline = True
score_font = pygame.font.SysFont(None, 24)

palette_green = pygame.Color("#99c98f") 
palette_blue = pygame.Color("#8b98fc")
palette_cyan1 = pygame.Color("#2fa89e")
palette_cyan2 = pygame.Color("#5dc2b9")
palette_light_gray = pygame.Color("#fff1bd")
palette_dark_gray = pygame.Color("#3f3f3f")
palette_gold = pygame.Color("#e0b14a")
palette_purple = pygame.Color("#8460a3")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_values = {
    "E":1,
    "A":1,
    "S":1,
    "O":1,
    "T":1,

    "I": 2,
    "R": 2,
    "N": 2,
    "L": 2,
    "D": 2,

    "U": 3,
    "P": 3,
    "M": 3,
    "C": 3,
    "G": 3,

    "Y":4,
    "B":4,
    "H":4,
    "K":4,
    "W":4,

    "F": 5,
    "V": 5,
    "Z": 5,
    "X": 5,
    "Q": 5,
    "J": 5,
    }

class Letter():
    def __init__(self, *args):
        self.screen = args[0]
        self.row = args[1]
        self.col = args[2]
        self.static = False
        self.active_letter = False
        self.width = 80
        self.height = 80
        self.margin = 5
        self.x_offset =35
        self.y_offset = 75
        self.color = "white"
        self.text = None
        self.selected = False
        self.in_word_across = False
        self.in_word_down = False
        self.score = 0
        self.game_over = False
        
    def SelectLetter(self, select=True):
        self.selected = select
            

    def RenderLetter(self):
        self.color = palette_gold if self.static and self.in_word_down and self.in_word_across else palette_blue if self.static and self.in_word_across or self.static and self.in_word_down else palette_blue if self.in_word_across and self.in_word_down else palette_green if self.in_word_across or self.in_word_down else palette_light_gray if self.selected == True else "white"
        pygame.draw.rect(self.screen,
                             self.color,
                             [(self.margin + self.width) * self.col + self.margin+self.x_offset,
                              (self.margin + self.height) * self.row + self.margin + self.y_offset,
                              self.width,
                              self.height])
        if self.selected:
            if self.active_letter:
                pygame.draw.rect(self.screen,
                                palette_cyan1,
                                [(self.margin + self.width) * self.col + self.margin+self.x_offset,
                                (self.margin + self.height) * self.row + self.margin+self.y_offset,
                                self.width,
                                self.height], 4)
            else:
                pygame.draw.rect(self.screen,
                    palette_cyan2,
                    [(self.margin + self.width) * self.col + self.margin+self.x_offset,
                    (self.margin + self.height) * self.row + self.margin+self.y_offset,
                    self.width,
                    self.height], 1)

        if self.text:
            if self.static:
                text = static_font.render(self.text, True, "black")
                self.screen.blit(text, [(self.margin + self.width) * self.col + self.margin+self.x_offset+10,
                    (self.margin + self.height) * self.row + self.margin+self.y_offset+10,
                    self.width,
                    self.height])
            else: 
                newfont = font.underline
                text = font.render(self.text, True, "black")
                self.screen.blit(text, [(self.margin + self.width) * self.col + self.margin+self.x_offset+10,
                        (self.margin + self.height) * self.row + self.margin+self.y_offset+10,
                        self.width,
                        self.height])
            if self.game_over:
                score = score_font.render(f"{str(self.score)} pts", True, "black")
                self.screen.blit(score, [(self.margin + self.width) * self.col + self.margin+self.x_offset+5,
                    (self.margin + self.height) * self.row + self.margin+self.y_offset+62,
                    self.width,
                    self.height])

            
    def ScoreLetter(self):
        self.game_over = True
        score = 0
        if self.in_word_across == False and self.in_word_down == False:
            return score
        if self.text == None:
            return score
        if self.in_word_across:
            score += 5
            if self.static:
                score += 5
        if self.in_word_down:
            score += 5
            if self.static:
                score += 5
        try:
            score += letter_values[self.text.upper()]
        except:
            score += 0
        self.score = score
        return score
          
# Letter scores inpsired by 
# CROSSWORD PUZZLE LETTER FREQUENCIES
# By JOHN D. IDTCHCOCK
# Laramie, Wyoming






