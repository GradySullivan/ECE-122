import numpy as np

secret=open(input("Enter compressed coordinate matrix file name: "),"r") #input compressed file 
read=secret.readlines()

x,y,color=[],[],[] #initialize lists

for line in read: #for each line in .txt file
    xval, yval, colorval = line.split() #splits three columns 
    color.append(colorval)
    x.append(int(xval)) #adds x values to list
    y.append(int(yval)) #adds y values to list
    
xmax,ymax=max(x),max(y)

matrix=np.full([xmax,ymax],0,dtype=int) #creates array of zeros - white background

i=0
while i < (len(x)-1):
    matrix[x[i]-1][ymax-y[i]-1] = color[i] #inputs non-white colors into matrix
    i+=1
    
matr=np.matrix(matrix) #creates matrix

with open('secretimage.txt','w') as image: #opens file
    for line in matr:
        np.savetxt(image,line,fmt='%2f') #saves each line in matrix