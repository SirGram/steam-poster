# game_grid_generator
Creates a random grid of game banners

----------------------------------------------------------------

Include games you wish to search for inside list_of_games.txt

----------------------------------------------------------------

Execute steam.py for searching images in STEAMGRIDDB
Images are saved within ./STEAMIMAGES

----------------------------------------------------------------

Execute main.py for making a grid window using ./STEAMIMAGES
Screenshot of grid saved in ./COLLAGE

Parameter		     |  Default Value  | Action					

RESIZE 			      	True		Downloaded images to be resized from orignial width and height.
DELETE_IMAGES 			True		Delete images from 3 root folders after making grid.
GENERATE_LABEL  		False		Creates label on top of IMAGE canvas to indicate coordinate.
FULLSCREEN_WINDOW  		False		Makes tkinter root Fullscreen.
CLOSE_WINDOW_AFTER_SEARCH	False		Quits window after 2s of showing the grid.
ROW_SIZE			5		Indicates row length.
COLUMN_SIZE 			5		Indicates column length.
GRID_SIZE_IN_PIXELS 		100		Indicates width and height of image canvas resizing in pixels.
PADDING				2		Indicates window padding in pixels.
PADDING_BETWEEN_CELLS 		2		Indicates cell padding in pixels.
BACKGROUND_COLOR 		"white"		Indicates window background color.

----------------------------------------------------------------
