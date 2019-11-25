import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

file = open('C:/users/andrew/desktop/input.txt')
filelines = file.readlines()
inputmatrix = []
S = []
G = []
markedseeds = []


def checkdup(dup):
    if dup not in G and dup not in markedseeds and dup not in S:
        G.append(dup)


for line in filelines:
    temp = []
    for char in line:
        if char != '\n':
            temp.append(int(char))
    inputmatrix.append(temp)

i = 0
for seed in inputmatrix[0]:
    if seed == 0:
        S.append([i, 0])
    i += 1

i = 0
for seed in inputmatrix[1]:
    if seed == 0:
        S.append([i, 1])
    i += 1

for startseed in S:
    marked = False
    if startseed in markedseeds:
        marked = True
    if not marked:
        markedseeds.append(startseed)
        left = startseed[0] - 1 >= 0
        top = startseed[1] - 1 >= 0
        right = startseed[0] + 1 <= 19
        bottom = startseed[1] - 1 <= 19
        if left:  # left side
            if inputmatrix[startseed[0] - 1][startseed[1]] == 0:  # middle left
                checkdup([startseed[0] - 1, startseed[1]])
            if top:  # top left
                if inputmatrix[startseed[0] - 1][startseed[1] - 1] == 0:
                    checkdup([startseed[0] - 1, startseed[1] - 1])
            if bottom:  # bottom left
                if inputmatrix[startseed[0] - 1][startseed[1] + 1] == 0:
                    checkdup([startseed[0] - 1, startseed[1] + 1])
        if top:  # top middle
            if inputmatrix[startseed[0]][startseed[1] - 1] == 0:
                checkdup([startseed[0], startseed[1] - 1])
        if bottom:  # bottom middle
            if inputmatrix[startseed[0]][startseed[1] + 1] == 0:
                checkdup([startseed[0], startseed[1] + 1])
        if right:  # right side
            if inputmatrix[startseed[0] + 1][startseed[1]] == 0:  # middle right
                checkdup([startseed[0] + 1, startseed[1]])
            if top:  # top right
                if inputmatrix[startseed[0] + 1][startseed[1] - 1] == 0:
                    checkdup([startseed[0] + 1, startseed[1] - 1])
            if bottom:  # bottom right
                if inputmatrix[startseed[0] + 1][startseed[1] + 1] == 0:
                    checkdup([startseed[0] + 1, startseed[1] + 1])

print('inputmatrix: ' + str(inputmatrix))
print('S (original seeds from first 2 rows): ' + str(S))
print('G (surroundings of original seeds): ' + str(G))
print('markedseeds: ' + str(markedseeds))

ax = plt.subplot()
cmap = colors.ListedColormap(['red', 'blue'])
ax.imshow(inputmatrix, cmap)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 20, 1))
ax.set_yticks(np.arange(-.5, 20, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.show()
