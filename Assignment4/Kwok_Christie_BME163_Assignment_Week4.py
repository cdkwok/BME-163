#Christie Kwok
#5/3/21
#its a mess, sorry

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import argparse
import math

mFigWidth= 5
mFigHeight = 2
xMin= 0
xMax = 12
yMin = 75
yMax = 100

def genplot(yList, xOff, minDist, bound):
    plotList = [[],[]]
    plotList[0].append(xOff)
    plotList[1].append(yList[0])
    shiftDir = 1
    outOfBounds = False
    i = 1
    #calculate x and y inch conversions
    xToInch = mFigWidth / (xMax - xMin)
    yToInch = mFigHeight / (yMax - yMin)
    while not outOfBounds and i < len(yList) and i <= 1000:
        #if(i%100==0):
        #    print("working on point ", i, "...")
        placed = False
        xVal = xOff
        j = 0
        while not placed:
            #print("1")
            tooClose = False
            while(j<len(plotList[0]) and not tooClose):
                #print("2")
                #print("j=", j)
                #print(tooClose)
                if plotList[1][j]*yToInch < (yList[i]*yToInch)+minDist and plotList[1][j]*yToInch > (yList[i]*yToInch)-minDist:
                    distance = math.sqrt(((plotList[0][j] - xVal)*xToInch)**2 + ((plotList[1][j] - yList[i])*yToInch)**2)
                    #print("3")
                    if (distance < minDist):
                        #print("too close!!!!")
                        tooClose = True
                        closePoint = j
                        j=0
                j+=1
            if tooClose:
                #xDiff = math.sqrt(minDist**2 - ((plotList[1][closePoint] - yList[i])*yToInch)**2)
                #xValNew = plotList[0][closePoint] + (xDiff/xToInch)*shiftDir
                #if abs(xValNew)>abs(xVal):
                #    xVal = xValNew
                #else:
                #    print("does it ever get here")
                xVal +=.0002*shiftDir
            else:
                if abs(xVal-xOff) < bound:
                    plotList[0].append(xVal)
                    plotList[1].append(yList[i])
                    shiftDir*=-1
                else:
                    outOfBounds = True
                placed = True
        i+=1
    return plotList

 

xList = []
yList = []

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file')
parser.add_argument('-s', '--style_sheet', default='BME163')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()
input_file = args.input_file
plt.style.use(args.style_sheet)

pointLists = [[],[],[],[],[],[],[],[],[],[],[]]

inFile = open(args.input_file)
for line in inFile:
    splitLine = line.strip().split('\t')
    identity = float(splitLine[1])
    numberList = splitLine[0].split('_')
    number = int(numberList[3])
    pointLists[min(number-1, 10)].append(identity)
         
figureHeight = 3
figureWidth = 7
plt.figure(figsize = (figureWidth, figureHeight))


mainPanelWidth = mFigWidth
mainPanelHeight = mFigHeight
mainPanel = plt.axes([0.1, 0.2, 5/7, 2/3])

for i in range(11):
    points = genplot(pointLists[i], i+1, 0.75 / 72, .5)
    mainPanel.plot([(i + 1) - mainPanelWidth / 12.5, (i + 1) + mainPanelWidth / 12.5], 
                   [np.median(points[1]), np.median(points[1])], linewidth = 1, color = 'red')
    mainPanel.plot(points[0], points[1], 
                    marker = 'o', 
                    markerfacecolor = 'black',
                    markeredgecolor = 'black',
                    markersize = 0.75, 
                    markeredgewidth = 0, 
                    linewidth = 0)


mainPanel.set_xlabel("Subread Coverage")
mainPanel.set_ylabel("Identity %")
mainPanel.set_xlim(xMin, xMax)

mainPanel.set_ylim(yMin, yMax)
mainPanel.set_yticks(np.arange(yMin, yMax + 1, 5))
mainPanel.set_xticks(np.arange(1, 12, 1))


mainPanel.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '>10'])
mainPanel.set_yticklabels(['75', '80', '85', '90', '95', '100'])
mainPanel.plot([-2, 14], [95, 95], linewidth = 0.5 , dashes = (1, 2, 2, 2), color = 'black')
mainPanel.tick_params(bottom = True, labelbottom = True,
                   left = True, labelleft = True, 
                   right = False, labelright = False,
                   top = False, labeltop = False)


plt.savefig(args.output_file, dpi = 600)
