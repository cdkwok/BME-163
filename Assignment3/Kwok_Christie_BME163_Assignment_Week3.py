#Christie Kwok
#4/23/21
#Assignment 3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import argparse
import math

plt.style.use('BME163') 

xList = []
yList = []

xRed = []
yRed = []

xLabel = []
yLabel = []
geneList = []

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file')
parser.add_argument('-s', '--style_sheet', default='BME163')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()
input_file = args.input_file
plt.style.use(args.style_sheet)

inFile = open(args.input_file)
for line in inFile:
    splitLine = line.strip().split('\t')
    geneName = splitLine[0] #gene name
    
    if splitLine[1] == 'NA':
        foldChange = 1 
        xList.append((foldChange))
    else:
        foldChange = float(splitLine[1])
        xList.append((foldChange))
    
    
    if splitLine[2] == 'NA':
        pValue = 0
        yList.append(pValue)
        
    else:
        pValue = float(splitLine[2])
        yList.append(-np.log10(pValue)) #p-value

        if 2**(abs(foldChange)) > 10 and -np.log10(pValue) > 8:
            xRed.append(foldChange)
            yRed.append(-np.log10(pValue))
            
        if foldChange < 0 and 2**(abs(foldChange)) > 10 and -np.log10(pValue) > 30:
            xLabel.append(foldChange)
            yLabel.append(-np.log10(pValue))
            geneList.append(geneName)
  
        
figureHeight = 3
figureWidth = 3

plt.figure(figsize = (figureWidth, figureHeight))

#size of individual left and right figures 
mainPanelWidth = 2
mainPanelHeight = 2


#panels - left
mainPanel = plt.axes([1/6, 1/6, 2/3, 2/3])


#main panel

mainPanel.plot(xList, yList, 
                marker = 'o', 
                markerfacecolor = 'black',
                markeredgecolor = 'black', 
                markersize = 2**0.5, 
                markeredgewidth = 0, 
                linewidth = 0)

mainPanel.plot(xRed, yRed, 
                marker = 'o', 
                markerfacecolor = 'red',
                markeredgecolor = 'red', 
                markersize = 2**0.5, 
                markeredgewidth = 0, 
                linewidth = 0)

mainPanel.plot(xLabel, yLabel, 
                marker = 'o', 
                markerfacecolor = 'red',
                markeredgecolor = 'red', 
                markersize = 2**0.5, 
                markeredgewidth = 0, 
                linewidth = 0)

mainPanel.set_xlabel( "log$_2$(fold change)")
mainPanel.set_ylabel("-log$_{10}$(p-value)")

for label in range(len(geneList)):
    mainPanel.text(xLabel[label], yLabel[label], geneList[label] + ' ' , va = 'center', ha = 'right', fontsize = 6)
    
mainPanel.set_xlim(-12, 12)
mainPanel.set_ylim(0, 60)
mainPanel.tick_params(bottom = True, labelbottom = True,
                   left = True, labelleft = True, 
                   right = False, labelright = False,
                   top = False, labeltop = False)





plt.savefig(args.output_file, dpi = 600)