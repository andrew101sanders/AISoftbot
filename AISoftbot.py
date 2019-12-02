import math
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

file = open('input.txt')
filelines = file.readlines()
file.close()
original = []
inputmatrix = []  # [Y][X] - [Rows][Columns] required for matplot (and yes this makes it very confusing to program lol)
outputList = []
fulloutputlist = []
bestpathvisual = []
FilledGaps = []
S = []  # Original seeds from first two rows in format [x,y]
G = []  # exploring seeds
Marked = []  # Seeds that have already been explored
StartOfPath = []
EndOfPath = [0, 0]  # [X, Y]
visited = []
fullvisited = []  # Normally, the trail finding stops once it reaches the end. This list is for finding the entire trail


def addtolist(node):  # param: [X, Y]
    if node not in G and node not in Marked:
        print("Adding " + str(node) + " to G")
        G.append(node)


# check potential error node
def checkpotential(node, checkNW, checkN, checkNE, checkE, checkSE, checkS, checkSW, checkW):
    #  print(node)
    left = node[0] - 1 >= 0
    top = node[1] - 1 >= 0
    right = node[0] + 1 <= 19
    bottom = node[1] + 1 <= 19

    # If not on top row
    if top:
        # if not on far left column and not on top row
        if left:
            # check NW
            if checkNW:
                if inputmatrix[node[1] - 1][node[0] - 1] == 0 and [node[0] - 1, node[1] - 1] not in FilledGaps:
                    if inputmatrix[node[1] - 1][node[0] - 1] not in Marked:
                        # print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        FilledGaps.append(node)
                        addtolist(node)
                        return

        # check N 
        if checkN:
            if inputmatrix[node[1] - 1][node[0]] == 0 and [node[0], node[1] - 1] not in FilledGaps:
                if inputmatrix[node[1] - 1][node[0]] not in Marked:
                    # print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    FilledGaps.append(node)
                    addtolist(node)
                    return

        # if not on far right column and not on top row
        if right:
            # check NE
            if checkNE:
                if inputmatrix[node[1] - 1][node[0] + 1] == 0 and [node[0] + 1, node[1] - 1] not in FilledGaps:
                    if inputmatrix[node[1] - 1][node[0] + 1] not in Marked:
                        # print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        FilledGaps.append(node)
                        addtolist(node)
                        return

    # if not on far right
    if right:
        # check E
        if checkE:
            if inputmatrix[node[1]][node[0] + 1] == 0 and [node[0] + 1, node[1]] not in FilledGaps:
                if inputmatrix[node[1]][node[0] + 1] not in Marked:
                    # print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    FilledGaps.append(node)
                    addtolist(node)
                    return

    # if not on bottom row
    if bottom:
        # if not on bottom row and not on far right column
        if right:
            # Check SE
            if checkSE:
                if inputmatrix[node[1] + 1][node[0] + 1] == 0 and [node[0] + 1, node[1] + 1] not in FilledGaps:
                    if inputmatrix[node[1] + 1][node[0] + 1] not in Marked:
                        # print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        FilledGaps.append(node)
                        addtolist(node)
                        return

        # check S
        if checkS:
            if inputmatrix[node[1] + 1][node[0]] == 0 and [node[0], node[1] + 1] not in FilledGaps:
                if inputmatrix[node[1] + 1][node[0]] not in Marked:
                    # print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    FilledGaps.append(node)
                    addtolist(node)
                    return

        # if not on bottom row and not on far left column
        if left:
            # check SW
            if checkSW:
                if inputmatrix[node[1] + 1][node[0] - 1] == 0 and [node[0] - 1, node[1] + 1] not in FilledGaps:
                    if inputmatrix[node[1] + 1][node[0] - 1] not in Marked:
                        # print('changing ' + str([node[0], node[1]]) + ' to 0')
                        inputmatrix[node[1]][node[0]] = 0
                        FilledGaps.append(node)
                        addtolist(node)
                        return

    # if not on far left 
    if left:
        # check W
        if checkW:
            if inputmatrix[node[1]][node[0] - 1] == 0 and [node[0] - 1, node[1]] not in FilledGaps:
                if inputmatrix[node[1]][node[0] - 1] not in Marked:
                    # print('changing ' + str([node[0], node[1]]) + ' to 0')
                    inputmatrix[node[1]][node[0]] = 0
                    FilledGaps.append(node)
                    addtolist(node)
                    return


