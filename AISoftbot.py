import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

file = open('C:/users/andrew/desktop/input.txt')
filelines = file.readlines()
inputmatrix = []  # [y][x] - [Rows][Columns] required for matplot
S = []  # Original seeds from first two rows in format [x,y]
G = []  # Surrounding seeds
Marked = []  # Seeds that have already been explored


def checksurrounding(node):  # [X, Y]
    print('hi')


# populate inputmatrix
for x in filelines:
    temp = []
    for y in x:
        if y != '\n':
            temp.append(int(y))
    inputmatrix.append(temp)

# populate S with first row of inputmatrix
for index, firstrowitem in enumerate(inputmatrix[0]):
    if inputmatrix[0][index] == 0:
        S.append([0, index])

# populate S with second row of inputmatrix
for index, firstrowitem in enumerate(inputmatrix[1]):
    if inputmatrix[1][index] == 0:
        S.append([1, index])

for initialseeds in S:
    print(initialseeds)


ax = plt.subplot()
cmap = colors.ListedColormap(['red', 'blue'])
ax.imshow(inputmatrix, cmap)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 20, 1))
ax.set_yticks(np.arange(-.5, 20, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.show()
