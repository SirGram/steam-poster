from steamgrid import SteamGridDB,MimeType,StyleType
import requests
import random
import threading

#API Key
sgdb = SteamGridDB('a180935d7445430074b645cf3d5097ee')

game_list=[]
with open("list_of_games.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        game_list.append(line.strip())


number_of_images=0
MAX_IMAGES=300

def worker():
    global number_of_images
    global MAX_IMAGES

    search=random.choice(game_list)
    print(f"Searching for {search}")
    #Search within database
    results=sgdb.search_game(search)
    #Goes through first 3 results
    for result in results[0:2]:
        grids=sgdb.get_grids_by_gameid(game_ids=[result.id], mimes=[MimeType.PNG], styles=[StyleType.Alternate])
        #If no grid, repeats search
        if grids==None:
            continue
        for grid in grids:
            if number_of_images > MAX_IMAGES:
                break

            #Url request
            img_data=requests.get(grid).content
            #Check file size
            if grid.height==430 and grid.width==920:
                path=f"./STEAMIMAGES/920x430/{grid.id}.png"
            elif (grid.height==1024 and grid.width==1024) or (grid.height==512 and grid.width==512):
                path = f"./STEAMIMAGES/1024x1024/{grid.id}.png"
            elif grid.height==900 and grid.width==600:
                path = f"./STEAMIMAGES/600x900/{grid.id}.png"
            else:
                print(f"Invalid grid size fetched: {grid.width}x{grid.height}")
                continue
            #Bytes
            f=open(path, "wb")
            f.write(img_data)
            f.close()
            number_of_images+=1
            print(f"Downloaded: {number_of_images} images")


thread_list=[]
for i in range(50):
    t=threading.Thread(target=worker)
    thread_list.append(t)
    t.start()
for i in thread_list:
    t.join()