def checksurrounding(node):  # param: [X, Y]
    left = node[0] - 1 >= 0
    top = node[1] - 1 >= 0
    right = node[0] + 1 <= 19
    bottom = node[1] + 1 <= 19

    # If not on top row
    if top:
        # if not on far left column and not on top row
        if left:
            # check NW           
            if inputmatrix[node[1] - 1][node[0] - 1] == 1 and node not in FilledGaps:
                checkpotential([node[0] - 1, node[1] - 1], True, False, False, False, False, False, False, False)
            if inputmatrix[node[1] - 1][node[0] - 1] == 0 and [node[0] - 1, node[1] - 1] not in FilledGaps:
                addtolist([node[0] - 1, node[1] - 1])

        # check N 
        if inputmatrix[node[1] - 1][node[0]] == 1 and node not in FilledGaps:
            checkpotential([node[0], node[1] - 1], False, True, False, False, False, False, False, False)
        if inputmatrix[node[1] - 1][node[0]] == 0 and [node[0], node[1] - 1] not in FilledGaps:
            addtolist([node[0], node[1] - 1])

        # if not on far right column and not on top row
        if right:
            # check NE
            if inputmatrix[node[1] - 1][node[0] + 1] == 1 and node not in FilledGaps:
                checkpotential([node[0] + 1, node[1] - 1], False, False, True, False, False, False, False, False)
            if inputmatrix[node[1] - 1][node[0] + 1] == 0 and [node[0] + 1, node[1] - 1] not in FilledGaps:
                addtolist([node[0] + 1, node[1] - 1])

    # if not on far right
    if right:
        # check E
        if inputmatrix[node[1]][node[0] + 1] == 1 and node not in FilledGaps:
            checkpotential([node[0] + 1, node[1]], False, False, False, True, False, False, False, False)
        if inputmatrix[node[1]][node[0] + 1] == 0 and [node[0] + 1, node[1]] not in FilledGaps:
            addtolist([node[0] + 1, node[1]])

    # if not on bottom row
    if bottom:
        # if not on bottom row and not on far right column
        if right:
            # Check SE
            if inputmatrix[node[1] + 1][node[0] + 1] == 1 and node not in FilledGaps:
                checkpotential([node[0] + 1, node[1] + 1], False, False, False, False, True, False, False, False)
            if inputmatrix[node[1] + 1][node[0] + 1] == 0 and [node[0] + 1, node[1] + 1] not in FilledGaps:
                addtolist([node[0] + 1, node[1] + 1])

        # check S
        if inputmatrix[node[1] + 1][node[0]] == 1 and node not in FilledGaps:
            checkpotential([node[0], node[1] + 1], False, False, False, False, False, True, False, False)
        if inputmatrix[node[1] + 1][node[0]] == 0 and [node[0], node[1] + 1] not in FilledGaps:
            addtolist([node[0], node[1] + 1])

        # if not on bottom row and not on far left column
        if left:
            # check SW
            if inputmatrix[node[1] + 1][node[0] - 1] == 1 and node not in FilledGaps:
                checkpotential([node[0] - 1, node[1] + 1], False, False, False, False, False, False, True, False)
            if inputmatrix[node[1] + 1][node[0] - 1] == 0 and [node[0] - 1, node[1] + 1] not in FilledGaps:
                addtolist([node[0] - 1, node[1] + 1])

    # if not on far left 
    if left:
        # check W
        if inputmatrix[node[1]][node[0] - 1] == 1 and node not in FilledGaps:
            checkpotential([node[0] - 1, node[1]], False, False, False, False, False, False, False, True)
        if inputmatrix[node[1]][node[0] - 1] == 0 and [node[0] - 1, node[1]] not in FilledGaps:
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


