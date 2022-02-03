#Christie Kwok (cdkwok)
#4/9/21

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import argparse


#command lind arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file')
parser.add_argument('-s', '--style_sheet', default='BME163')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()
input_file = args.input_file
plt.style.use(args.style_sheet)


figureHeight = 2
figureWidth = 3.42

plt.figure(figsize = (figureWidth, figureHeight))

#size of individual left and right graphs
panelWidth = 1
panelHeight = 1

relativePanelWidth = panelWidth / figureWidth
relativePanelHeight = panelHeight / figureHeight

panel1 = plt.axes([0.1, 0.2, relativePanelWidth, relativePanelHeight])
panel2 = plt.axes([0.55, 0.2, relativePanelWidth, relativePanelHeight])


#panel 1 - left
xList = np.linspace(0, np.pi / 2,  25) 
#to get circles - 25 circles in panel

for value in xList:
    xvalue = np.cos(value) #x axis 
    yvalue = np.sin(value) #y axis
    panel1.plot(xvalue, yvalue, 
                marker = 'o', 
                markerfacecolor = (xvalue, xvalue, xvalue),
                markeredgecolor = 'black', 
                markersize = 2, 
                markeredgewidth = 0, 
                linewidth = 0 )

# panel1.set_xlim(0, 1)
# panel1.set_ylim(0, 1)
panel1.tick_params(bottom = False, labelbottom = False,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)


#panel 2 - right
for xBlocks in np.arange (0, 1, 0.1): #blocks along y axis
    for yBlocks in np.arange (0, 1, 0.1): #blocks along x axis
            rectangle = mplpatches.Rectangle([xBlocks,yBlocks], 0.1, 0.1,
                                            facecolor = (xBlocks, yBlocks, 1),
                                            edgecolor = 'black',
                                            linewidth = 1)
            panel2.add_patch(rectangle)
    
panel2.set_xlim(0,1)
panel2.set_ylim(0,1)
panel2.tick_params(bottom = False, labelbottom = False,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)


plt.savefig(args.output_file, dpi = 600)