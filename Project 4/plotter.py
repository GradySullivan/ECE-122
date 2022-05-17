from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import Tk
from tkinter import Canvas
import math
from math import sin
from math import cos
from math import tan

#### formula input
formula=input("Enter math formula (using x variable): ")


"""to complete"""

coords=input("Enter xmin,xmax,ymin,ymax (return for default -5,5,-5,5): ") #input for x and y min/max
if coords == "":
        coords = "-5 5 -5 5" #changes values to "defaults" if nothing is inputted
        
floatlist = []
for coord in coords.split():
    floatlist.append(float(coord)) #adds x and y min/max to list

xmin, xmax, ymin, ymax = floatlist #assigns variables to parts of list

m = Mapping_for_Tkinter(xmin, xmax, ymin, ymax, 800)
   
floatlist.insert(0,float(m.get_xmin())) #changes x's and y's to i's and j's
floatlist.insert(1,float(m.get_xmax()))
floatlist.insert(2,float(m.get_ymin()))
floatlist.insert(3,float(m.get_ymax()))

window = Tk() # instantiate a tkinter window
canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
canvas.pack()

for i in range(m.get_width()): #evaluates the "y" value at each "x" and creates part of the line (very small rectangle)
    x=m.get_x(i)
    y=eval(formula)
    canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="blue")

canvas.create_line(m.get_i(0),+m.get_height(),m.get_i(0),0,fill="black") #creates y axis
canvas.create_line(0,+m.get_j(0),m.get_width(),m.get_j(0),fill="black") #creates x axis

window.mainloop()
