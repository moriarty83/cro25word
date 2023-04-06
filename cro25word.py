import pygame
import numpy
from pygame.locals import *
from letter import *
from word import *
from key_input import *

# 
select_across = True

selected_row = 0
selected_col = 0
 
# Width and Height of Letter Boxes
WIDTH = 80
HEIGHT = 80
 
# This sets the margin between each letter.
MARGIN = 5
 
# Create 2 dimensional array of letters.
letters = []

# Create array of words
words_across = []
words_down = []
words_in_use = []

 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [600, 900]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Cro25Word")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    letters.append([])
    for column in range(5):
        letters[row].append(Letter(screen, row, column))  # Append a cell

# METHODS
def update_selected():
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            letters[i][j].active_letter = False
            if i == selected_row and j == selected_col:
                letters[i][j].active_letter = True
                letters[i][j].SelectLetter()
            elif select_across and i == selected_row:

                letters[i][j].SelectLetter()
            elif select_across == False and j == selected_col:
                letters[i][j].SelectLetter()
            else:
                letters[i][j].SelectLetter(False)

def advance_cursor(next_letter = False):
    global selected_row
    global selected_col
    global select_across
    if next_letter == True:
        if select_across:
            selected_col = (selected_col + 1) % len(letters[selected_row])
        else:
            length = 0
            for i in range(len(letters)):
                if letters[i][selected_col]:
                    length += 1
            selected_row = (selected_row + 1) % length
    else:
        if select_across:
            length = len(letters[selected_row])
            for i in range(selected_col, selected_col + length):

                new_col = (i+1)%length

                if letters[selected_row][new_col].text == None:
                    selected_col = new_col
                    break
        else:
            length = 0
            for i in range(len(letters)):
                if letters[i][selected_col]:
                    length += 1
            for i in range(selected_row, length):
                if letters[i % length][selected_col].text == None:
                    selected_row = i % length
                    break
    update_selected()

def populate_words():
    global letters

    for i in range(5):
        row_letters = []
        col_letters = []
        for j in range(5):
            
            row_letters.append(letters[i][j])
            col_letters.append(letters[j][i])

        words_across.append(Word(row_letters, True, i))
        words_down.append(Word(col_letters, False, j))        

populate_words()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to letters coordinates
            new_col = pos[0] // (WIDTH + MARGIN)
            new_row = pos[1] // (HEIGHT + MARGIN)
            if new_row == selected_row and new_col == selected_col:
                select_across = not select_across
            else:
                selected_row = new_row
                selected_col = new_col
            update_selected()
            # Set that location to one
        elif event.type == pygame.KEYDOWN:
            key = get_key_pressed(event)
            if key == "tab":
                advance_cursor(True)
            else:

                letters[selected_row][selected_col].text = key
                words_across[selected_row].check_word()
                words_down[selected_col].check_word()
                if key != None:
                    advance_cursor()
                

 
    # Set the screen background
    screen.fill("black")
 
    # Draw the letters
    for row in range(5):
        for column in range(5):
            color = "white"
            letters[row][column].RenderLetter()
            

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()