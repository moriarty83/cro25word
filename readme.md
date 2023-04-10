## Installation
1. Clone this repo.
2. Navigate to the repo folder in your terminal.
3. Run 'pip -r requirements.txt'
4. Run 'python cro25word.py'

## Inspiration
Cro25word (pronounced ‘crossword’) is a puzzle game inspired by the competitive and communal aspects of Wordle, the logic challenge of Sudoku and a classic crossword puzzle. The result is a daily puzzle for players to challenge their brain and vocabulary and showcase their wit and verbal creativity.

## What it does
Cro25word is a reverse crossword game. Players are presented with a 5x5 crossword grid with 3 letters randomly selected and placed on the board. These 'Fixed' letters cannot be moved or changed. players have the day to fill in as much of the puzzle with English words as possible. 

What's with the name? Because Cro25word is built on a 5 x 5 grid, it seemed appropriate to substitute the 'ss' in 'Crossword' with '25' to represent the number of letters on the board.

##### Scoring:
All letters are worth 5 points for each word they appear in, i.e., 5 points when used in an across word and/or 5 points when used in a down word.
    
Fixed letters are worth an additional 5 points per word they are in, so 10 points when used in one word and 20 points when used in both an across and down word together.

Additional points are awarded for specific letters. Point values are inspired by the paper "Crossword Puzzle Letter Frequencies" by John. D. Hitchcock, Laramie, WI, and are as follows:

###### 1 Point
E, A, S, O, T

###### 2 Points
I, R, N, L, D

###### 3 Points
U, P, M, C, G

###### 4 Points
B, H, K, W, Y

###### 5 Points
F, V, Z, X, Q, J


## How we built it
Cro25word was built over ten major stages using PyGame and no other major libraries or modules. Standard python modules used include Math, Random, JSON, Sys, OS & DateTime

##### Stage 1: Set up PyGame:
The first stage was building the basic PyGame framework with screen surface, while loop and quit logic.

##### Stage 2: Build the Board.
This stage consisted of generating a 5 x 5 gird of Rects and doing some simple math in PyGame to determine which Rect should be selected when the user clicks.

##### Stage 3: Developing the 'Letter' class. 
The custom class Letter is the workhorse of the game. It holds the actual pygame.Rect that is rendered on the screen as well as the actual letter being used for that place on the board. The Letter class identifies if a letter is being used in an across word and/or a down word, how many points it is worth, and if it is a 'Fixed' letter.

Additionally, refactoring the 'get_key_pressed' method happened in Stage 3 to keep the main file or letter class from becoming cluttered with a long cumbersome function.

##### Stage 4: Developing the 'Word' class. 
The Word Class holds a list of words. In each game there are 25 Words. The class identifies them as Across or Down and holds the functionality for matching its letters to the game's 'Dictionary' to see if it is indeed a valid English word. The Dictionary is a subset of words_dictionary.json available at https://github.com/dwyl/english-words. 

##### Stage 5: Build functionality for 'Fixed' letters.
It was important to ensure that everybody playing Cro25word on any given day got the same board. In addition to adding a 'static' attribute to the Letter class to prevent this letter from being changed by the player, a date-specific method of seeding the random number generator used to generate the Fixed letters had to be created.

##### Stage 6: UI Enhancements.
It became apparent early on that the UI needed simple enhancements to make navigating the board easier. In this stage quality of life functionality was added including advancing the selected letter to the next available after a letter is entered, pressing 'Tab' to advance the selected letter and 'Delete' or 'Backspace' to move to the previous letter. 

Selecting a color palette and adding methodology to color code letters to show their overall point value during gameplay was also necessary.

##### Stage 6: End of Game & Scoring
With the board now being populated with Fixed letters and the UI functioning well, a scoring regime needed to be implemented and functionality for a player to declare the game finished.

##### Stage 8: Implementing persistent data.
This stage added persistent data to the game which stored a player's session for the day. This ensured that if a player quit the program before they finished the game, upon opening the program again later that day, they would pick up where they left off.

##### Stage 9: Adding how-to-play and scoring info and quit button.
A simple window that let players see a quick description of how to play and how scoring works was added, accessible through a simple 'i' icon in the lower right of the window.

For deployment on Trinket, a ‘x’ button to quit the game was added to ensure the quit and save functions ran correctly when stopping play.

## Challenges we ran into
With experience using Unity but not PyGame, it was a challenge to work with a game engine/library that had no inherent physics or developer UI. The first draft project relied heavily on collisions, rotation, and vectors. After running into several performance and other issues developing physics and complex collision detection, Cro25word came out of a new brainstorming session for a game that was more suited to PyGame's strengths.

## Accomplishments that we're proud of
##### Random seed functionality and single-day play. 
In order to achieve a level of community and competitive spirit, it was necessary to make sure players were playing the same game, i.e., the same starting letters and locations, on any given day. This is done by using a simple datetime.today() function and then building that into a single number. This number is used as the seed value for all random operations in the game. Thus, allowing players across the globe to be playing with the same board from day to day.

## What we learned
First and foremost, I learned PyGame. Having never used this library before, I learned its strengths and weaknesses. The biggest strength I found is simply the ability to use Python, it's clean style and syntax, to develop game ideas. I found what PyGame is and isn't well suited for and my experience reinforced the importance of writing clean, well-factored code.

## What's next for Cro25word

##### Mobile
Cro25word is a perfect game for mobile devices. Developing a version for both Android and iOS is very high on the next-steps list. It may be necessary to move to a different platform like Unity or React Native to accomplish this.

##### Sharing
Along with Mobile development, adding functionality for players to share their accomplishments with the puzzle of the day is a high priority.

##### Code Optimization
The 'get_key_pressed' method will be updated to use a regular expression instead of the current long string of if/elif statements.

##### Cheating/Hacking Safeguards
Steps will be taken to prevent hacking future dates’ Fixed letters. This will probably be best accomplished by generating Fixed letters remotely instead of on a player’s device locally and using additional hashing to keep the process secure.