for n in inputmatrix:
    temp = []
    for x in n:
        temp.append(x)
    fulloutputlist.append(temp)

# populate S with first row of inputmatrix
for index, firstrowitem in enumerate(inputmatrix[0]):
    if inputmatrix[0][index] == 0:
        S.append([index, 0])

# populate S with second row of inputmatrix
for index, secondrowitem in enumerate(inputmatrix[1]):
    if inputmatrix[1][index] == 0:
        S.append([index, 1])


def checkSeeds(seed):
    global StartOfPath
    global EndOfPath
    foundtrail = False
    if seed not in Marked:
        Marked.append(seed)
        visited.append(seed)
        checksurrounding(seed)
        while G:
            popped = G.pop(0)
            print(popped)
            if popped[1] > EndOfPath[1]:
                EndOfPath = popped
            if not foundtrail:
                if popped[1] == 19:
                    if seed[1] - 1 >= 0:
                        StartOfPath = [seed[0], seed[1]]
                        if inputmatrix[seed[1] - 1][seed[0]] == 1:
                            inputmatrix[seed[1] - 1][seed[0]] = 0
                            visited.append([seed[0], seed[1] - 1])
                            FilledGaps.append([seed[0], seed[1] - 1])
                            StartOfPath = [seed[0], seed[1] - 1]
                    visited.append(popped)
                    foundtrail = True
                    for n in visited:
                        temp = []
                        for x in n:
                            temp.append(x)
                        fullvisited.append(temp)
                visited.append(popped)
            else:
                fullvisited.append(popped)
            if popped not in Marked:
                Marked.append(popped)
                # print('checking ' + str(popped))
                checksurrounding(popped)
    if foundtrail: return 1
    return 0


# Go through seeds in S and try to find path
for initialseed in S:
    G = []
    visited = []
    if checkSeeds(initialseed) == 0:
        continue
    else:
        break


def reconstruct(camefrom, current):
    c = current[0]
    totalpath = []
    while c != StartOfPath:
        i = 0
        while i < camefrom.__len__():
            if camefrom[i][0] == c:
                newc = camefrom[i][1]
                totalpath.append(c)
                camefrom.remove(camefrom[i])
                c = newc
                break
            i += 1
    totalpath.append(StartOfPath)
    return totalpath


