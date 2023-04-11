import pygame

pygame.init()

headline_font = pygame.font.SysFont(None, 48)
headline2_font = pygame.font.SysFont(None, 36)

headline_font.underline = True
how_to_font = pygame.font.SysFont(None, 24)
letter_header_font = pygame.font.SysFont(None, 24)
letter_header_font.underline = True

how_tos = ["Fill the board with as many 5-letter English words", "as possible before the end of the day.", "The underlined letters cannot be changed.", "Click the 'Finish' button when you're done."]

color_scores = [
    {"color": pygame.Color("#99c98f"), "points": "5 pts"},
    {"color": pygame.Color("#8b98fc"), "points": "10 pts"},
    {"color": pygame.Color("#e0b14a"), "points": "20 pts"},
]
one_point_letters = ["A", "E", "O", "S", "T"]
two_point_letters = ["D", "I", "L", "N", "R"]
three_point_letters = ["C", "G", "M", "P", "U"]
four_point_letters = ["B", "H", "K", "W", "Y"]
five_point_letters = ["F", "J", "Q", "V", "X", "Z"]



class GameInfo():
    def __init__(self, *args):
        self.screen = args[0]
        self.display = False
        self.headline = "How to Play"

        
    def RenderInfo(self):
        
        info_rect = pygame.draw.rect(self.screen, "black", [40,40,500,550])
        headline_text = headline_font.render(self.headline, True, "white")
        headline_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2,50,100,30], border_radius=3)
        headline_rect = headline_text.get_rect(center=(self.screen.get_width()/2 , 50))
        self.screen.blit(headline_text , headline_rect)

        for i in range(len(how_tos)):
            how_to_text = how_to_font.render(how_tos[i], True, "white")
            how_to_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2,100+(i*20),100,30], border_radius=3)
            how_to_rect = how_to_text.get_rect(center=(self.screen.get_width()/2 , 100+(i*20)))
            self.screen.blit(how_to_text , how_to_rect)

        scoring_text = headline2_font.render("Scoring", True, "white")
        scoring_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2,200,100,30], border_radius=3)
        scoring_text_rect = scoring_text.get_rect(center=(self.screen.get_width()/2 , 200))
        self.screen.blit(scoring_text, scoring_text_rect)

        for i in range(len(color_scores)):
            offset = -150 if i == 0 else 0 if i == 1 else 150
            color_rect = pygame.draw.rect(self.screen, color_scores[i]["color"], [self.screen.get_width()/2 + offset - 30,220,60,60], border_radius=3)
            score_text = how_to_font.render(color_scores[i]["points"], True, "white")
            score_text_rect = scoring_text.get_rect(center=(self.screen.get_width()/2 + offset + 23, 250))
            self.screen.blit(score_text, score_text_rect)
    

        letter_header_1 = letter_header_font.render("1 Pt ", True, "white")
        letter_header1_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2-210,300,50,30])
        self.screen.blit(letter_header_1, letter_header1_rect)
        for i in range (len(one_point_letters)):
            letter_text = how_to_font.render(one_point_letters[i], True, "white")
            letter_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2-210,320+(i*20),50,30])
            self.screen.blit(letter_text, letter_text_rect)

        letter_header_2 = letter_header_font.render("2 Pts", True, "white")
        letter_header2_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2-110,300,50,30])
        self.screen.blit(letter_header_2, letter_header2_rect)
        for i in range (len(two_point_letters)):
            letter_text = how_to_font.render(two_point_letters[i], True, "white")
            letter_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2-110,320+(i*20),50,30])
            self.screen.blit(letter_text, letter_text_rect)
        
        letter_header_3 = letter_header_font.render("3 Pts", True, "white")
        letter_header3_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2-10,300,50,30])
        self.screen.blit(letter_header_3, letter_header3_rect)
        for i in range (len(three_point_letters)):
            letter_text = how_to_font.render(three_point_letters[i], True, "white")
            letter_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2-10,320+(i*20),50,30])
            self.screen.blit(letter_text, letter_text_rect)

        letter_header_4 = letter_header_font.render("4 Pts", True, "white")
        letter_header4_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2+90,300,50,30])
        self.screen.blit(letter_header_4, letter_header4_rect)
        for i in range (len(four_point_letters)):
            letter_text = how_to_font.render(four_point_letters[i], True, "white")
            letter_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2+90,320+(i*20),50,30])
            self.screen.blit(letter_text, letter_text_rect)

        letter_header_5 = letter_header_font.render("5 Pts", True, "white")
        letter_header5_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2+190,300,50,30])
        self.screen.blit(letter_header_5, letter_header5_rect)
        for i in range (len(five_point_letters)):
            letter_text = how_to_font.render(five_point_letters[i], True, "white")
            letter_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2+190,320+(i*20),50,30])
            self.screen.blit(letter_text, letter_text_rect)

        bonus_text = how_to_font.render("Completion Bonus: 100 Pts", True, "white")
        bonus_text_rect = pygame.draw.rect(self.screen, "black", [self.screen.get_width()/2,450,100,30], border_radius=3)
        bonus_text_rect = bonus_text.get_rect(center=(self.screen.get_width()/2 , 450))
        self.screen.blit(bonus_text, bonus_text_rect)