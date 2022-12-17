import json
from tkinter import *
from canvas import CreateLabel
import os
import glob
import random
import PIL.ImageGrab as ImageGrab
import steam

#Gets parameters
with open("parameters.json") as f:
    data=json.load(f)
    g=data["main.py"]
    h=data["steam.py"]

    RESIZE = g["RESIZE"]
    DELETE_IMAGES = g["RESIZE"]
    GENERATE_LABEL = g["GENERATE_LABEL"]
    FULLSCREEN_WINDOW = g["FULLSCREEN_WINDOW"]
    CLOSE_WINDOW_AFTER_SEARCH=g["CLOSE_WINDOW_AFTER_SEARCH"]
    ROW_SIZE = g["ROW_SIZE"]
    COLUMN_SIZE = g["COLUMN_SIZE"]
    GRID_SIZE_IN_PIXELS = g["GRID_SIZE_IN_PIXELS"]
    PADDING = g["PADDING"]
    PADDING_BETWEEN_CELLS = g["PADDING_BETWEEN_CELLS"]
    BACKGROUND_COLOR = g["BACKGROUND_COLOR"]

    steam.MAX_IMAGES=h["MAX_IMAGES"]
    steam.API_KEY = h["API_KEY"]

#Run steam.py:
steam.main()

path_list = ["./STEAMIMAGES/1024x1024", "./STEAMIMAGES/920x430", "./STEAMIMAGES/600x900"]
image_list_1024x1024 = list(glob.glob(os.path.join(path_list[0], '*.*')))
image_list_920x400 = list(glob.glob(os.path.join(path_list[1], '*.*')))
image_list_600x900 = list(glob.glob(os.path.join(path_list[2], '*.*')))

image_list = [image_list_920x400, image_list_600x900, image_list_1024x1024]
coord_list = []
type = ""
canvas_list = []

window = Tk()
window.config(background=BACKGROUND_COLOR, padx=PADDING, pady=PADDING)
if FULLSCREEN_WINDOW:
    window.attributes("-fullscreen", True)
window.title("Grid Generator")

#Optional Label
def generate_label(i, j, label):
    if label:
        label = Label(text=f"{i}:{j}", font=("Arial", 15, "bold"))
        label.grid(row=i, column=j)
# Output screenshot
def save_image():
    box = (window.winfo_rootx(), window.winfo_rooty(), window.winfo_rootx() + window.winfo_width(),
           window.winfo_rooty() + window.winfo_height())
    screenshot = ImageGrab.grab(bbox=box)
    #Creates COLLAGE dir
    dir = os.path.join("./", "COLLAGE")
    if not os.path.exists(dir):
        os.mkdir(dir)
    screenshot.save(f"./COLLAGE/{random.randrange(1000)}.png")
# Append to list of coordinates
def append_coord(i, j, type):
    coord_list.append((i, j))
    if type == "big":
        coord_list.append((i, j + 1))
        coord_list.append((i + 1, j))
        coord_list.append((i + 1, j + 1))
    if type == "medium":
        coord_list.append((i, j + 1))
    if type == "medium2":
        coord_list.append((i + 1, j))
# Checks type of image
def get_type(image):
    if image in big:
        return "big"
    elif image in medium:
        return "medium"
    elif image in medium2:
        return "medium2"


i = 0
while i <= ROW_SIZE:
    j = 0
    while j <= COLUMN_SIZE:
        # Check if position is not empty
        if (i, j) in coord_list:
            j += 1
            continue
        # Separate image list
        medium, medium2, big = [image_list[i] for i in (0, 1, 2)]

        # Pick random image from image_list
        random_choice = random.randrange(len(image_list))
        #Check images left
        if len(image_list[random_choice])==0:
            j+=1
            print(f"Not enough images in {image_list[random_choice]}")
            continue

        item = image_list[random_choice][random.randrange(len(image_list[random_choice]))]
        type = get_type(item)

        print("Checking " + item)

        # BIG/SMALL Canvas
        if item in big:
            # Check nearby cells
            if (i, j) not in coord_list and (i + 1, j + 1) not in coord_list and (i + 1, j) not in coord_list and (
            i, j + 1) not in coord_list and j != COLUMN_SIZE and i != ROW_SIZE:
                canvas = CreateLabel(RESIZE, item, type, i, j, window, 2, 2, GRID_SIZE_IN_PIXELS, PADDING_BETWEEN_CELLS)
                canvas_list.append(canvas)
                generate_label(i, j, GENERATE_LABEL)
                append_coord(i, j, "big")
                j += 2
                print("big")
            else:
                # If doesnt fit, resize into small
                type = "small"
                if (i, j) not in coord_list:
                    canvas = CreateLabel(RESIZE, item, type, i, j, window, 1, 1, GRID_SIZE_IN_PIXELS,
                                         PADDING_BETWEEN_CELLS)
                    canvas_list.append(canvas)
                    generate_label(i, j, GENERATE_LABEL)
                    append_coord(i, j, "small")
                    j += 1
                    print("small")
                else:
                    # Gets another image
                    print("Cannot fit")
                    continue
        # MEDIUM Canvas
        if item in medium:

            if (i, j) not in coord_list and (i, j + 1) not in coord_list and j != COLUMN_SIZE:

                canvas = CreateLabel(RESIZE, item, type, i, j, window, 2, 1, GRID_SIZE_IN_PIXELS, PADDING_BETWEEN_CELLS)
                canvas_list.append(canvas)
                generate_label(i, j, GENERATE_LABEL)
                append_coord(i, j, "medium")
                j += 2
                print("medium")
            else:
                # Gets another image
                print("Cannot fit")
                continue
        # MEDIUM2 Canvas
        elif item in medium2:

            if (i, j) not in coord_list and (i + 1, j) not in coord_list and i != ROW_SIZE:

                canvas = CreateLabel(RESIZE, item, type, i, j, window, 1, 2, GRID_SIZE_IN_PIXELS, PADDING_BETWEEN_CELLS)
                canvas_list.append(canvas)
                generate_label(i, j, GENERATE_LABEL)
                append_coord(i, j, "medium2")
                j += 1
                print("medium2")

            else:
                # Gets another image
                print("Cannot fit")
                continue

        image_list[random_choice].remove(item)

    i += 1
coord_list.sort()


window.after(1000, save_image)
print(f"Saved screenshot in ./COLLAGE")
if CLOSE_WINDOW_AFTER_SEARCH:
    window.after(2000, window.destroy)

window.mainloop()

# Delete images from STEAMIMAGES folder
if DELETE_IMAGES:
    for path in path_list:
        print(f"Removed images from {path}")
        files = glob.glob(f"{path}/*")
        for f in files:
            os.remove(f)
