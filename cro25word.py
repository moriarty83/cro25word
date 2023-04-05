import pygame
from pygame.locals import *
from letter import *
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
grid = []

 
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
    grid.append([])
    for column in range(5):
        grid[row].append(Letter(screen, row, column))  # Append a cell

# METHODS
def update_selected():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].active_letter = False
            if i == selected_row and j == selected_col:
                grid[i][j].active_letter = True
                grid[i][j].SelectLetter()
            elif select_across and i == selected_row:

                grid[i][j].SelectLetter()
            elif select_across == False and j == selected_col:
                grid[i][j].SelectLetter()
            else:
                grid[i][j].SelectLetter(False)

def advance_cursor(next_letter = False):
    global selected_row
    global selected_col
    global select_across
    if next_letter == True:
        if select_across:
            selected_col = (selected_col + 1) % len(grid[selected_row])
        else:
            length = 0
            for i in range(len(grid)):
                if grid[i][selected_col]:
                    length += 1
            selected_row = (selected_row + 1) % length
    else:
        if select_across:
            length = len(grid[selected_row])
            print(selected_col)
            for i in range(selected_col, selected_col + length):

                new_col = (i+1)%length

                if grid[selected_row][new_col].text == None:
                    selected_col = new_col
                    print(selected_col)
                    break
        else:
            length = 0
            for i in range(len(grid)):
                if grid[i][selected_col]:
                    length += 1
            for i in range(selected_row, length):
                if grid[i % length][selected_col].text == None:
                    selected_row = i % length
                    break
    update_selected()

def populate_words():


 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            new_col = pos[0] // (WIDTH + MARGIN)
            new_row = pos[1] // (HEIGHT + MARGIN)
            if new_row == selected_row and new_col == selected_col:
                select_across = not select_across
            else:
                selected_row = new_row
                selected_col = new_col
            update_selected()
            # Set that location to one
            print("Click ", pos, "Grid coordinates: ", selected_row, selected_col)
        elif event.type == pygame.KEYDOWN:
            if get_key_pressed(event) == "tab":
                advance_cursor(True)
            else:
                key = get_key_pressed(event)
                grid[selected_row][selected_col].text = get_key_pressed(event)
                if key != None:
                    advance_cursor()
                

 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(5):
        for column in range(5):
            color = WHITE
            grid[row][column].RenderLetter()
            

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()