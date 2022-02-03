#Christie Kwok
#5/17/21
# takes ~20 secs to run
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import matplotlib.image as mpimg
import argparse

figureWidth = 5
figureHeight = 3

plt.figure(figsize = (figureWidth, figureHeight))
 
mainPanelWidth =  0.75
mainPanelHeight = 2.5

leftPanel = plt.axes([0.1,  0.1, mainPanelWidth/figureWidth, mainPanelHeight/figureHeight])


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file')
parser.add_argument('-s', '--style_sheet', default='BME163')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()
input_file = args.input_file
 
plt.style.use('BME163')
inFile = open(args.input_file)
lines = inFile.readlines()[1:]

data = []
update = []
peakPhase = []

R = np.linspace(255 / 255, 56 / 255, 101)
G = np.linspace(225 / 255, 66 / 255, 101)
B = np.linspace(40 / 255, 157 / 255, 101)

for line in lines:
    splitLine = line.strip().split('\t')
    data.append(splitLine)
    peakPhase.append(float(splitLine[13]))

for line in data:
    sliced = line[4:]
    del sliced[-4:]
    update.append(sliced)
    
for i in update:
    for j in range(len(i)):
        i[j] = int(i[j])


for item in range(len(update)):
    update[item].append(peakPhase[item])

update.sort(key = lambda e: e[8], reverse = True)

for row in range(len(update)):
    update[row].pop()

for row in range(len(update)):
    maxValue = max(update[row])
    minValue = min(update[row])
    
    for j in range(len(update[row])):
        ndata = ((update[row][j] - minValue) / (maxValue - minValue)) * 100
        update[row][j] = int(ndata)

for row in range(len(update)):
    for i in range(len(update[row])):
        bow = update[row][i]
        rectangle = mplpatches.Rectangle([i, row], 1, 1,
                               facecolor = (R[bow], G[bow], B[bow]),
                               edgecolor = 'black',
                               linewidth = 0)
        leftPanel.add_patch(rectangle)

    


leftPanel.set_xlabel( "CT")
leftPanel.set_ylabel("Number of genes")
leftPanel.set_xlim(0, 8)
leftPanel.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
leftPanel.set_xticklabels([0, '', 6, '', 12, '', 18, ''])
leftPanel.set_ylim(0, 1262)
leftPanel.set_yticks([0, 200, 400, 600, 800, 1000, 1200])
leftPanel.set_yticklabels([0, 200, 400, 600, 800, 1000, 1200])
leftPanel.tick_params(bottom = True, labelbottom = True,
                   left = True, labelleft = True, 
                   right = False, labelright = False,
                   top = False, labeltop = False)


plt.savefig(args.output_file, dpi = 600)
