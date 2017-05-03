import psutil, time  
import string, sys

PervCPUuser = PervCPUnice = PervCPUsys = prevCPUidle = PervCPUiowait = PervCPUIRQ = PervCPUsoftIRQ = PervCPUsteal = PervCPUlast = 0

tmpCPUuser = tmpCPUnice = tmpCPUsys = tmpCPUidle = tmpCPUiowait = tmpCPUIRQ = tmpCPUsoftIRQ = tmpCPUsteal = tmpCPUlast =0

while True:
#find PID from the process name 
    for proc in psutil.process_iter():
        if  proc.name == 'bash':# or proc.name =='bash': # list of processes to monitor
            print "\n Process found for monitoring"
            fileName = "/"+proc.name+'-'+time.strftime("%a-%d-%b-%y-%H-%M-%S",time.gmtime())+'.txt'
            statsFile = open(fileName,'w')
            print 'Open file: %s' %(fileName)
            captionList = 'ProcessName'+','+'pid'+','+'ElapsedTime'+','+'ProcessCPU%age'+','+'CPUIOwait%age'+','+'CPUIdle%age'+','+'PhysicalMemory'+','+\
                      'VirtualMemory'+','+'MemoryUtilization%age'+','+ 'QueueLength'+','+ 'rIOops'+','+ 'wIOops'+','+ 'rIObytes'+','+'wIObytes'+','+\
                      'pageFaults'+','+'NetBytesReceived'+','+'NetPacketReceived'+','+'NetPacketDropped(Received)'+','+'NetBytesTransmitted'+','+\
                      'NetPacketTransmitted'+','+'NetPacketDropped(Transmitted)'+'\n'               
            statsFile.write(captionList)
            
            fcpu = open('/proc/stat','r') # temporary store the previous values of CPU utilization parameters
            for line in fcpu.readlines():
                if line[:4]=='cpu ':
                    line=line.split()
                    PervCPUuser = int(line[1])
                    PervCPUnice = int(line[2])
                    PervCPUsys = int(line[3])
                    prevCPUidle = int(line[4])
                    PervCPUiowait = int(line[5])
                    PervCPUIRQ = int(line[6])
                    PervCPUsoftIRQ = int(line[7])
                    PervCPUsteal = int(line[8])
                    PervCPUlast = int(line[9])
                    fcpu.close()
                    break
                
            while psutil.pid_exists(proc.pid):  
                try:      
                    p = psutil.Process(proc.pid)
                    rIOops = -1
                    wIOops = -1
                    rIObytes = -1
                    wIObytes = -1
                    
                    ppath = "/proc/"+str(proc.pid)+"/io"
                    pfpath = "/proc/"+str(proc.pid)+"/stat"
                    netpath = "/proc/"+str(proc.pid)+"/net/dev"
                    f = open(ppath,'r')
                    for line in f.readlines():
                        line=line.strip()
                        if str.find(line,"syscr")>-1: #  Read IO Operations
                            pos = str.rfind(line,":")+2
                            rIOops = int(line[pos:])
                        elif str.find(line,"syscw")>-1: # Write IO Operations
                            pos = str.rfind(line,":")+2
                            wIOops = int(line[pos:])
                        elif str.find(line,"read_bytes")>-1: # IO Read bytes
                            pos = str.rfind(line,":")+2
                            rIObytes = int(line[pos:])
                        elif str.find(line,"write_bytes")>-1 and str.find(line,"cancelled_write_bytes")<0: # IO Write bytes 
                            pos = str.rfind(line,":")+2  
                            wIObytes = int(line[pos:])
                          
                    pfstats = string.split(open(pfpath).read()) # read /proc/<pid>/stat for page fault information
                    
                    netfile = open(netpath,'r')
                    for line in netfile.readlines():
                        line=line.strip()
                        if line[:4]=='eth0':
                            netstats = string.split(line)                    
                    
           
                    fcpu = open('/proc/stat','r') # reading values of CPU utilization parameters
                    for line in fcpu.readlines():
                        if line[:4]=='cpu ':
                            line=line.split()
                            tmpCPUuser = int(line[1]) - PervCPUuser
                            tmpCPUnice = int(line[2]) - PervCPUnice
                            tmpCPUsys = int(line[3]) - PervCPUsys
                            tmpCPUidle=int(line[4])-prevCPUidle
                            tmpCPUiowait = int(line[5]) - PervCPUiowait
                            tmpCPUIRQ = int(line[6]) - PervCPUIRQ
                            tmpCPUsoftIRQ = int(line[7]) - PervCPUsoftIRQ
                            tmpCPUsteal = int(line[8]) - PervCPUsteal
                            tmpCPUlast = int(line[9]) - PervCPUlast
                                                        
                            # assigning previous values
                            PervCPUuser = int(line[1]) 
                            PervCPUnice = int(line[2])  
                            PervCPUsys = int(line[3])  
                            prevCPUidle = int(line[4])  
                            PervCPUiowait = int(line[5])  
                            PervCPUIRQ = int(line[6])  
                            PervCPUsoftIRQ = int(line[7])  
                            PervCPUsteal = int(line[8]) 
                            PervCPUlast = int(line[9])                   
                            fcpu.close()
                            break
                    
                    TotalCPUusage =  tmpCPUuser + tmpCPUnice + tmpCPUsys + tmpCPUidle + tmpCPUiowait + tmpCPUIRQ + tmpCPUsoftIRQ + tmpCPUsteal + tmpCPUlast
                    
                    if TotalCPUusage == 0:
                        IOwait = 0
                        Idle = 0
                    else:
                        IOwait = float (tmpCPUiowait) / float(TotalCPUusage) * 100.0
                        Idle = float (tmpCPUidle) / float(TotalCPUusage) * 100.0                        

                    fdisk = open('/proc/diskstats','r') # reading values of CPU utilization parameters
                    for line in fdisk.readlines():
                        line=line.split()
                        if line[2]=='sda':
                            queueLength = float(line[11])
                            
                    S = ('%s,%s,%.2f,%.2f,%.2f,%.2f,%d,%.2f,%.2f,%.2f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n')  %(proc.name,proc.pid,(time.time()-p.create_time),p.get_cpu_percent(interval=0.1),IOwait,Idle,p.get_memory_info().rss,p.get_memory_info().vms,p.get_memory_percent(),queueLength,rIOops,wIOops,rIObytes,wIObytes,int(pfstats[11]),int(netstats[1]),int(netstats[2]),int(netstats[4]),int(netstats[9]),int(netstats[10]),int(netstats[12]))
                  
                    #S = str(proc.name)+','+str(proc.pid)+','+str((time.time()-p.create_time))+','+str(p.get_cpu_percent(interval=0.1))+','+str(IOwait)+','+str(Idle)+','+str(p.get_memory_info().rss)+','+\
                    #str(p.get_memory_info().vms)+','+str(p.get_memory_percent())+','+ str(queueLength) +','+ str(rIOops)+','+ str(wIOops)+','+ str(rIObytes)+','+str(wIObytes)+','+pfstats[11]+','+netstats[1]+','+netstats[2]+','+netstats[4]+','+netstats[9]+','+netstats[10]+','+netstats[12]+'\n'           
                    statsFile.write(S)
                
                except:
                    if psutil.NoSuchProcess(proc.pid):    
                        print '\nProcess ended'
                    else:
                        print "Unexpected error:", sys.exc_info()[0]
                        raise
                       
            else:
                statsFile.close()
                print 'Closing file: %s' %(fileName)
            break