import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
file = open('C:/users/andrew/desktop/input.txt')
filelines = file.readlines()
inputmatrix = []
for line in filelines:
    temp = []
    for char in line:
        if char != '\n':
            temp.append(int(char))
    inputmatrix.append(temp)
ax = plt.subplot()
cmap = colors.ListedColormap(['red', 'blue'])
ax.imshow(inputmatrix, cmap=cmap)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 20, 1))
ax.set_yticks(np.arange(-.5, 20, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.show()
