""" Enter your name(s) here
Smit Patel
Grady Sullivan
"""
from tkinter import Tk
from tkinter import Canvas

class Mapping_for_Tkinter:

    """ to complete"""
    def __init__(self,xmin,xmax,ymin,ymax,width): #creates __init__ method
        self.set_xmin(xmin)
        self.set_xmax(xmax)
        self.set_ymin(ymin)
        self.set_ymax(ymax)
        self.set_width(width)
        self.__set_height()
        
    def __str__(self): #return info on object in as string
        return "Mapping created between x=[%.1f,%.1f] y=[%.1f,%.1f] math => (%i,%i) tkinter" % (
            self.get_xmin(),
            self.get_xmax(),
            self.get_ymin(),
            self.get_ymax(),
            self.get_width(),
            self.get_height()
        )
        
    def set_xmin(self,xmin): #getter method for xmin
        self.__xmin=xmin
        
    def get_xmin(self): #setter method for xmax
        return self.__xmin
    
    def set_xmax(self,xmax):
        self.__xmax=xmax
        if self.__xmin >= self.__xmax: #condition true if xmin is greater than xmax
            self.__xmin,self.__xmax=input("Your xmax is invalid (xmax<=xmin), Re-Enter correct [xmin,xmax]: ").split()
            self.__xmin=int(self.__xmin)
            self.__xmax=int(self.__xmax)
            
    def get_xmax(self): #getter method for xmax
        return self.__xmax
            
    def set_ymin(self,ymin): #setter method for ymin
        self.__ymin=ymin
        
    def get_ymin(self): #getter method for ymin
        return self.__ymin
    
    def set_ymax(self,ymax):
        self.__ymax=ymax
        if self.__ymin >= self.__ymax: #condition true if ymin is greater than ymax
            self.__ymin,self.__ymax=input("Your ymax is invalid (ymax<=ymin), Re-Enter correct [ymin,ymax]: ").split()
            self.__ymin=int(self.__ymin)
            self.__ymax=int(self.__ymax)
        
    def get_ymax(self): #getter method for ymax
        return self.__ymax
    
    def set_width(self,width): #setter method for width
        self.__width=width
    
    def get_width(self): #getter method for width
        return self.__width
    
    def __set_height(self): #setter method for height (calculates height from y/x min/max)
         self.__height=int((self.get_ymax()-self.get_ymin())*(self.get_width()/(self.get_xmax()-self.get_xmin())))
        
    def get_height(self): #getter method for height
        return self.__height  

    def get_x(self,i): #converts i to x
        return i*(self.get_xmax()-self.get_xmin())/(self.get_width())+self.get_xmin()
    
    def get_y(self,j): #converts j to y
        return (self.get_height()-j)*((self.get_ymax()-self.get_ymin())/self.get_height())+self.get_ymin()
    
    def get_i(self,x): #converts x to i
        return (x-self.get_xmin())*(self.get_width()/(self.get_xmax()-self.get_xmin()))
    
    def get_j(self,y): #convertsy to j
        return self.get_height()-(self.get_height()/(self.get_ymax()-self.get_ymin()))*(y-self.get_ymin())
    
    
def main():
    m=Mapping_for_Tkinter(-5.0,5.0,-5.0,5.0,500) # instantiate mapping
    print(m) # print info about object
    
    window = Tk() # instantiate a tkinter window
    canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
    canvas.pack()
    # create rectangle the Tkinter way
    print("Draw rectangle using tkinter coordinates at (100,400) (400,100)")
    canvas.create_rectangle(100,400,400,100,outline="black")
    
    # create circle using the mapping
    print("Draw circle using math coordinates at center (0,0) with radius 3")
    canvas.create_oval(m.get_i(-3.0),m.get_j(-3.0),m.get_i(3.0),m.get_j(3.0),outline="blue")
    
    # create y=x line pixel by pixel using the mapping
    print("Draw line math equation y=x pixel by pixel using the mapping")
    for i in range(m.get_width()):
        x=m.get_x(i) # obtain the x coordinate
        y=x
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="green") 

    
    window.mainloop() # wait until the window is closed


if __name__=="__main__":
    main()