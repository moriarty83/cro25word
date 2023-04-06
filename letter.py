import pygame

pygame.init()
font = pygame.font.SysFont(None, 56)


class Letter():
    def __init__(self, *args):
        self.screen = args[0]
        self.row = args[1]
        self.col = args[2]
        self.active_letter = False
        self.width = 80
        self.height = 80
        self.margin = 5
        self.color = "white"
        self.text = None
        self.selected = False
        self.in_word_across = False
        self.in_word_down = False

        
        
    def SelectLetter(self, select=True):
        self.selected = select
            

    def RenderLetter(self):
        self.color = "blue" if self.in_word_across and self.in_word_down else "green" if self.in_word_across or self.in_word_down else "white"
        pygame.draw.rect(self.screen,
                             self.color,
                             [(self.margin + self.width) * self.col + self.margin,
                              (self.margin + self.height) * self.row + self.margin,
                              self.width,
                              self.height])
        if self.selected:
            if self.active_letter:
                pygame.draw.rect(self.screen,
                                "purple",
                                [(self.margin + self.width) * self.col + self.margin,
                                (self.margin + self.height) * self.row + self.margin,
                                self.width,
                                self.height], 2)
            else:
                pygame.draw.rect(self.screen,
                    "cyan",
                    [(self.margin + self.width) * self.col + self.margin,
                    (self.margin + self.height) * self.row + self.margin,
                    self.width,
                    self.height], 2)

        if self.text:
            text = font.render(self.text, True, "black")
            self.screen.blit(text, [(self.margin + self.width) * self.col + self.margin,
                    (self.margin + self.height) * self.row + self.margin,
                    self.width,
                    self.height])

            

