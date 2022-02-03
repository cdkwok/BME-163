#Christie Kwok
#5/10/21

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import matplotlib.image as mpimg
import argparse


fiveList = []
threeList = []
fileList = []

aFiveList = []
tFiveList = []
gFiveList = []
cFiveList = []

aThreeList = []
tThreeList = []
gThreeList = []
cThreeList = []

hFiveList = []
hThreeList = []


A = 0
T = 1
C = 2
G = 3

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file')
parser.add_argument('-s', '--style_sheet', default='BME163')
parser.add_argument('-o', '--output_file')
parser.add_argument('-p', '--pngs')


args = parser.parse_args()
pngList = [
 mpimg.imread(args.pngs + '/A_small.png'),
 mpimg.imread(args.pngs + '/T_small.png'),
 mpimg.imread(args.pngs + '/C_small.png'),
 mpimg.imread(args.pngs + '/G_small.png')]

input_file = args.input_file
plt.style.use(args.style_sheet)

inFile = open(args.input_file)
for line in inFile:
    splitLine = line.strip().split('_')
    fileList.append(splitLine[0])

#shenanigans
for i in range(len(fileList) // 2):
    if fileList[2 * i] == ">5'":
        fiveList.append(fileList[2 * i + 1])
    elif fileList[2 * i] == ">3'":
        threeList.append(fileList[2 * i + 1])
    else:
        print("error")
   

    
figureWidth = 6
figureHeight = 3

plt.figure(figsize = (figureWidth, figureHeight))

#size of individual left and right figures 
mainPanelWidth = 2.4
mainPanelHeight = 1


#panels
leftPanel = plt.axes([0.5/6,  0.3, mainPanelWidth/figureWidth, 1/3])
rightPanel = plt.axes([3.4/6, 0.3, mainPanelWidth/figureWidth, 1/3])

for i in range(len(fiveList[0])): 
    aFiveList.append(0)
    tFiveList.append(0)
    gFiveList.append(0)
    cFiveList.append(0)
    hFiveList.append(0)
    aThreeList.append(0)
    tThreeList.append(0)
    gThreeList.append(0)
    cThreeList.append(0)
    hThreeList.append(0)
    
for sequence in fiveList:
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            aFiveList[i] += 1
        elif sequence[i] == 'T':
            tFiveList[i] += 1
        elif sequence[i] == 'G':
            gFiveList[i] += 1
        elif sequence[i] == 'C':
            cFiveList[i] += 1

for sequence in threeList:
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            aThreeList[i] += 1
        elif sequence[i] == 'T':
            tThreeList[i] += 1
        elif sequence[i] == 'G':
            gThreeList[i] += 1
        elif sequence[i] == 'C':
            cThreeList[i] += 1

            


for i in range(len(aFiveList)):
    aFiveList[i] = aFiveList[i] / len(fiveList)
    tFiveList[i] = tFiveList[i] / len(fiveList)
    gFiveList[i] = gFiveList[i] / len(fiveList)
    cFiveList[i] = cFiveList[i] / len(fiveList)
    
    aThreeList[i] = aThreeList[i] / len(threeList)
    tThreeList[i] = tThreeList[i] / len(threeList)
    gThreeList[i] = gThreeList[i] / len(threeList)
    cThreeList[i] = cThreeList[i] / len(threeList)
    
    hFiveList[i] += aFiveList[i] * np.log2(aFiveList[i])
    hFiveList[i] += tFiveList[i] * np.log2(tFiveList[i])
    hFiveList[i] += cFiveList[i] * np.log2(cFiveList[i])
    hFiveList[i] += gFiveList[i] * np.log2(gFiveList[i])
    
    hThreeList[i] += aThreeList[i] * np.log2(aThreeList[i])
    hThreeList[i] += tThreeList[i] * np.log2(tThreeList[i])
    hThreeList[i] += cThreeList[i] * np.log2(cThreeList[i])
    hThreeList[i] += gThreeList[i] * np.log2(gThreeList[i])
    
    aFiveList[i] = aFiveList[i] * (np.log2(4) - (abs(hFiveList[i]) + (1 / np.log(2)) * (3 / (2 * len(fiveList)))))
    tFiveList[i] = tFiveList[i] * (np.log2(4) - (abs(hFiveList[i]) + (1 / np.log(2)) * (3 / (2 * len(fiveList)))))
    gFiveList[i] = gFiveList[i] * (np.log2(4) - (abs(hFiveList[i]) + (1 / np.log(2)) * (3 / (2 * len(fiveList)))))
    cFiveList[i] = cFiveList[i] * (np.log2(4) - (abs(hFiveList[i]) + (1 / np.log(2)) * (3 / (2 * len(fiveList)))))
    
    aThreeList[i] = aThreeList[i] * (np.log2(4) - (abs(hThreeList[i]) + (1 / np.log(2)) * (3 / (2 * len(threeList)))))
    tThreeList[i] = tThreeList[i] * (np.log2(4) - (abs(hThreeList[i]) + (1 / np.log(2)) * (3 / (2 * len(threeList)))))
    gThreeList[i] = gThreeList[i] * (np.log2(4) - (abs(hThreeList[i]) + (1 / np.log(2)) * (3 / (2 * len(threeList)))))
    cThreeList[i] = cThreeList[i] * (np.log2(4) - (abs(hThreeList[i]) + (1 / np.log(2)) * (3 / (2 * len(threeList)))))
    
    aFiveList[i] = (aFiveList[i], A)
    tFiveList[i] = (tFiveList[i], T)
    cFiveList[i] = (cFiveList[i], C)
    gFiveList[i] = (gFiveList[i], G)
    
    aThreeList[i] = (aThreeList[i], A)
    tThreeList[i] = (tThreeList[i], T)
    cThreeList[i] = (cThreeList[i], C)
    gThreeList[i] = (gThreeList[i], G)

    
fiveBigList = [list(x) for x  in zip(aFiveList, tFiveList, gFiveList, cFiveList)] 
threeBigList = [list(x) for x  in zip(aThreeList, tThreeList, gThreeList, cThreeList)] 

for i in range(len(fiveBigList)):
    fiveBigList[i].sort(key=lambda tup: tup[0]) 

for i in range(len(threeBigList)):
    threeBigList[i].sort(key=lambda tup: tup[0]) 


for x in np.arange(-10, 10):
    prevHeight = 0
    for base in ((fiveBigList[x + 10])):
        leftPanel.imshow(pngList[base[1]], aspect = 'auto', extent = [x , x + 1, prevHeight, prevHeight + base[0]])
        
        prevHeight += base[0]
        
for x in np.arange(-10, 10):
    prevHeight = 0
    for base in ((threeBigList[x + 10])):
        rightPanel.imshow(pngList[base[1]], aspect = 'auto', extent = [x , x + 1, prevHeight, prevHeight + base[0]])
        
        prevHeight += base[0]
        
   
leftPanel.axvline(0, color = 'black', linewidth = '0.5')
leftPanel.set_title("5'SS")
leftPanel.set_xlabel( "Distance to\nSplice Site")
leftPanel.set_ylabel("Bits")
leftPanel.set_xlim(-10, 10)
leftPanel.set_ylim(0, 2)
leftPanel.tick_params(bottom = True, labelbottom = True,
                   left = True, labelleft = True, 
                   right = False, labelright = False,
                   top = False, labeltop = False)
rightPanel.axvline(0, color = 'black', linewidth = '0.5')
rightPanel.set_title("3'SS")
rightPanel.set_xlabel( "Distance to\nSplice Site")
rightPanel.set_xlim(-10, 10)
rightPanel.set_ylim(0, 2)
rightPanel.tick_params(bottom = True, labelbottom = True,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)






plt.savefig(args.output_file, dpi = 600)