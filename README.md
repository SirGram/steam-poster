# game_grid_generator
Creates a random grid of game banners.
![alt text](https://raw.githubusercontent.com/SirGram/game_grid_generator/main/example.png)

----------------------------------------------------------------

Include games you wish to search for inside __list_of_games.txt__

----------------------------------------------------------------

pip install python-steamgriddb
| :---:   | 

api_key
| :---:   | 

https://www.steamgriddb.com/profile/preferences/api

Execute __steam.py__ for searching images in STEAMGRIDDB

Images are saved within ./STEAMIMAGES

----------------------------------------------------------------

Execute __main.py__ for making a grid window using ./STEAMIMAGES
Screenshot of grid saved in ./COLLAGE



Parameter		    						 |  Default Value | Action
| :---:   | :---: | :---: |
RESIZE 	|		      							True		|						Downloaded images to be resized from orignial width and height.
DELETE_IMAGES |									True	|							Delete images from 3 root folders after making grid.
GENERATE_LABEL | 								False	|							Creates label on top of IMAGE canvas to indicate coordinate.
FULLSCREEN_WINDOW  		|					False	|							Makes tkinter root Fullscreen.
CLOSE_WINDOW_AFTER_SEARCH	|			False	|							Quits window after 2s of showing the grid.
ROW_SIZE				|								5			|							Indicates row length.
COLUMN_SIZE 			|							5			|							Indicates column length.
GRID_SIZE_IN_PIXELS 	|					100			|						Indicates width and height of image canvas resizing in pixels.
PADDING								|					2			|							Indicates window padding in pixels.
PADDING_BETWEEN_CELLS 	|				2			|							Indicates cell padding in pixels.
BACKGROUND_COLOR 					|	 	 "white"	|						Indicates window background color.

----------------------------------------------------------------
