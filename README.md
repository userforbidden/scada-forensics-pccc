PLC Ladder logic Extractor
-
This document tells you how to run and configuration needed for the tool

To run the extractor use command
python extractor.py capturefile destination-directory
-
capture file is wireshark capture file of type *.pcap or *.pcapng

destination-directory is the directory where your files will be stored

=======================================================================================

To parse an extracted file use command
python fileparse.py filenumber filetype file-path
-
filenumber can be 00 to 254 in hex

filetype can be 00 to 254 in hex

file-path is the directory path of the file to be parsed

=======================================================================================

Dependencies:
-
The only dependency for this tool is PyShark 
It is the python wrapper for TShark.

PyShark installation information can be found from https://github.com/KimiNewt/pyshark
>>>>>>> d0884c4d5075c2c3e1e0360d7d6ce77983cee932
