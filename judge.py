import numpy as np
import re
import math

name = input("name of the file : ")
with open(f"{name}.xyz", "r") as f:
    txt = f.readlines()

atoms = []
for i in range(2, len(txt)):
    txt[i] = re.split(r"\s+", txt[i])
    atoms.append(txt[i][0])

atomsSet = list(set(atoms))

cats = [[] for i in range(len(atomsSet))]
alls = [[] for i in range(3)]

def fl(val, order):
    if val > 0:
        return math.floor(val*(10**order)) / (10**order)
    else:
        return math.ceil(val*(10**order)) / (10**order)

def minus(mat):
    mat1 = [[0 for j in range(len(mat[i]))] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat1[i][j] = -mat[i][j]

    return mat1

for i in range(2, len(txt)):
    n = atomsSet.index(txt[i][0])
    cats[n].append([fl(float(txt[i][1]), 5), fl(float(txt[i][2]),5), fl(float(txt[i][3].replace("\n", "")), 5)])
    alls[0].append(fl(float(txt[i][1]), 5))
    alls[1].append(fl(float(txt[i][2]), 5))
    alls[2].append(fl(float(txt[i][3]), 5))

#print(cats[0])

x = fl((max(alls[0]) + min(alls[0]))/2, 5)
y = fl((max(alls[1]) + min(alls[1]))/2, 5)
z = fl((max(alls[2]) + min(alls[2]))/2, 5)
means = [x, y, z]

for i in range(len(cats)):
    for j in range(len(cats[i])):
        for k in range(3):
            cats[i][j][k] = fl(cats[i][j][k] - means[k], 2)
#print(cats[0])

cnt = 0
org = 0
for i in range(len(atomsSet)):
    l = minus(cats[i])
    #print(l)
    for j in range(len(cats[i])):
        if cats[i][j] in l:
            cnt += 1
    
    org += len(cats[i])

print(cnt, org)

#print([1.01, 1.01, -1.01] in [[1.01, 1.01, 1.01], [-1.01, -1.01, 1.01]])s