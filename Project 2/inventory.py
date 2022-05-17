from MediaItem import MediaItem #to communicate with MediaItem class

class Inventory: #all functions for commands inside
    
    maxprice=100 #initial value of max price set to 100
    
    def display_menu(self): #displays menu
        print("\nMenu")
        print("====")
        print("1-List Inventory")
        print("2-Info Inventory")
        print("3-List of All Books");
        print("4-List of All Movies");
        print("5-Item Description");
        print("6-Remove Item");
        print("7-Add Item");
        print("8-Set Maximum Price");
        print("0-Exit");
    
####### All other functions listed below
        
    def __init__(self): #creates list of media with attributes included
        self.media_list = [MediaItem("Movie","2001: A Space Odyssey","$11.99","TU2RL012","Stanley Kubrick","Keir Dullea",None),
                           MediaItem("Book","A Brief History of Time","$10.17","GV5N32M9",None,None,"Stephen Hawking"),
                           MediaItem("Movie","North by Northwest","$8.99","1DB6HK3L","Alfred Hitchcock","Cary Grant",None),
                           MediaItem("Movie","The Good, The Bad and The Ugly","$9.99","PO5T7Y89","Sergio Leone","Clint Eastwood",None),
                           MediaItem("Book","The Alchemist","$6.99","TR3FL0EW",None,None,"Paulo Coelho"),
                           MediaItem("Book","Thus Spoke Zarathustra","$7.81","F2O9PIE9",None,None,"Friedrich Nietzsche"),
                           MediaItem("Book","Jonathan Livingston Seagull","$6.97","R399CED1",None,None,"Richard Bach"),
                           MediaItem("Movie","Gone with the Wind","$4.99","2FG6B3N9","Victor Fleming","Vivien Leigh",None),
                           MediaItem("Book","Gone with the Wind","$7.99","6Y9OPL87",None,None,"Margarett Mitchell")]
    
    def display(self):  #command 1
        print("\nReference/Media/Title/Price (max=$" + str(self.maxprice) + " )\n---------------------------")
        for item in self.media_list: #checks the following if statement for each item in list
            mp = float(self.maxprice)
            ip = float(item.price[1:])
            if mp >= ip: #if the max price is greater than the price of item, it will print the price of item with certain attributes
                print(item.ref + " " + item.media + " " + item.title + " " + item.price)

    def display_book(self): #command 3
        media_check=" "
        print("\nReference/Media/Title/Price (max=$" + str(self.maxprice) + " )\n---------------------------")
        for item in self.media_list:
            media_check=item.media #blank variable is set to value of media type attribute
            if media_check=="Book": #if the attribute is a book, print info on it
                print(item.ref + " " + item.media + " " + item.title + " " + item.price)
    
    def display_movie(self): #command 4
        media_check=" "
        print("\nReference/Media/Title/Price (max=$" + str(self.maxprice) + ")\n---------------------------")
        for item in self.media_list:
            media_check=item.media #blank variable set to value of media type attribute
            if media_check=="Movie": #if attribute is a movie, print info
                print(item.ref + " " + item.media + " " + item.title + " " + item.price)
            
    def info(self): #command 2
        total_price=0
        expensive=[]
        media_check=""
        book=0
        movie=0
        for item in self.media_list: #completes following for each item in list
            media_check=item.media
            if media_check=="Book": #every book adds 1 to count
                book=book+1
            else:
                movie=movie+1 #every movie adds 1 to count
            price=item.price[1:] #gets price value without "$"
            expensive.append(float(price)) #adds prices to a list, to add up
            total_price=total_price+float(item.price[1:]) #calculates total price
        print("Inventory is worth $" + str(total_price)) 
        print("Most expensive item at $" + str(max(expensive)))
        print("There are " + str(book) + " Book(s), and " + str(movie) + " Movie(s)")
        
    def search_item(self): #command 5
        look_for = input("Enter Item Reference: ") #user inputs reference number
        found=0
        for item in self.media_list:
            if item.ref==look_for: #if ref number found, adds one to found, later used in another conditional statement
                found=found+1
                if item.media == "Book": #prints book info if book
                    print("Title: " + item.title + " (Ref: " + item.ref +", Price: " + item.price + ";")
                    print("Author: " + item.author)
                elif item.media == "Movie": #prints movie info if movie
                    print("Title: " + item.title + " (Ref: " + item.ref +", Price: " + item.price + ";")
                    print("Movie Director: " + item.director + "; Lead Actor: " + item.lead_actor)
                    found=found+1
        if found==0:
            print("No such item found!") #if found variable doesn't increase, no item has been found
        else:
            found=0
    
    def search_index_item(self): #command 6
        search_index = input(str(("Enter Item Reference: ")))
        i=0
        for item in self.media_list: 
            if search_index == item.ref: #if ref number matches input, it deletes that media from list
                del self.media_list[i]
            i=i+1 #keeps track of what number in list for deleting correct media
                
    def create_item(self): #command 7
        var1 = input(str("Book or Movie? ")) #asks for which type of media
        if var1 == "Book": #inputting "Book" asks for book related attributes
            var2 = input(str("Enter Book Title: "))
            var3 = input(str("Enter Book Reference: "))
            var4 = "$" + input(str("Enter Book Price: "))
            var5 = input(str("Enter Author Name: "))
            var6 = None
        elif var1 == "Movie": #inputting "Movie" asks for book related attributes
            var2 = input(str("Enter Movie Title: "))
            var3 = input(str("Enter Movie Reference: "))
            var4 = input(str("Enter Movie Price: "))
            var5 = input(str("Enter Director Name: "))
            var6 = input(str("Enter Lead Actor Name: "))
        else: #if neither movie or book selected, error output selected
            print("Wrong input!")
        self.media_list.append(MediaItem(var1,var2,str(var4),var3,var5,var6,var5))
        
    def max_price(self): #allows user to set maximum price for what shows up in list (command 1)
        self.maxprice = input(str("Enter maximum price (current=$"+str(self.maxprice) + "): "))