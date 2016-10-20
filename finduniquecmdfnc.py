import pyshark
import sys 

if len(sys.argv) < 1 :
  print "Usage python finduniquecmdfnc.py capturefile "
  print " Capture File is the Network Capture"
  sys.exit()
else:
  capturefile = str(sys.argv[1])  

cap = pyshark.FileCapture(capturefile)
func0f = []
func06 = []
func46 = []
func4f = []
comm = []

def print_enip_packets(pkt):
    try:

        enip_lay = pkt.layers
        cpfdata = enip_lay[3].cpf_data
        alternatefield = str(cpfdata.alternate_fields)
        only_data = alternatefield[28:].split(">]")
        hex_bytes = only_data[0].split(":")
        hex_range = len(hex_bytes)
        comm.append(hex_bytes[0])
        if hex_bytes[0] == "0f":
          func0f.append(hex_bytes[4])
        elif hex_bytes[0] == "4f": 
          func4f.append(hex_bytes[4])  
        elif hex_bytes[0] == "06":
          func06.append(hex_bytes[4])
        else:
          func4f.append(hex_bytes[4])
    except AttributeError as e:
        #ignore packets that aren't ENIP
        pass
    except IndexError as e2:
        #ignoring out of index packets
        pass
cap.apply_on_packets(print_enip_packets, timeout=100)
commset = set(comm)
func0fset = set(func0f)
func4fset = set(func4f)
func46set = set(func46)
func06set = set(func06)
print "Commands: " + str(commset)
print " Unique Function codes of 0f: " + str(func0fset)
print " Unique Function codes of 06: " + str(func06set)