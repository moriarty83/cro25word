## Inspiration
Five x 5 (pronouced 'five by five') is puzzle game inspired by the comptetive and communal aspects of Wordle, the logic challenge of Sudoko and a classic crossword puzzle. The result is a daily puzzle for players challenge their brain and vocabulary and showcase their wit and verbal creativity.

## What it does
Five x 5  is a reverse crossword game. Players are presented with a 5x5 crossword grid with 3 letters randomly selected and placed on the board. These 'Fixed' letters cannot be moved or changed. players have the day to fill in as much of the puzzle with English words as possible. 

##### Scoring:
All letters are worth 5 points for each word they appear in, i.e. 5 points when used in an across word and/or 5 points when used in a down word.
    
Fixed letters are worth an additional 5 points per word they are used in for 10 and 20 points instead of 5 and 10.


Additional points are awarded for specific letters, point values are inspired by the paper "Crossword Puzzle Letter Frequencies" by  John. D. Hitchcock, Laramie and are as follows:
|Letter |Points |       |Letter |Points |       |Letter |Points |
|-------|-------|-------|-------|-------|-------|-------|-------|
|E      |1      |       |U      |3      |       |F      |5      |
|A      |1      |       |P      |3      |       |V      |5      |
|S      |1      |       |M      |3      |       |Z      |5      |
|O      |1      |       |C      |3      |       |X      |5      |
|T      |1      |       |G      |3      |       |Q      |5      |
|I      |2      |       |Y      |4      |       |J      |5      |
|R      |2      |       |B      |4      |
|N      |2      |       |H      |4      |
|L      |2      |       |K      |4      |
|D      |2      |       |W      |4      |


## How we built it
Five x 5 was built over ten majro stages using PyGame and no other major libraries with the exception of PyInstaller which is was to generate a single executable for Mac users. Other standard python modules used include: Math, Random, JSON, Sys, OS & DateTime

##### Stage 1: Set up PyGame:
The first stage was buildin the basic PyGame framework with screen surface, while look and quit logic.

##### Stage 2: Build the Board.
This stage consisted of generating a 5 x 5 gird of Rects and doing some simple math in pygam to determine which Rect should be selected when the user clicks.

##### Stage 3: Developing the 'Letter' class. 
The custom class Letter is the workhorse of the game. It holds the actual pygame.Rect that is rendered on the screen as well as the actual letter being used in for that place onthe board. Additionally, the Letter class idenifies if a letter is being used in an across word and/or a down word, how many points it is worth, and if it is a 'Fixed' letter.

Additionally, refactoring the 'get_key_pressed' method happened in Stage 3 to keep the main file or letter class from becoming cluttered with a long cumbersome function.

##### Stage 4: Developing the 'Word' class. 
Just like in real life, a Word consists of a list of Letters. In each game there is a list of 25 Words which identify themselves as Across or Down and the Word class holds the important functionality for matching its list of letters to the game's 'Dictionary' to see if it is indeed a valid English word. The Dictionary is is a subset of words_dictionary.json available at https://github.com/dwyl/english-words. 

##### Stage 5: Build functionality for 'Fixed' letters.
It was important to ensure that everybody playing Five x 5 on any given day got the same board. In addition to adding a 'static' attribute to the Letter class to prevent this letter from being changed by the player, a date-specific method of seeding the random number generator used to generate the Fixed letters had to be created.

##### Stage 6: UI Enhancements.
It became apparent early on that the UI needed simple enhancements to make navigating the board easier. In this stage quality of life functionality was added including advancing the selected letter to the next available after a letter is entered, pressing 'Tab' to advance the selected letter and 'Delete' or 'Backspace' move to the previous letter. 

Selecting a color palette and additing methodology to color code letters to show thier overall 'value' during gameplay was also necessary.

##### Stage 6: End of Game & Scoring
With the board now being populated with Fixed letters and the UI functioning well, a scoring regime needed to be implemented and functionaltiy for a player to declare the game finished.

##### Stage 8: Implementing persistant data.
This stage added persisent data to the game which stored a player's session for the day. This ensured that if a player quit the program before they finished the game, upon opening the program again later that day, they would pick up where the left off.

##### Stage 9: Adding how-to-play and scoring info.
A simple window that let players see a quick description of how to play and how scoring works was added, accessible through a simple 'i' icon in the lower right of the window.

##### Stage 10: Generating Mac executable.
Using PyInstaller, a standalone executable for mac was created.


## Challenges we ran into

## Accomplishments that we're proud of
Random seed functionality and single-day play. In order to achieve a level of community and competitive spirit, it was necessary to make sure players were playing the same game, e.g. the same starting letters and locations, on any given day. This is done by using a simple datetime.today() function and then building that into a single number. This number is seed value for all random operations in the game. Thus allowing players across the globe to be playing with the same board from day to day.

## What we learned

## What's next for Five x Five

##### Mobile
Five x 5 is a perfect game for mobile devices. Developing a version for both Android and iOS is very high on the next-steps list. It may be necessary to move to a differnet platform like Unity or React Native to accomplish this.

##### Sharing
Along with Mobile development, adding functionality for players to share their accomplishments with the puzzle of the day is a high priority.

##### Code Optimization
The 'get_key_pressed' method will be updated to use a regular expression instead of the current long string of if/elif statements.

##### Cheating/Hacking Safeguards
Steps will be toaken to prevent hacking future dates Fixed letters. This will probably be best accomplisehed by generating Fixed letters remotely instead of on a players device locally and using additional hashing to keep the process secure.
