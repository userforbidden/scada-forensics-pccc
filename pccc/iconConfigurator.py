'''
Created on Feb 09, 2017

@author: Saranyan
'''
import os

class propertyFile:
    
    def __init__(self):
        print "propertyFile.py initiated"
        pass
        
    companyName = ""
    participantName = ""
    base_dir = os.path.dirname(__file__)
    Path = os.path.dirname(base_dir)
    xicPath = ""
    endPath = ""
    horlinePath = ""
    verlinePath = ""
    outputEnergizerPath = ""
    loadInstructionsPath = ""
    blankSpacePath = ""
    
    def changePath(self):
        print "changing the paths required"
        self.loadInstructionsPath = self.base_dir + "//instructions//"

        if os.path.isdir(self.base_dir):
            self.load()    
    
    def load(self):
            print "Loading all instructions path"
            self.xicPath = self.loadInstructionsPath + "XIC.JPG"
            self.endPath = self.loadInstructionsPath + "end.JPG"
            self.horlinePath = self.loadInstructionsPath + "horline.JPG"
            self.verlinePath = self.loadInstructionsPath + "verline.JPG"
            self.outputEnergizerPath = self.loadInstructionsPath + "OE.JPG"
            self.blankSpacePath = self.loadInstructionsPath + "blank.JPG"