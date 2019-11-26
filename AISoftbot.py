import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

file = open('input.txt')
filelines = file.readlines()
file.close()
original = []
inputmatrix = []  # [Y][X] - [Rows][Columns] required for matplot (and yes this makes it very confusing to program lol)
outputList = []
S = []  # Original seeds from first two rows in format [x,y]
G = []  # exploring seeds
Temp = []  # potential nodes
Marked = []  # Seeds that have already been explored
Lowest = [0, 0]  # [X, Y]
visited = []


def addtolist(node):  # param: [X, Y]
    if node not in G and node not in Marked:
        G.append(node)


def addtotemp(node):
    if node not in temp and node not in Marked:
        Temp.append(node)


# check potential error node
def checkpotential(node, checkNW, checkN, checkNE, checkE, checkSE, checkS, checkSW, checkW):
    #  addtotemp(node)
    #  print(node)
    left = node[0] - 1 >= 0
    top = node[1] - 1 >= 0
    right = node[0] + 1 <= 19
    bottom = node[1] + 1 <= 19

    # TODO if point = 1, run it through another function that
    #  checks the 3 points that are away from initial node. eg node[
    #  3, 3] checks [4, 3] and it's a 1, it would check [4, 2], [5, 2], [5, 3]

    # If not on top row
    if top:
        # if not on far left column and not on top row
        if left:
            # check NW
            if checkNW:
                if inputmatrix[node[1] - 1][node[0] - 1] == 0:
                    if inputmatrix[node[1] - 1][node[0] - 1] not in Marked:
                        print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        addtotemp(node)
                        addtolist(node)
                        # addtolist([node[1]-1, node[0]-1])
                        # Marked.append(node)
                        # visited.append([node[0], node[1]])
                        return

        # check N 
        if checkN:
            if inputmatrix[node[1] - 1][node[0]] == 0:
                if inputmatrix[node[1] - 1][node[0]] not in Marked:
                    print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    addtotemp(node)
                    addtolist(node)
                    # addtolist([node[1]-1, node[0]])
                    # Marked.append(node)
                    # visited.append([node[0], node[1]])
                    return

        # if not on far right column and not on top row
        if right:
            # check NE
            if checkNE:
                if inputmatrix[node[1] - 1][node[0] + 1] == 0:
                    if inputmatrix[node[1] - 1][node[0] + 1] not in Marked:
                        print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        addtotemp(node)
                        addtolist(node)
                        # addtolist([node[1]-1, node[0]+1])
                        # Marked.append(node)
                        # visited.append([node[0], node[1]])
                        return

    # if not on far right
    if right:
        # check E
        if checkE:
            if inputmatrix[node[1]][node[0] + 1] == 0:
                if inputmatrix[node[1]][node[0] + 1] not in Marked:
                    print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    addtotemp(node)
                    addtolist(node)
                    # addtolist([node[1], node[0]+1])
                    # Marked.append(node)
                    # visited.append([node[0], node[1]])
                    return

    # if not on bottom row
    if bottom:
        # if not on bottom row and not on far right column
        if right:
            # Check SE
            if checkSE:
                if inputmatrix[node[1] + 1][node[0] + 1] == 0:
                    if inputmatrix[node[1] + 1][node[0] + 1] not in Marked:
                        print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        addtotemp(node)
                        addtolist(node)
                        # addtolist([node[1]+1, node[0]+1])
                        # Marked.append(node)
                        # visited.append([node[0], node[1]])
                        return

        # check S
        if checkS:
            if inputmatrix[node[1] + 1][node[0]] == 0:
                if inputmatrix[node[1] + 1][node[0]] not in Marked:
                    print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    addtotemp(node)
                    addtolist(node)
                    # addtolist([node[1]+1, node[0]])
                    # Marked.append(node)
                    # visited.append([node[0], node[1]])
                    return

        # if not on bottom row and not on far left column
        if left:
            # check SW
            if checkSW:
                if inputmatrix[node[1] + 1][node[0] - 1] == 0:
                    if inputmatrix[node[1] + 1][node[0] - 1] not in Marked:
                        print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        addtotemp(node)
                        addtolist(node)
                        # addtolist([node[1]+1, node[0]-1])
                        # Marked.append(node)
                        # visited.append([node[0], node[1]])
                        return

    # if not on far left 
    if left:
        # check W
        if checkW:
            if inputmatrix[node[1]][node[0] - 1] == 0:
                if inputmatrix[node[1]][node[0] - 1] not in Marked:
                    print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    addtotemp(node)
                    addtolist(node)
                    # addtolist([node[1], node[0]-1])
                    # Marked.append(node)
                    # visited.append([node[0], node[1]])
                    return