def distance(a, b):
    return math.sqrt((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2)


def getneighbors(nodeToCheck):
    global visited
    templist = []
    left = nodeToCheck[0] - 1 >= 0
    top = nodeToCheck[1] - 1 >= 0
    right = nodeToCheck[0] + 1 <= 19
    bottom = nodeToCheck[1] + 1 <= 19
    if top and left:
        if [nodeToCheck[0] - 1, nodeToCheck[1] - 1] in visited:
            templist.append([nodeToCheck[0] - 1, nodeToCheck[1] - 1])
    if top:
        if [nodeToCheck[0], nodeToCheck[1] - 1] in visited:
            templist.append([nodeToCheck[0], nodeToCheck[1] - 1])
    if top and right:
        if [nodeToCheck[0] + 1, nodeToCheck[1] - 1] in visited:
            templist.append([nodeToCheck[0] + 1, nodeToCheck[1] - 1])
    if right:
        if [nodeToCheck[0] + 1, nodeToCheck[1]] in visited:
            templist.append([nodeToCheck[0] + 1, nodeToCheck[1]])
    if right and bottom:
        if [nodeToCheck[0] + 1, nodeToCheck[1] + 1] in visited:
            templist.append([nodeToCheck[0] + 1, nodeToCheck[1] + 1])
    if bottom:
        if [nodeToCheck[0], nodeToCheck[1] + 1] in visited:
            templist.append([nodeToCheck[0], nodeToCheck[1] + 1])
    if bottom and left:
        if [nodeToCheck[0] - 1, nodeToCheck[1] + 1] in visited:
            templist.append([nodeToCheck[0] - 1, nodeToCheck[1] + 1])
    if left:
        if [nodeToCheck[0] - 1, nodeToCheck[1]] in visited:
            templist.append([nodeToCheck[0] - 1, nodeToCheck[1]])

    return templist


def astar():
    global StartOfPath
    global EndOfPath
    openset = [StartOfPath]
    camefrom = []
    gscore = []
    fscore = []
    for q in visited:
        gscore.append([q, 99999])
        fscore.append([q, 99999])

    next(z for z in gscore if z[0] == StartOfPath)[1] = 0
    next(z for z in fscore if z[0] == StartOfPath)[1] = distance(StartOfPath, EndOfPath)
    while openset:
        # get lowest fscore
        current = [StartOfPath, 99999]
        for temporary in openset:
            tempos = current
            for temp in fscore:
                if temporary == temp[0]:
                    tempos = temp
            if tempos[1] < current[1]:
                current = tempos

        if current[0] == EndOfPath:
            return reconstruct(camefrom, current)
        for temp in openset:
            if temp == current[0]:
                openset.remove(temp)
        neighbors = getneighbors(current[0])
        for neigh in neighbors:
            tempg = None
            for temp in gscore:
                if neigh == temp[0]:
                    tempg = temp
            tempf = None
            for temp in fscore:
                if neigh == temp[0]:
                    tempf = temp
            tentative_gscore = current[1] + distance(neigh, current[0])

            if tentative_gscore < tempg[1]:
                tempc = None
                for temp in camefrom:
                    if neigh == temp[0]:
                        tempc = temp
                if tempc is None:
                    camefrom.append([neigh, current[0]])
                else:
                    tempc[1] = current[0]
                tempg[1] = tentative_gscore
                tempf[1] = tempg[1] + distance(neigh, EndOfPath)
                if neigh not in openset:
                    openset.append(neigh)


bestpath = astar()

for v in visited:
    outputList[v[1]][v[0]] = 2

for k in fullvisited:
    fulloutputlist[k[1]][k[0]] = 2

# This is for visualizing the best path - found using A*
for n in inputmatrix:
    temp = []
    for x in n:
        temp.append(x)
    bestpathvisual.append(temp)
for b in bestpath:
    bestpathvisual[b[1]][b[0]] = 2

# printing to file
output = open('correctedImage.txt', 'w')
for y in inputmatrix:
    for x in y:
        output.write(str(x))
    output.write('\n')
output.close()

# print(FilledGaps)
print("visited nodes: ")
print(visited)
print("Marked nodes: ")
print(Marked)
plt.figure('AI Assignment 3', figsize=(8, 8))
ax = plt.subplot(234)
cmap = colors.ListedColormap(['red', 'blue', 'yellow'])
ax.imshow(outputList, cmap)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 20, 1))
ax.set_yticks(np.arange(-.5, 20, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_title('Hiking Trail')

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

ax4 = plt.subplot(236)
ax4.imshow(bestpathvisual, cmap)
ax4.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax4.set_xticks(np.arange(-.5, 20, 1))
ax4.set_yticks(np.arange(-.5, 20, 1))
ax4.set_yticklabels([])
ax4.set_xticklabels([])
ax4.set_title('A* Shortest Path')

ax5 = plt.subplot(235)
ax5.imshow(fulloutputlist, cmap)
ax5.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax5.set_xticks(np.arange(-.5, 20, 1))
ax5.set_yticks(np.arange(-.5, 20, 1))
ax5.set_yticklabels([])
ax5.set_xticklabels([])
ax5.set_title('Entire Hiking Trail')
plt.show()
