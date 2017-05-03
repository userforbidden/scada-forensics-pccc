import binascii
import itertools
import sys

strfile = str(sys.argv[1])
all_rungs = []

def starter(str):
    try:
     sz_limit = int(str[8:10],16)
     rung = str[0:sz_limit*2]
     all_rungs.append(rung)
     rem = starter(str[sz_limit*2:])
    except:
     pass

with open(strfile, 'rb') as f:
     buf=f.read()
     hexx = binascii.hexlify(buf)
f.close()

starter(hexx)

print all_rungs