def checksurrounding(node):  # param: [X, Y]
    addtolist(node)
    # print(node)
    left = node[0] - 1 >= 0
    top = node[1] - 1 >= 0
    right = node[0] + 1 <= 19
    bottom = node[1] + 1 <= 19

    # TODO if point = 1, run it through another function that
    #  checks the 3 points that are away from initial node. eg node[
    #  3, 3] checks [4, 3] and it's a 1, it would check [4, 2], [5, 2], [5, 3]

    # If not on top row
    if top:
        # if not on far left column and not on top row
        if left:
            # check NW           
            if inputmatrix[node[1] - 1][node[0] - 1] == 1:
                checkpotential([node[0] - 1, node[1] - 1], True, False, False, False, False, False, False, False)
            if inputmatrix[node[1] - 1][node[0] - 1] == 0:
                addtolist([node[0] - 1, node[1] - 1])

        # check N 
        if inputmatrix[node[1] - 1][node[0]] == 1:
            checkpotential([node[0], node[1] - 1], False, True, False, False, False, False, False, False)
        if inputmatrix[node[1] - 1][node[0]] == 0:
            addtolist([node[0], node[1] - 1])

        # if not on far right column and not on top row
        if right:
            # check NE

            if inputmatrix[node[1] - 1][node[0] + 1] == 1:
                checkpotential([node[0] + 1, node[1] - 1], False, False, True, False, False, False, False, False)
            if inputmatrix[node[1] - 1][node[0] + 1] == 0:
                addtolist([node[0] + 1, node[1] - 1])

    # if not on far right
    if right:
        # check E

        if inputmatrix[node[1]][node[0] + 1] == 1:
            checkpotential([node[0] + 1, node[1]], False, False, False, True, False, False, False, False)
        if inputmatrix[node[1]][node[0] + 1] == 0:
            addtolist([node[0] + 1, node[1]])

    # if not on bottom row
    if bottom:
        # if not on bottom row and not on far right column
        if right:
            # Check SE
            if inputmatrix[node[1] + 1][node[0] + 1] == 1:
                checkpotential([node[0] + 1, node[1] + 1], False, False, False, False, True, False, False, False)
            if inputmatrix[node[1] + 1][node[0] + 1] == 0:
                addtolist([node[0] + 1, node[1] + 1])

        # check S
        if inputmatrix[node[1] + 1][node[0]] == 1:
            checkpotential([node[0], node[1] + 1], False, False, False, False, False, True, False, False)
        if inputmatrix[node[1] + 1][node[0]] == 0:
            addtolist([node[0], node[1] + 1])

        # if not on bottom row and not on far left column
        if left:
            # check SW
            if inputmatrix[node[1] + 1][node[0] - 1] == 1:
                checkpotential([node[0] - 1, node[1] + 1], False, False, False, False, False, False, True, False)
            if inputmatrix[node[1] + 1][node[0] - 1] == 0:
                addtolist([node[0] - 1, node[1] + 1])

    # if not on far left 
    if left:
        # check W
        if inputmatrix[node[1]][node[0] - 1] == 1:
            checkpotential([node[0] - 1, node[1]], False, False, False, False, False, False, False, True)
        if inputmatrix[node[1]][node[0] - 1] == 0:
            addtolist([node[0] - 1, node[1]])


# populate inputmatrix
for y in filelines:
    temp = []
    for x in y:
        if x != '\n':
            temp.append(int(x))
    inputmatrix.append(temp)


# copy over to value, not reference (because it is being altered), to outputlist
for n in inputmatrix:
    temp = []
    for x in n:
        temp.append(x)
    outputList.append(temp)

# copy over to value, not reference (because it is being altered), to original.
# This is for the final output to compare the altered path to the original
for n in inputmatrix:
    temp = []
    for x in n:
        temp.append(x)
    original.append(temp)

# populate S with first row of inputmatrix
for index, firstrowitem in enumerate(inputmatrix[0]):
    if inputmatrix[0][index] == 0:
        S.append([index, 0])

# populate S with second row of inputmatrix
for index, secondrowitem in enumerate(inputmatrix[1]):
    if inputmatrix[1][index] == 0:
        S.append([index, 1])


def checkSeeds(seed):
    global Lowest
    if seed not in Marked:
        Marked.append(seed)
        visited.append(seed)
        checksurrounding(seed)
        while G.__len__() != 0:
            temp = G.pop()
            if temp[1] > Lowest[1]:
                Lowest = temp
            if temp[1] == 19:
                if seed[1] - 1 >= 0:
                    if inputmatrix[seed[1] - 1][seed[0]] == 1:
                        inputmatrix[seed[1] - 1][seed[0]] = 0
                        visited.append([seed[0],seed[1]-1])
                visited.append(temp)
                return 1
            visited.append(temp)
            if temp not in Marked:
                Marked.append(temp)
                print('checking ' + str(temp))
                checksurrounding(temp)
    return 0


# Go through seeds in S and try to find path
# TODO break if it finds a path to the bottom
# TODO keep track of 'highest' and if path is found and highest Y = 1, change the pixel above it to 0
for initialseed in S:
    G = []
    visited = []
    if checkSeeds(initialseed) == 0:
        continue
    else:
        break

for v in visited:
    outputList[v[1]][v[0]] = 2
# TODO implement another color
output = open('correctedImage.txt', 'w')
for y in inputmatrix:
    for x in y:
        output.write(str(x))
    output.write('\n')
output.close()
ax = plt.subplot(212)
cmap = colors.ListedColormap(['red', 'blue', 'yellow'])
ax.imshow(outputList, cmap)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 20, 1))
ax.set_yticks(np.arange(-.5, 20, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_title('Path')
ax2 = plt.subplot(222)
cmap2 = colors.ListedColormap(['red', 'blue'])
ax2.imshow(inputmatrix, cmap2)
ax2.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax2.set_xticks(np.arange(-.5, 20, 1))
ax2.set_yticks(np.arange(-.5, 20, 1))
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.set_title('Fixed Image')
ax3 = plt.subplot(221)
ax3.imshow(original, cmap2)
ax3.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax3.set_xticks(np.arange(-.5, 20, 1))
ax3.set_yticks(np.arange(-.5, 20, 1))
ax3.set_yticklabels([])
ax3.set_xticklabels([])
ax3.set_title('Original Image')
plt.show()
