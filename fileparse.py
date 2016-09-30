import sys

#check for command line arguments
if len(sys.argv) < 4 :
  print "Usage python fileparse.py filenumber filetype filepath "
  print " FileNumber can be 00 to 254"
  print " FileType can be 00 to 254"
  print " Storage path is where the PLC file dumps are stored"
  sys.exit()
else:
  filenumber = str(sys.argv[1])
  filetype = str(sys.argv[2])
  strfile = str(sys.argv[3])


smtplist = []

#open the file in Binary read mode
with open(strfile, 'rb') as f:
 #check for file number 04 and file  
 if (filenumber == '04' or '4') and (filetype == '4C'):
   
    buffer = f.read()  
    nb = ''.join([ buffer[x:x+2][::-1] for x in range(0, len(buffer), 2) ])
    smtplist.insert(0,nb[0:15])
    smtplist.insert(1,nb[16:79])
    smtplist.insert(2,nb[80:143])
    smtplist.insert(3,nb[144:207])
    smtplist.insert(4,nb[208:271])
    smtplist.insert(5,nb[272:335])
    smtplist.insert(6,nb[336:399])
    smtplist.insert(7,nb[400:463])
    smtplist.insert(8,nb[464:527])
    smtplist.insert(9,(nb[528:559] + nb[562:593]))
    smtplist.insert(10,(nb[594:641] + nb[643:659]))
    smtplist.insert(11,nb[660:723])
    smtplist.insert(12,nb[726:789])
    smtplist.insert(13,(nb[790:805] + nb[808:855]))
    smtplist.insert(14,nb[856:915])
    #print chr(smtplist[0][3])
    if (ord(smtplist[0][0]) == 0 and ord(smtplist[0][1]) == 9 and ord(smtplist[0][2]) == 3 and ord(smtplist[0][3]) == 140):
      print "SMTP file signature matches"
      if ord(smtplist[1][1]) > 0:
	print "Email Server: " + str(smtplist[1][2:])
      else:
	print "Email server Not Configured"
      if ord(smtplist[2][1]) > 0:
	print "From Address: " + str(smtplist[2][2:])
      else:
	print "From Address: Not Configured"
      if ord(smtplist[3][1]) > 0:
	print "Username:" + str(smtplist[3][2:])
      else:
	print "Username: Not Configured"
      if ord(smtplist[4][1]) > 0:
	print "Password: " + str(smtplist[4][2:])
      else:
	print "Password Not Configured"
      if ord(smtplist[5][1]) > 0:
	print "To Address[1]: " + str(smtplist[5][2:])
      else:
	print "To Address[1]: Not Configured"
      if ord(smtplist[6][1]) > 0:
	print "To Address[2]: " + str(smtplist[6][2:])
      else:
	print "To Address[2]: Not Configured"
      if ord(smtplist[7][1]) > 0:
	print "To Address[3]: " + str(smtplist[7][2:])
      else:
	print "To Address[3]: Not Configured"
      if ord(smtplist[8][1]) > 0:
	print "To Address[4]: " + str(smtplist[8][2:])
      else:
	print "To Address[4]: Not Configured"
      if ord(smtplist[9][1]) > 0:
	print "To Address[5]: " + str(smtplist[9][2:])
      else:
	print "To Address[5]: Not Configured"
      if ord(smtplist[10][1]) > 0:
	print "To Address[6]: " + str(smtplist[10][2:])
      else:
	print "To Address[6]: Not Configured"
      if ord(smtplist[11][1]) > 0:
	print "To Address[7]: " + str(smtplist[11][2:])
      else:
	print "To Address[7]: Not Configured"
      if ord(smtplist[12][1]) > 0:
	print "To Address[8]: " + str(smtplist[12][2:])
      else:
	print "To Address[8]: Not Configured"
      if ord(smtplist[13][1]) > 0:
	print "To Address[9]: " + str(smtplist[13][2:])
      else:
	print "To Address[9]: Not Configured"
    #if not an SMTP file remove it  
    else:
       print "This is not smtp file"
 #tell parser is not configured to parse this file      
 else:
   print "parser is not configured to parse this filenumber and filetype combination"
    