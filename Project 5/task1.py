import numpy as np
import matplotlib.pyplot as plt

n=1000000
np.random.seed(7)
x=np.random.uniform(-1.0,1.0,n) #generate 1 million pseudo random x values
y=np.random.uniform(-1.0,1.0,n) #generate 1 million pseudo random x values
d=x**2+y**2 #formula for circle
count=[0,0]
for i in range(n): #determines if point is in or out of circle
    if np.sqrt(d[i])<=1:
        count[1]=count[1]+1
        
sample=1 #initialize variables for next while statement
xi=0
yi=0
output=0
est_pi = []

while sample <= 1000000:
    xi=x[sample-1] #pick number from list starting from 0, counting up each loop
    yi=y[sample-1] #pick number from list starting from 0, counting up each loop
    if (xi**2)+(yi**2)<=1:
        output+=1 #adds 1 to counter if inside circle
    if sample==1:
        print("Using", sample ,"samples, pi is " + str(4/sample*output)) #prints value of pi for 1 sample
    if sample==10:
        print("Using", sample ,"samples, pi is " + str(4/sample*output)) #prints value of pi for 10 samples
    if sample==100:
        print("Using", sample ,"samples, pi is " + str(4/sample*output)) #prints value of pi for 100 samples
    if sample==1000:
        print("Using", sample ,"samples, pi is " + str(4/sample*output)) #prints value of pi for 1000 samples
    if sample==10000:
        print("Using", sample ,"samples, pi is " + str(4/sample*output)) #prints value of pi for 10000 samples
    if sample==100000:
        print("Using", sample ,"samples, pi is " + str(round(4/sample*output,5))) #prints value of pi for 100000 samples
    if sample==1000000:
        print("Using", sample ,"samples, pi is " + str(4/sample*output)) #prints value of pi for 1000000 samples
    est_pi.append(4/sample*output) #calculate each value of pi, add to list
    sample+=1

#######################################################################################################################

#line plot 
plt.plot(est_pi)
plt.xlabel("#samples") #x axis label
plt.ylabel("pi") #y axis label
plt.yticks([0,.5,1,1.5,2,2.5,3,3.5]) 
plt.xscale('log')
plt.show()

#######################################################################################################################

theta = np.arange(360)*2*np.pi/360 #helps construct circle
cos=np.cos(theta)
sin=np.sin(theta)

#n=10
sample = 0
plt.subplot(2, 2, 1) #creates plot
plt.plot(cos,sin,zorder=0) #creates circle
dots_in_circle = 0
sigmaf = 0
circle1x, circle1y, circle2x, circle2y, circle3x, circle3y, circle4x, circle4y=[],[],[],[],[],[],[],[]
while dots_in_circle < 10: #calculates values for number of points and sigmaf using circle formula
    xi=x[sample]
    yi=y[sample]
    if (xi**2)+(yi**2)<=1:
        circle1x.append(xi) #add points to x/y list respectively
        circle1y.append(yi)
        dots_in_circle += 1
        sigmaf += 1
    sample+=1
val=round(4*sigmaf/sample,3)
plt.scatter(circle1x,circle1y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=10, pi=" + "%.3f" % val) #title added

#n=100
plt.subplot(2, 2, 2) #creates plot
plt.plot(cos,sin,zorder=0) #creates circle
sample = 0
dots_in_circle = 0
sigmaf = 0
while dots_in_circle < 100:  #calculates values for number of points and sigmaf using circle formula
    xi=x[sample]
    yi=y[sample]
    if (xi**2)+(yi**2)<=1:
        circle2x.append(xi) #add points to x/y list respectively
        circle2y.append(yi)
        dots_in_circle += 1
        sigmaf += 1
    sample+=1
val=round(4*sigmaf/sample,3)
plt.scatter(circle2x,circle2y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=100, pi=" + "%.3f" % val) #title added

#n=1000
plt.subplot(2, 2, 3) #creates plot
plt.plot(cos,sin,zorder=0) #creates circle
sample = 0
dots_in_circle = 0
sigmaf = 0
while dots_in_circle < 1000: #calculates values for number of points and sigmaf using circle formula
    xi=x[sample]
    yi=y[sample]
    if (xi**2)+(yi**2)<=1:
        circle3x.append(xi) #add points to x/y list respectively
        circle3y.append(yi)
        dots_in_circle += 1
        sigmaf += 1
    sample+=1
val=round(4*sigmaf/sample,3)
plt.scatter(circle3x,circle3y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=1000, pi=" + "%.3f" % val) #title added

#n=10000
plt.subplot(2, 2, 4) #creates plot
plt.plot(cos,sin,zorder=0) #creates circle
sample = 0
dots_in_circle = 0
sigmaf = 0
while dots_in_circle < 10000:  #calculates values for number of points and sigmaf using circle formula
    xi=x[sample]
    yi=y[sample]
    if (xi**2)+(yi**2)<=1:
        circle4x.append(xi) #add points to x/y list respectively
        circle4y.append(yi)
        dots_in_circle += 1
        sigmaf += 1
    sample+=1
val=round(4*sigmaf/sample,3)
plt.scatter(circle4x,circle4y,color="orange",s=10,zorder=1) #more efficient way of plotting
plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.title("n=10000, pi=" + "%.3f" % val) #title added

plt.show()