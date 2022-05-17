import numpy as np


class point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

#file name
secret = open(input("Enter compressed coordinate matrix file name: "), "r")
slines = secret.readlines()

x = []
y = []
color = []

for line in slines:
    x_val, y_val, color_val = line.split()
    x.append(int(x_val))
    y.append(int(y_val))
    color.append(color_val)

points = []
for i in range(len(x)):
    c = point(x[i], y[i], color[i])
    points.append(c)


xmax = max(x)
ymax = max(y)

matrix = np.full([xmax,ymax], 0, dtype=int)

for point in points:
    #matrix[ymax-point.get_y()-1][point.get_x()-1] = point.get_color()
    matrix[point.get_x() - 1][ymax - point.get_y() - 1] = point.get_color()

mat = np.matrix(matrix)

with open('lingere.txt', 'w') as victoria:
    for line in mat:
        np.savetxt(victoria, line, fmt='%2f')







