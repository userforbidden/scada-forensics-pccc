'''
Created on Feb 9, 2017

@author: Saranyan
'''

import sys
import string
import struct
import filecap
import binascii
from ladderDrawer import ladderDrawer


class fileparse():
    
    
    def __init__(self):
      print "fileparse Initiated"
      
    smtplist = []
    all_rungs = []
    all_instructions = []
    allRungFileList = []
    fileNameDir = []
	
    def fileFinder(self,strfile,filetype):
      #open the file in Binary read mode
      self.fileNameDir = strfile.split('/')
      with open(strfile, 'rb') as f:
      #check for file number 04 and file  
	if (filetype == '4C'):
       
	  buffer = f.read()  
	  nb = ''.join([ buffer[x:x+2][::-1] for x in range(0, len(buffer), 2) ])
	  self.smtplist.insert(0,nb[0:15])
	  self.smtplist.insert(1,nb[16:79])
	  self.smtplist.insert(2,nb[80:143])
	  self.smtplist.insert(3,nb[144:207])
	  self.smtplist.insert(4,nb[208:271])
	  self.smtplist.insert(5,nb[272:335])
	  self.smtplist.insert(6,nb[336:399])
	  self.smtplist.insert(7,nb[400:463])
	  self.smtplist.insert(8,nb[464:527])
	  self.smtplist.insert(9,(nb[528:559] + nb[562:593]))
	  self.smtplist.insert(10,(nb[594:641] + nb[643:659]))
	  self.smtplist.insert(11,nb[660:723])
	  self.smtplist.insert(12,nb[726:789])
	  self.smtplist.insert(13,(nb[790:805] + nb[808:855]))
	  self.smtplist.insert(14,nb[856:915])
	  #print chr(smtplist[0][3])
	  if (ord(self.smtplist[0][0]) == 0 and ord(self.smtplist[0][1]) == 9 and ord(self.smtplist[0][2]) == 3 and ord(self.smtplist[0][3]) == 140):
	    print "SMTP file signature matches"
	    if ord(self.smtplist[1][1]) > 0:
		print "Email Server: " + str(self.smtplist[1][2:])
	    else:
		print "Email server Not Configured"
	    if ord(self.smtplist[2][1]) > 0:
		print "From Address: " + str(self.smtplist[2][2:])
	    else:
		print "From Address: Not Configured"
	    if ord(self.smtplist[3][1]) > 0:
		print "Username:" + str(self.smtplist[3][2:])
	    else:
		print "Username: Not Configured"
	    if ord(self.smtplist[4][1]) > 0:
		print "Password: " + str(self.smtplist[4][2:])
	    else:
		print "Password Not Configured"
	    if ord(self.smtplist[5][1]) > 0:
		print "To Address[1]: " + str(self.smtplist[5][2:])
	    else:
		print "To Address[1]: Not Configured"
	    if ord(self.smtplist[6][1]) > 0:
		print "To Address[2]: " + str(self.smtplist[6][2:])
	    else:
		print "To Address[2]: Not Configured"
	    if ord(self.smtplist[7][1]) > 0:
		print "To Address[3]: " + str(self.smtplist[7][2:])
	    else:
		print "To Address[3]: Not Configured"
	    if ord(self.smtplist[8][1]) > 0:
		print "To Address[4]: " + str(self.smtplist[8][2:])
	    else:
		print "To Address[4]: Not Configured"
	    if ord(self.smtplist[9][1]) > 0:
		print "To Address[5]: " + str(self.smtplist[9][2:])
	    else:
		print "To Address[5]: Not Configured"
	    if ord(self.smtplist[10][1]) > 0:
		print "To Address[6]: " + str(self.smtplist[10][2:])
	    else:
		print "To Address[6]: Not Configured"
	    if ord(self.smtplist[11][1]) > 0:
		print "To Address[7]: " + str(self.smtplist[11][2:])
	    else:
		print "To Address[7]: Not Configured"
	    if ord(self.smtplist[12][1]) > 0:
		print "To Address[8]: " + str(self.smtplist[12][2:])
	    else:
		print "To Address[8]: Not Configured"
	    if ord(self.smtplist[13][1]) > 0:
		print "To Address[9]: " + str(self.smtplist[13][2:])
	    else:
		print "To Address[9]: Not Configured"
	    if ord(self.smtplist[14][1]) > 0:
		print "To Address[10]: " + str(self.smtplist[14][2:])
	    else:
		print "To Address[10]: Not Configured"
	  #if not an SMTP file remove it  
	  else:
	    print "This is not smtp file"
	#tell parser is not configured to parse this file      
	elif filetype == '85':
	  buf = f.read()
	  indi = filecap.borders(buf,2)
	  print "Data present in file : " + strfile 
	  for i,j in enumerate(indi):
	    #print dir(i)
	    print "Index:" + str(i) + " =" ,
	    y = str(struct.unpack("h",str(j)))
	    print y.split('(')[1].split(',')[0]
	elif filetype == '22':
	  
	  ld = ladderDrawer()
	  saveDir = 'Results'+'/'+str(self.fileNameDir[5])+'/'
	  ld.setSaveDir(saveDir)
	  buf = f.read()
	  hexx = binascii.hexlify(buf)
	  self.rungSplitter(hexx)
	  for i in range(0,len(self.all_rungs)):
	    del self.all_instructions[:]
	    self.instructionSplitter(self.all_rungs[i][12:])
	    imagename = "Rung:"+str(i)
	    
	    fl = ld.setFilepath(self.all_instructions, i)
	    #print fl
	    ld.combineImageHorizontally(fl,imagename)
	    #print ld.getAllFilePath()
	
       
	else:
	  print "parser is not configured to parse this filenumber and filetype combination"
      
    
    def rungSplitter(self,str):
        try:
            sz_limit = int(str[8:10],16)
            rung = str[0:sz_limit*2]
            self.all_rungs.append(rung)
            rem = self.rungSplitter(str[sz_limit*2:])
        except:
            pass

    def instructionSplitter(self, str):
        try:
            instruc = str[0:16]
            self.all_instructions.append(instruc)
            rem = str[16:]
            if rem != "":
                self.instructionSplitter(rem)
        except:
            pass
    
    def setAllFilePath(self, str):
        print self.imagePathForVerticalMerging
        self.imagePathForVerticalMerging.append(str)
        print self.imagePathForVerticalMerging
    
    def getAllFilePath(self):
        #del self.imagePathForHorizontalMerging[:]
        return self.imagePathForVerticalMerging
        #del self.imagePathForVerticalMerging[:]
      
    
def main():
    #check for command line arguments
    if len(sys.argv) < 3 :
	print "Usage python fileparse.py filetype filepath "
	#print " FileNumber can be 00 to 254"
	print " FileType can be 00 to 254"
	print " Storage path is where the PLC file dumps are stored"
	sys.exit()
    else:
	#filenumber = (str(sys.argv[1])).upper()
	filetype = (str(sys.argv[1])).upper()
	strfile = str(sys.argv[2])
	dial = fileparse()
	dial.fileFinder(strfile,filetype)
if __name__ == '__main__': 
    main()    
