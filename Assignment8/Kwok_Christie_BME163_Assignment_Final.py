#Christie Kwok
# 6/9/21
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import matplotlib.image as mpimg
import numpy as np
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-i1', '--input_file1', default = 'BME163_Input_Data_5.psl')
parser.add_argument('-i2', '--input_file2', default = 'BME163_Input_Data_6.psl')
parser.add_argument('-g', '--input_fileG', default = 'gencode.vM12.annotation.gtf')
parser.add_argument('-s', '--style_sheet', default = 'BME163')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()

plt.style.use(args.style_sheet)
topInFile = (args.input_fileG)
middleInFile = (args.input_file2)
bottomInFile = (args.input_file1)

def readGtf(inFile):
    transcriptList = []
    gtfDict = {}
    for line in open(inFile):
        if line[0] != '#':
            a = line.strip().split('\t')
            chromosome = a[0]
            type1 = a[2]
            if type1 in  ['exon','CDS']:
                start = int(a[3])
                end = int(a[4])
                transcript = a[8].split(' transcript_id "')[1].split('"')[0]
                if transcript not in gtfDict:
                    gtfDict[transcript] = []
                gtfDict[transcript].append([chromosome,start,end,type1])

    for transcript,parts in gtfDict.items():
        starts = []
        ends = []
        blockstarts = []
        blockwidths = []
        types = []
        for part in parts:
            starts.append(part[1])
            ends.append(part[2])
            blockstarts.append(part[1])
            blockwidths.append(part[2]-part[1])
            chromosome = part[0]
            types.append(part[3])
        transcriptList.append([chromosome,min(starts),max(ends),blockstarts,blockwidths,types])

    return transcriptList
    
def readData(inFile):
    readList = []
    openFile = open(inFile,'r')
#    firstLine = openFile.readline()
    for line in openFile:
        a = line.strip().split('\t')
        chromosome = a[13]
        start = int(a[15])
        end = int(a[16])
        blockstarts = np.array(a[20].split(',')[:-1],dtype = int)
        blockwidths = np.array(a[18].split(',')[:-1],dtype = int)
        if chromosome == 'chr7':
            read = [chromosome,start,end,blockstarts,blockwidths]
            readList.append(read)

    return readList


def plotReads(panel,readList,target):
    genome_chromosome,genome_start,genome_end = target[0],target[1],target[2]
    bottom = 0
    filteredReadList = []
    for read in readList:
        chromosome,start,end,blockstarts,blockwidths = read[0],read[1],read[2],read[3],read[4]
        if chromosome == genome_chromosome:
            if genome_start<start<genome_end or genome_start<end<genome_end:
                filteredReadList.append(read)
                
    
    
    filteredReadList.sort(key = lambda a: (a[2]))
    plotList = []
    yValues = []
    allPlotted = False
    for i in range(0,len(filteredReadList)):
        plotList.append(False)
        
    while allPlotted == False:
        allPlotted = True
        lastEnd = 0
        for i in range(len(filteredReadList)):
            if plotList[i] == False:
                chromosome,start,end,blockstarts,blockwidths=filteredReadList[i][0],filteredReadList[i][1],filteredReadList[i][2],filteredReadList[i][3],filteredReadList[i][4]
                if start > lastEnd:
                    rectangle1=mplpatches.Rectangle((start,bottom+0.18),end-start, 0.1,facecolor='black',edgecolor='black',linewidth=0)
                    panel.add_patch(rectangle1)
                    lastEnd = end
                    yValues.append(bottom)
                    plotList[i] = True
                    for index in np.arange(0,len(blockstarts),1):
                        blockstart=blockstarts[index]
                        blockwidth=blockwidths[index]
                        rectangle1=mplpatches.Rectangle((blockstart,bottom),blockwidth, 0.5,facecolor='black',edgecolor='black',linewidth=0)
                        panel.add_patch(rectangle1)
                else:
                    allPlotted = False
                                  
        bottom += 1
    yValues.sort(reverse = True)
    maxYValue = yValues[0]
    return maxYValue
 
