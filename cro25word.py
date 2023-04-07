import pygame
import random
import datetime
from pygame.locals import *
from letter import *
from word import *
from key_input import *

# Seed number
current_date = datetime.date.today()

seed = current_date.year*10000 + current_date.month * 100 + current_date.day
random.seed(seed)
# 
select_across = True

selected_row = 0
selected_col = 0
 
# Width and Height of Letter Boxes
cell_width = 80
cell_height = 80

# Screen dimensions
screen_width = 500
screen_height = 550
 
# This sets the margin between each letter.
MARGIN = 5
 
# Create 2 dimensional array of letters.
letters = []

# Create array of words
words_across = []
words_down = []
words_in_use = []

# Session Data
font = pygame.font.SysFont(None, 24)
btn_font = pygame.font.SysFont(None, 36)

time_elapsed = 0
total_score = 0

finish_clicked = False
finish_confirmed = False

game_finished = False

 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [500, 550]
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

# Advance cursor on entry or tab.
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

# Populate word class instances with their appropriate letters.
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

# Randomly generate the static starting letters.
def get_start_letters():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    start_letters = []
    start_locations = []
    for i in range(3):
        start_letters.append(alphabet[random.randint(0,25)])
    while len(start_locations) < 3:
        random_1 = random.randint(0,4)
        random_2 = random.randint(0,4)
        location = str(random_1) + "," + str(random_2)
        if location not in start_locations:
            start_locations.append(location)
    for i in range(len(start_locations)):
        loc = start_locations[i].split(',')
        letter = letters[int(loc[0])][int(loc[1])]
        letter.text = start_letters[i]
        letter.static = True

# Update the game clock.
def update_clock():
    time_elapsed = pygame.time.get_ticks()//1000
    game_clock = str(0) + ":" + str(time_elapsed%60) if time_elapsed%60 > 9 else f"0:0{time_elapsed%60}"
    clock_text = font.render(game_clock, True, "white")
    clock_rect = clock_text.get_rect(center=(screen.get_width()/2, 10))
    screen.blit(clock_text, clock_rect)

def tally_score():
    global total_score
    for i in range(5):
        for j in range(5):
            total_score += letters[i][j].ScoreLetter()

populate_words()
get_start_letters()
update_selected()

finished_text = btn_font.render("Finish", True, "black")
     
    # superimposing the text onto our button

 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if finish_clicked == True:
            if event.type == pygame.MOUSEBUTTONUP:
                if confirm_btn_rect.collidepoint(pygame.mouse.get_pos()):
                    finish_confirmed = True
                if cancel_btn_rect.collidepoint(pygame.mouse.get_pos()):
                    finish_clicked = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] >= 35 and pos[0] <= 465 and pos[0] >= 35 and pos[1] <= 465:
                # Change the x/y screen coordinates to letters coordinates
                new_col = (pos[0]-35) // (cell_width + MARGIN)
                new_row = (pos[1]-35) // (cell_height + MARGIN)
                if new_row == selected_row and new_col == selected_col:
                    select_across = not select_across
                else:
                    selected_row = new_row
                    selected_col = new_col
                update_selected()
            # Set that location to one
        elif event.type == pygame.MOUSEBUTTONUP:
            if finished_rect.collidepoint(pygame.mouse.get_pos()):
                finish_clicked = True
        elif event.type == pygame.KEYDOWN:
            
            key = get_key_pressed(event)
            if key == "tab":
                advance_cursor(True)
            elif letters[selected_row][selected_col].static != True:
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

    if game_finished == False:
        update_clock()

    # Render finished btn
    if finish_clicked == False:
        finished_rect = pygame.draw.rect(screen, "gold", [screen_width/2-70,screen_height-65,140,40], border_radius=3)
        pygame.draw.rect(screen, "gray", [screen_width/2-70,screen_height-65,140,40], 2, 3)
        finish_text_rect = finished_text.get_rect(center=(screen.get_width()/2, screen_height-45))
        screen.blit(finished_text , finish_text_rect)

    # Confirm Finish rect
    if finish_clicked:
        #Parent rect
        if game_finished == False:
            confirm_rect = pygame.draw.rect(screen, "gray", [40,40,420,420], border_radius=3)
            pygame.draw.rect(screen, "white", [40,40,420,420], 2, 3)
            if finish_confirmed == False:
                #Confirm Text
                info_text = btn_font.render("Are you sure you're finished?", True, "black")
                info_text_rect = info_text.get_rect(center=(screen_width/2,screen_height/2-100))
                screen.blit(info_text, info_text_rect)

                #Confirm Btn
                confirm_text = btn_font.render("Yes", True, "black")
                confirm_btn_rect = pygame.draw.rect(screen, "gold", [screen_width/2-70-100,screen_height/2,140,40], border_radius=3)
                pygame.draw.rect(screen, "black", [screen_width/2-70-100,screen_height/2,140,40], 2, border_radius=3)
                confirm_text_rect = confirm_text.get_rect(center=(screen_width/2-70-30,screen_height/2+20))
                screen.blit(confirm_text, confirm_text_rect)

                #Cancel Btn
                cancel_text = btn_font.render("Cancel", True, "black")
                cancel_btn_rect = pygame.draw.rect(screen, "white", [screen_width/2-70+100,screen_height/2,140,40], border_radius=3)
                pygame.draw.rect(screen, "black", [screen_width/2-70+100,screen_height/2,140,40], 2, border_radius=3)
                
                cancel_text_rect = cancel_text.get_rect(center=(screen_width/2-70+170,screen_height/2+20))
                screen.blit(cancel_text, cancel_text_rect)
            else:
                if game_finished == False:
                    tally_score()
                    game_finished = True
        if game_finished == True:
            final_score_text = btn_font.render(str(total_score), True, "white")
            final_score_rect = pygame.draw.rect(screen, "black", [screen_width/2-70,screen_height-65,140,40])
            final_score_text_rect = final_score_text.get_rect(center=(screen.get_width()/2, screen_height-45))
            screen.blit(final_score_text, final_score_text_rect)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()