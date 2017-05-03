 #!/bin/bash
#  OPTIONS="Create_Baseline Compare_with_Baseline Quit"
#            select opt in $OPTIONS; do
#                if [ "$opt" = "Quit" ]; then
#                 echo done
#                 exit
#                elif [ "$opt" = "Create_Baseline" ]; then
# 		echo Enter the path of .pcap file of which the baseline to be created
# 		read FN
#                 echo Create_Baseline at $FN
#                elif [ "$opt" = "Compare_with_Baseline" ]; then
#                 echo Compare_with_Baseline
#                else
#                 clear
#                 echo bad option
#                fi
#            done
  stringFN=$1
  if [stringFN = ""]; then
    echo No file name given
  else 
    #clear
    echo ${stringFN:(-5)}
    echo Creating baseline at stringFN
    #echo a
    #python extractor.py $1
  fi
  
  #python pcapfile destinationfolder