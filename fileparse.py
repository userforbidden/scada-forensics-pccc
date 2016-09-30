import sys

strfile = r'/mnt/hgfs/Wireshark Captures/New Testing/testresults/test40res//download-[5, 122]/file:04-Type:4c'
smtplist = []
with open(strfile, 'rb') as f:
  buffer = f.read()
  #print len(buffer)
  
  nb = ''.join([ buffer[x:x+2][::-1] for x in range(0, len(buffer), 2) ])
  nbnew = nb[17:]
  bits = 64
  smtplist = [nbnew[i:i+bits] for i in range(0, len(nbnew), bits)]
  
  for i in range(0,len(smtplist)):
   print smtplist[i]
    