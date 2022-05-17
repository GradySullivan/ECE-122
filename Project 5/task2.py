import numpy as np
import matplotlib.pyplot as plt

coords1 = input("Enter (x,y) of point-1, default is (0.5,0.5):")
if coords1 == "":
    coords1 = ".5 .5"

coords2 = input("Enter (x,y) of  point-2, default is (3,2.5):")
if coords2 == "":
    coords2 = "3 2.5"

coords3 = input("Enter (x,y) of  point-3, default is (1,3):")
if coords3 == "":
    coords3 = "1 3"
    
varlist = []
for i in coords1.split():
    varlist.append(float(i))
for i in coords2.split():
    varlist.append(float(i))
for i in coords3.split():
    varlist.append(float(i))
x1, y1, x2, y2, x3, y3 = varlist

if (x1>=x2) and (x1>=x3): #checks for greatest x value
    bigx=x1
elif (x2>=x1) and (x2>=x3):
    bigx=x2
else:
    bigx=x3
    
if (x1<=x2) and (x1<=x3): #checks for smallest y value
    smallx=x1
elif (x2<=x1) and (x2<=x3):
    smallx=x2
else:
    smallx=x3

if (y1>=y2) and (y1>=y3): #checks for greatest y value
    bigy=y1
elif (y2>=y1) and (y2>=y3):
    bigy=y2
else:
    bigy=y3
    
if (y1<=y2) and (y1<=y3): #checks for smallest y value
    smally=y1
elif (y2<=y1) and (y2<=y3):
    smally=y2
else:
    smally=y3

omega=(bigx-smallx)*(bigy-smally)
n=100000
np.random.seed(7)
x=np.random.uniform(smallx,bigx,n) #generates 100K x values between x min and x max
y=np.random.uniform(smally,bigy,n) #generates 100K y values between y min and y max

sample=1 #create variables used in while loop later
xi=0
yi=0
output=0
calc=np.matrix([[x1,x2,x3],[y1,y2,y3],[1,1,1]]) #creates part of system matrix
est_area=[]

while sample <= 100000:
    xi=x[sample-1]
    yi=y[sample-1]
    xy = np.matrix([[xi],[yi],[1]])
    if np.linalg.solve(calc,xy)[0][0] > 0 and np.linalg.solve(calc,xy)[1][0] > 0 and np.linalg.solve(calc,xy)[2][0] > 0: 
        output+=1
    v=omega/sample*output
    if sample==1:
        print("Using", sample ,"area of triangle is " + str(v))
    if sample==10:
        print("Using", sample ,"area of triangle is " + str(v))
    if sample==100:
        print("Using", sample ,"area of triangle is " + str(v))
    if sample==1000:
        print("Using", sample ,"area of triangle is " + str(v))
    if sample==10000:
        print("Using", sample ,"area of triangle is " + str(v))
    if sample==100000:
        print("Using", sample ,"area of triangle is " + str(v))
    est_area.append(v)
    sample+=1

#line plot 
plt.plot(est_area)
plt.xlabel("#samples") #x axis label
plt.ylabel("Area-Triangle") #y axis
plt.yticks([0,.5,1,1.5,2,2.5,3]) #increment of y axis
plt.xscale('log') #x axis is log based
plt.show()

tri1x, tri1y, tri2x, tri2y, tri3x, tri3y, tri4x, tri4y=[],[],[],[],[],[],[],[]

#n=10
sample = 0
plt.subplot(2, 2, 1) #creates plot
plt.plot([x1,x2,x3,x1], [y1,y2,y3,y1],zorder=0) #creates triangle
dots_in_triangle = 0
sigmaf = 0
while dots_in_triangle < 10: #calculates values for number of points and sigmaf using triangle formula
    xi=x[sample]
    yi=y[sample]
    xy = np.matrix([[xi],[yi],[1]])
    if np.linalg.solve(calc,xy)[0][0] > 0 and np.linalg.solve(calc,xy)[1][0] > 0 and np.linalg.solve(calc,xy)[2][0] > 0: #solve for matrix
        tri1x.append(xi) #add points to x/y list respectively
        tri1y.append(yi)
        dots_in_triangle += 1
        sigmaf += 1
    sample+=1
val=round(omega*sigmaf/sample,3) #round to three decimal places
plt.scatter(tri1x,tri1y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=10, area=" + "%.3f" % val) #title added

#n=100
plt.subplot(2, 2, 2) #creates plot
plt.plot([x1,x2,x3,x1], [y1,y2,y3,y1], zorder=0) #creates triangle
sample = 0
dots_in_triangle = 0
sigmaf = 0
while dots_in_triangle < 100:  #calculates values for number of points and sigmaf using triangle formula
    xi=x[sample]
    yi=y[sample]
    xy = np.matrix([[xi],[yi],[1]])
    if np.linalg.solve(calc,xy)[0][0] > 0 and np.linalg.solve(calc,xy)[1][0] > 0 and np.linalg.solve(calc,xy)[2][0] > 0: #solve for matrix
        tri2x.append(xi) #add points to x/y list respectively
        tri2y.append(yi)
        dots_in_triangle += 1
        sigmaf += 1
    sample+=1
val=round(omega*sigmaf/sample,3) #round to three decimal places
plt.scatter(tri2x,tri2y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=100, area=" + "%.3f" % val) #title added

#n=1000
plt.subplot(2, 2, 3) #creates plot
plt.plot([x1,x2,x3,x1], [y1,y2,y3,y1],zorder=0) #creates triangle
sample = 0
dots_in_triangle = 0
sigmaf = 0
while dots_in_triangle < 1000: #calculates values for number of points and sigmaf using triangle formula
    xi=x[sample]
    yi=y[sample]
    xy = np.matrix([[xi],[yi],[1]])
    if np.linalg.solve(calc,xy)[0][0] > 0 and np.linalg.solve(calc,xy)[1][0] > 0 and np.linalg.solve(calc,xy)[2][0] > 0: #solve for matrix
        tri3x.append(xi) #add points to x/y list respectively
        tri3y.append(yi)
        dots_in_triangle += 1
        sigmaf += 1
    sample+=1
val=round(omega*sigmaf/sample,3) #round to three decimal places
plt.scatter(tri3x,tri3y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=1000, area=" + "%.3f" % val) #title added

#n=10000
plt.subplot(2, 2, 4) #creates plot
plt.plot([x1,x2,x3,x1], [y1,y2,y3,y1],zorder=0) #creates triangle
sample = 0
dots_in_triangle = 0
sigmaf = 0
while dots_in_triangle < 10000:  #calculates values for number of points and sigmaf using triangle formula
    xi=x[sample]
    yi=y[sample]
    xy = np.matrix([[xi],[yi],[1]])
    if np.linalg.solve(calc,xy)[0][0] > 0 and np.linalg.solve(calc,xy)[1][0] > 0 and np.linalg.solve(calc,xy)[2][0] > 0: #solve for matrix
        tri4x.append(xi) #add points to x/y list respectively
        tri4y.append(yi)
        dots_in_triangle += 1
        sigmaf += 1
    sample+=1
val=round(omega*sigmaf/sample,3) #round to three decimal places
plt.scatter(tri4x,tri4y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=10000, area=" + "%.3f" % val) #title added

plt.show()


