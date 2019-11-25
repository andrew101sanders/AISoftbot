import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

file = open('input.txt')
filelines = file.readlines()
inputmatrix = []  # [Y][X] - [Rows][Columns] required for matplot (and yes this makes it very confusing to program lol)
S = []  # Original seeds from first two rows in format [x,y]
G = []  # exploring seeds
Marked = []  # Seeds that have already been explored
Lowest = [0, 0]  # [X, Y]
visited = []


def addtolist(node):  # param: [X, Y]
    if node not in G and node not in Marked:
        G.append(node)


def checksurrounding(node):  # param: [X, Y]
    addtolist(node)
    left = node[0]-1 >= 0
    top = node[1]-1 >= 0
    right = node[0]+1 <= 19
    bottom = node[1]+1 <= 19
    # TODO change this to the correct order (idk if that's needed tho lol) top-left and then go clockwise
    if left:
        if inputmatrix[node[1]][node[0] - 1] == 0:
            addtolist([node[0] - 1, node[1]])
        if top:
            if inputmatrix[node[1] - 1][node[0] - 1] == 0:
                addtolist([node[0] - 1, node[1] - 1])
        if bottom:
            if inputmatrix[node[1] + 1][node[0] - 1] == 0:
                addtolist([node[0] - 1, node[1] + 1])
    if top:
        if inputmatrix[node[1] - 1][node[0]] == 0:
            addtolist([node[0], node[1]-1])
    if right:
        if inputmatrix[node[1]][node[0] + 1] == 0:
            addtolist([node[0]+1, node[1]])
        if top:
            if inputmatrix[node[1] - 1][node[0] + 1] == 0:
                addtolist([node[0] + 1, node[1] - 1])
        if bottom:
            if inputmatrix[node[1] + 1][node[0] + 1] == 0:
                addtolist([node[0] + 1, node[1] + 1])
    if bottom:
        if inputmatrix[node[1] + 1][node[0]] == 0:
            addtolist([node[0], node[1]+1])


# populate inputmatrix
for y in filelines:
    temp = []
    for x in y:
        if x != '\n':
            temp.append(int(x))
    inputmatrix.append(temp)

# populate S with first row of inputmatrix
for index, firstrowitem in enumerate(inputmatrix[0]):
    if inputmatrix[0][index] == 0:
        S.append([index, 0])

# populate S with second row of inputmatrix
for index, firstrowitem in enumerate(inputmatrix[1]):
    if inputmatrix[1][index] == 0:
        S.append([index, 1])

# Go through seeds in S and try to find path
for initialseed in S:
    G = []
    visited = []
    if initialseed not in Marked:
        Marked.append(initialseed)
        checksurrounding(initialseed)
        while G.__len__() != 0:
            temp = G.pop()
            if temp[1] > Lowest[1]:
                Lowest = temp
            visited.append(temp)
            Marked.append(temp)
            checksurrounding(temp)


print(Lowest)
ax = plt.subplot()
cmap = colors.ListedColormap(['red', 'blue'])
ax.imshow(inputmatrix, cmap)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 20, 1))
ax.set_yticks(np.arange(-.5, 20, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.show()
