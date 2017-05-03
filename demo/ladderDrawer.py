'''
Created on Feb 6, 2017

@author: Saranyan
'''
import os, sys
from PIL import Image
from iconConfigurator import propertyFile

#all_instructions = ['e40000019e4f0000', 'e4000103ae4f0100', 'bc0000009c4f0e00']

class ladderDrawer:
    def __init__(self):
      print "Ladder Drawer Initiated"
    
    imagePathForHorizontalMerging = []
    saveDir = ""
      
    def setFilepath(self, instructions, num):
      print "Rung Number : " + str(num)
      del self.imagePathForHorizontalMerging[:]
      propertyVar = propertyFile()
      propertyVar.changePath()
      #print str(self.imagePathForHorizontalMerging) + str(num)
      
      self.imagePathForHorizontalMerging.append(propertyVar.blankSpacePath)
      self.imagePathForHorizontalMerging.append(propertyVar.verlinePath)
      
      for i in range(0, len(instructions)):
	  #print instructions[i][0:2]
	  if instructions[i][0:2] == 'e4':
	    #im = Image.open(propertyVar.xicPath)
	    #print im.size
	    self.imagePathForHorizontalMerging.append(propertyVar.horlinePath)
	    self.imagePathForHorizontalMerging.append(propertyVar.xicPath)
	    self.imagePathForHorizontalMerging.append(propertyVar.horlinePath)
	  elif instructions[i][0:2] == 'bc':
	    self.imagePathForHorizontalMerging.append(propertyVar.horlinePath)
	    self.imagePathForHorizontalMerging.append(propertyVar.outputEnergizerPath)
	    self.imagePathForHorizontalMerging.append(propertyVar.horlinePath)
	  elif instructions[i][0:2] == '30':
	    self.imagePathForHorizontalMerging.append(propertyVar.horlinePath)
	    self.imagePathForHorizontalMerging.append(propertyVar.endPath)
	    self.imagePathForHorizontalMerging.append(propertyVar.horlinePath)
	    
      self.imagePathForHorizontalMerging.append(propertyVar.verlinePath)
      self.imagePathForHorizontalMerging.append(propertyVar.blankSpacePath)
      #print str(self.imagePathForHorizontalMerging) + str(num)
      return self.imagePathForHorizontalMerging
      #print self.imagePathForVerticalMerging
    
    def combineImageHorizontally(self,fileList,newfileName):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        images = map(Image.open, fileList)
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]
	
	dir_com = dir_path+'/'+self.saveDir
	print dir_com
	if not os.path.exists(dir_com):
	    os.makedirs(dir_com)
	new_im.save(dir_com+newfileName + '.jpg')
	
    def setSaveDir(self,strname):
	self.saveDir = strname
	
    def getSaveDir(self):
	return self.saveDir
      
    