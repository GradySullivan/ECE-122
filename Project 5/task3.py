import matplotlib.pyplot as plt
import numpy as np

########################################################################

#inputs

n = input("Newton fractal z**n=1, Enter n (default 3): ") #input for n
if n == "": #set n equal to 3 if no input given
    n = "3"
n=int(n) #changes input into integer value

bounds = input("Enter xmin,xmax,ymin,ymax (default -1.35,1.35,-1.35,1.35): ") #input for bounds of x and y axis for plot

bounds_list = []
if bounds == "": #default values if no input given
    bounds = "-1.35 1.35 -1.35 1.35"

varlist = [] 
for i in bounds.split(): #splits bounds, converts string to float and adds to list
    varlist.append(float(i))
xmin, xmax, ymin, ymax = varlist

x=np.linspace(xmin+.0011,xmax,1000) #generates 1000 random x values in x bound range
y=np.linspace(ymin+.0011,ymax,1000) #generates 1000 random y values in y bound range

##################################################################

#calculations

print("Solutions are")

sol=[] 
m=0 #counter for while loop
while m < n:
    solution=np.exp(1j*((2*np.pi*m)/n)) #equation (1) from assignment
    sol.append(solution) #add to list sol
    print(sol[m])
    m+=1
    
C=np.zeros((1000, 1000), dtype=complex) #creates array (1000x1000) filled with 0s
i=0
while i < 1000:
    for j in range(1000):
        C[i,j]=x[j]+1j*y[999-i] #calculate complex numbers
    i+=1
j=0
while j < (20): #Newton iteration
    C=(C-(((C**n)-1)/(n*(C**(n-1)))))
    j+=1

color=np.zeros((1000,1000)) #matrix for color values
i=0
while i < 1000:
    for j in range(1000):
        der=[]
        for m in range(n):
            der.append(abs(C[i,j]-sol[m])/(abs(sol[m]))) #all root solutions
        color[i,j]=der.index(min(der))*255/(n-1) #color assigned
    i+=1

###########################################################################
    
#plotting

plt.xlabel("x") #label x axis
plt.ylabel("y") #label y axis
plt.imshow(color, cmap="rainbow", extent=(xmin, xmax, ymin, ymax), interpolation= "bilinear",origin="upper")
plt.show()