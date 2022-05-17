from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import Tk
from tkinter import Canvas
import math
import time

""" to complete """

bounds=input("Enter xmin,xmax,ymin,ymax (return for default -300,300,-300,300):" )
if bounds == "":
    bounds = "-300 300 -300 300"

inputs=input("Enter x0,y0,v,theta (return for default 0,0,70,30): ")
if inputs == "":
    inputs = "0 0 70 30"

varlist = []
for i in bounds.split():
    varlist.append(float(i))
for i in inputs.split():
    varlist.append(float(i))
    
xmin, xmax, ymin, ymax, x0, y0, v, theta= varlist
theta = math.radians(theta)

m = Mapping_for_Tkinter(xmin, xmax, ymin, ymax, 600)

rebounds=0     

root = Tk()
canvas = Canvas(root, width=600,height=m.get_height(),bg="white")
canvas.pack()

ball=canvas.create_oval(m.get_i(x0)-4,m.get_j(y0)-4,m.get_i(x0)+4,m.get_j(y0)+4,fill="blue") 

v=v/10
t=0
t_rel = 0 #relative time (since last bounce)
#starting position
x = x0
y = y0

root.update()
time.sleep(1)

while t<1500:
    # keep track of old position
    xold = x
    yold = y
    
    # update x and y
    x=x0+v*math.cos(theta)*t_rel
    y=y0+v*math.sin(theta)*t_rel
    
    # move the ball
    canvas.move(ball,x-xold,yold-y)
    # recording the new position of the ball
    canvas.create_oval(m.get_i(x)-1,m.get_j(y)-2,m.get_i(x)+1,m.get_j(y)+1,fill="black")
    root.update()
    
    # handle collisions
    if (y > ymax and math.sin(theta) > 0):
        theta=-theta
        rebounds=rebounds+1
        t_rel = 0
        x0, y0 = x, ymax
    
    if (y < ymin and math.sin(theta) < 0):
        theta=-theta
        rebounds=rebounds+1
        t_rel = 0
        x0, y0 = x, ymin
    
    if (x > xmax and math.cos(theta) > 0):
        theta=math.pi-theta
        rebounds=rebounds+1
        x0, y0 = xmax, y
        t_rel = 0
    
    if (x < xmin and math.cos(theta) < 0):
        theta=math.pi-theta
        rebounds=rebounds+1
        x0, y0 = xmin, y
        t_rel = 0
    
    
    #iteration
    root.update()
    time.sleep(.01)
    t_rel +=1
    t+=1

canvas.itemconfig(ball, fill="red")
root.update()

print("\nTotal number of rebounds is:", rebounds)
root.mainloop()
        