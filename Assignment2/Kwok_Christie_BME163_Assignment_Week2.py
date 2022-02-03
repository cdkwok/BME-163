import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file')
parser.add_argument('-s', '--style_sheet', default='BME163')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()
input_file = args.input_file
plt.style.use(args.style_sheet)
 

xList =[]
yList = []

inFile = open(args.input_file)
for line in inFile:
    splitLine = line.strip().split('\t')
    xList.append(np.log2(int(splitLine[1]) + 1))
    yList.append(np.log2(int(splitLine[2]) + 1))
    
    
figureHeight = 2
figureWidth = 5

plt.figure(figsize = (figureWidth, figureHeight))

#size of individual left and right figures 
mainPanelWidth = 1
mainPanelHeight = 1

sidePanelWidth = 0.25
sidePanelHeight = 1

topPanelWidth = 1
topPanelHeight = 0.25

#panels - left
leftPanel = plt.axes([0.14, 0.15, 0.20, 0.50])
leftSidePanel = plt.axes([0.076, 0.15, 0.05, 0.5])
leftTopPanel = plt.axes([0.14, 0.685, 0.20, 0.125])

#left main panel
leftPanel.plot(xList, yList, 
                marker = 'o', 
                markerfacecolor = 'black',
                markeredgecolor = 'black', 
                markersize = 1.45, 
                markeredgewidth = 0, 
                linewidth = 0,
                alpha = 0.1)

xHisto, bins = np.histogram(xList, np.arange(0, 15, 0.5))
yHisto, bins = np.histogram(yList, np.arange(0, 15, 0.5))


# left side panel
for side in range(0, len(yHisto), 1):
    bottom = 0
    left=bins[side]
    width=bins[side + 1] - left
    height=np.log2(yHisto[side] + 1)
    rectangle=mplpatches.Rectangle([bottom, left], height, width,
                               facecolor ='grey',
                               edgecolor ='black',
                               linewidth =0.1)
    leftSidePanel.add_patch(rectangle)

#left top panel
for top in range(0,len(xHisto),1):
    bottom=0
    left=bins[top]
    width=bins[top + 1] - left
    height=np.log2(xHisto[top] + 1)
    rectangle=mplpatches.Rectangle([left, bottom], width, height,
                               facecolor = 'grey',
                               edgecolor = 'black',
                               linewidth = 0.1)
    leftTopPanel.add_patch(rectangle)

leftPanel.set_xlim(0, 15)
leftPanel.set_ylim(0, 15)
leftPanel.tick_params(bottom = True, labelbottom = True,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)

leftSidePanel.set_xlim(20, 0)
leftSidePanel.set_ylim(0, 15)
leftSidePanel.tick_params(bottom = True, labelbottom = True,
                   left = True, labelleft = True, 
                   right = False, labelright = False,
                   top = False, labeltop = False)

leftTopPanel.set_xlim(0, 15)
leftTopPanel.set_ylim(0, 20)
leftTopPanel.tick_params(bottom=False, labelbottom=False,
                   left=True, labelleft=True,
                   right=False, labelright=False,
                   top=False, labeltop=False)


#right Panel stuff

rightPanel= plt.axes([0.54, 0.15, 0.20, 0.50])
rightSidePanel = plt.axes([0.476, 0.15, 0.05, 0.5])
rightTopPanel = plt.axes([0.54, 0.685, 0.20, 0.125])
legend = plt.axes([0.8, 0.15, 0.02, 0.50])


# rightPanel.scatter(xList, yList,
#                  s = 2,
#                  facecolor = 'black',
#                  linewidth = 0)

rightPanel.set_xlim(0, 15)
rightPanel.set_ylim(0, 15)
rightPanel.tick_params(bottom = True, labelbottom = True,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)

rightSidePanel.set_xlim(20, 0)
rightSidePanel.set_ylim(0, 15)
rightSidePanel.tick_params(bottom = True, labelbottom = True,
                   left = True, labelleft = True, 
                   right = False, labelright = False,
                   top = False, labeltop = False)

rightTopPanel.set_xlim(0, 15)
rightTopPanel.set_ylim(0, 20)
rightTopPanel.tick_params(bottom=False, labelbottom=False,
                   left=True, labelleft=True,
                   right=False, labelright=False,
                   top=False, labeltop=False)

legend.set_xlim(0, 1)
legend.set_ylim(0,20)
legend.set_yticks(np.arange(0, 21, 20))
legend.tick_params(bottom=False, labelbottom=False,
                   left=True, labelleft=True,
                   right=False, labelright=False,
                   top=False, labeltop=False)



plt.savefig(args.output_file, dpi = 600)