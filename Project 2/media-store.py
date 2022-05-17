#### Import Modules
import inventory 
import MediaItem

from inventory import Inventory
from MediaItem import __init__
'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''

my_inventory=Inventory() #allows for inventory file to be used

print("Welcome to BestMedia\n====================")

command=999 #starts at a number above 0 to start loop
while command>0: #
    my_inventory.display_menu() #displays menu on startup and after executing a command
    command=int(input("Enter Command: "))
    if command==1: #each command (0-8) lauches a different function
        my_inventory.display()
    elif command==2:
        my_inventory.info()
    elif command==3:
        my_inventory.display_book()
    elif command==4:
        my_inventory.display_movie()
    elif command==5:
        my_inventory.search_item()
    elif command==6:
        my_inventory.search_index_item()
    elif command==7:
        my_inventory.create_item()
    elif command==8:
        my_inventory.max_price()
    elif command>=9:    #If a number is greater than 8, user instructed to choose a valid command 
        print("Not a Valid Command. Try Again.")
    elif command==0: #ends program if input is 0
        print("Goodbye")
        break
