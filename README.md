PLC Ladder logic Extractor
-
This document tells you how to run and configuration needed for the tool

To run the command use
python extractor.py capturefile destination-directory
-
capture file is wireshark capture file of type *.pcap

destination-directory is the directory where your files will be stored

Dependencies:
-
The only dependency for this tool is PyShark 
It is the python wrapper for TShark.

PyShark installation information can be found from https://github.com/KimiNewt/pyshark