def plotReads2(panel,readList,target):
    genome_chromosome,genome_start,genome_end=target[0],target[1],target[2]
    bottom=1
    filteredReadList = []
    for read in readList:
        chromosome,start,end,blockstarts,blockwidths,types=read[0],read[1],read[2],read[3],read[4], read[5]
        if chromosome==genome_chromosome:
            if genome_start<start<genome_end or genome_start<end<genome_end:
                filteredReadList.append(read)
                
    
    
    filteredReadList.sort(key=lambda a: (a[2]))
    plotList = []
    yValues = []
    allPlotted = False
    for i in range(0,len(filteredReadList)):
        plotList.append(False)
    
    while allPlotted == False:
        allPlotted = True
        lastEnd = 0
        for i in range(0,len(filteredReadList)):
            if plotList[i] == False:
                chromosome,start,end,blockstarts,blockwidths, types=filteredReadList[i][0],filteredReadList[i][1],filteredReadList[i][2],filteredReadList[i][3],filteredReadList[i][4],filteredReadList[i][5]
                if start > lastEnd:
                    rectangle1=mplpatches.Rectangle((start,bottom+0.2),end-start, 0.1,facecolor='black',edgecolor='black',linewidth=0)
                    panel.add_patch(rectangle1)
                    lastEnd = end
                    plotList[i] = True
                    yValues.append(bottom)
                    for index in np.arange(0,len(blockstarts),1):
                        blockstart=blockstarts[index]
                        blockwidth=blockwidths[index]
                        if types[index] == 'exon':
                            rectangle1=mplpatches.Rectangle((blockstart,bottom+ 0.1),blockwidth, 0.25,facecolor='black',edgecolor='black',linewidth=0)
                            panel.add_patch(rectangle1)      
                        elif types[index] == 'CDS':
                            rectangle1=mplpatches.Rectangle((blockstart,bottom),blockwidth, 0.5,facecolor='black',edgecolor='black',linewidth=0)
                            panel.add_patch(rectangle1)
                else:
                    allPlotted = False
                   
                   
        bottom += 1
    yValues.sort(reverse = True)
    maxYValue = yValues[0]
    return maxYValue   


#plt.style.use('BME163')

figureHeight=5
figureWidth=10

plt.figure(figsize=(figureWidth,figureHeight))

panelWidth = 10
panelHeight = 1.25

relativePanelWidth=panelWidth/figureWidth
relativePanelHeight=panelHeight/figureHeight

# left,bottom, width,height
topPanel = plt.axes([0.001,0.65,relativePanelWidth,relativePanelHeight],frameon=True)
middlePanel = plt.axes([0.001,0.35,relativePanelWidth,relativePanelHeight],frameon=True)
bottomPanel = plt.axes([0.001,0.05,relativePanelWidth,relativePanelHeight],frameon = True)

target = ['chr7',45232945,45240000]

topReadList = readGtf(topInFile)
middleReadList = readData(middleInFile)
bottomReadList = readData(bottomInFile)

top  =  plotReads2(topPanel, topReadList, target)
middle = plotReads(middlePanel, middleReadList, target)
bottom = plotReads(bottomPanel, bottomReadList, target)
topPanel.set_xlim(target[1], target[2])
topPanel.set_ylim(0, top + 2)

middlePanel.set_xlim(target[1], target[2])
middlePanel.set_ylim(0, middle + 7.5)

bottomPanel.set_xlim(target[1], target[2])
bottomPanel.set_ylim(0, bottom + 40)

topPanel.tick_params(bottom = False, labelbottom = False,
                  left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)
middlePanel.tick_params(bottom = False, labelbottom = False,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)
bottomPanel.tick_params(bottom = False, labelbottom = False,
                   left = False, labelleft = False, 
                   right = False, labelright = False,
                   top = False, labeltop = False)         
                   
plt.savefig(args.output_file, dpi = 1200)
