"""
 This util is to calculate PDSCH TB size for NR 5G
 For Ninfo < 3824, please refer to table in 38.214 as mentioned in the script
 Further enhancements for LDPCgraph selection pending
"""

import math
from sys import exit
print ("""Please use the appropriate table in the script for 64QAM and 256QAM. Please state the MCS table to use
        							0 - 64QAM
        							1 - 256QAM""")


class TBCalculator:
    IMCS = []
    Qm = []
    R = []
    Layers = []
    xOverhead = []
    NRB_SC = -1
    MCS = -1
    numlayers =-1
    Nsh_Sym=-1
    NPRB_DMRS=-1
    Overhead=-1
    Total_prbs=-1
	
    def __init__(self, MCS_Table, MCS, numlayers, Nsh_Sym, NPRB_DMRS, Overhead, Total_prbs):
        '''
        MCS_Table = int(raw_input("""Please state the MCS table to use
        							0 - 64QAM
        							1 - 256QAM
        							> """))
        '''
		
	for mcsCount in range(0,32):
	    self.IMCS.append(mcsCount)
			
        if MCS_Table == '64QAM':
        	""" For 64QAM"""
        	self.Qm = [2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,2,4,6]
        	self.R = [120,157,193,251,308,379,449,526,602,679,340,378,434,490,553,616,658,438,466,517,567,616,666,719,772,822,873,910,948]
        elif MCS_Table == '256QAM':
        	""" For 256QAM"""
        	self.Qm = [2,2,2,2,2,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,8,8,8,8,8,8,8,8,2,4,6,8]
        	self.R = [120,193,308,449,602,378,434,490,553,616,658,466,517,567,616,666,719,772,822,873,682.5,711,754,797,841,885,916.5,948]
        else:
		    print "Incorrect Value entered by user"
        
        #Layers = [1,2,3,4,5,6,7,8]

	for layersCount in range(1,9):
            self.Layers.append(layersCount)
            self.xOverhead = [0, 6, 12, 18]
            self.NRB_SC = 12
		
		
        
		
	def TBCalc(self):
	
            MCS_Index = self.IMCS.index(self.MCS)
            Modulation_order = self.Qm.pop(MCS_Index)
            Code_Rate = self.R.pop(MCS_Index)/1024.00000
            print("The code rate used is %r and modulation order is %r") %(Code_Rate, Modulation_order)
    
            nre_prb = (self.NRB_SC*self.Nsh_Sym)-self.NPRB_DMRS-self.Overhead
            NRE = min(156,nre_prb)*self.Total_prbs
            N_info = NRE*self.Code_Rate*Modulation_order*self.numlayers
            print("Intermediate number of information bits are %r") %N_info
        
            if N_info <= 3824:
                n = max(3, math.floor(math.log(N_info,2))-6)
        	N_info_quant_1 = max(24,math.pow(2,n)*math.floor(N_info/math.pow(2,n)))
        	print ("\nquantized intermediate number of information bits : %r\nFor TBS please refer to table 5.1.3.2-2 in 38.214") %N_info_quant_1
        	exit()
            else:
        	n = math.floor(math.log(N_info-24,2))-5
        	N_info_quant = max(3840, math.pow(2,n)*math.ceil((N_info-24)/math.pow(2,n)))
        	print "quantized intermediate number of information bits : %r\n" %N_info_quant
        
            if Code_Rate <=0.25:
        	C = math.ceil((N_info_quant+24)/3816)
        	TBS = 8*C*math.ceil((N_info_quant+24)/(8*C))-24
        	print("Code rate > 1/4 and TB size is : %r\n") %TBS
            else:
        	if N_info_quant > 8424:
        	    C = math.ceil((N_info_quant+24)/8424)
        	    TBS = 8*C*math.ceil((N_info_quant+24)/(8*C))-24
        	    Average_Througput = ((TBS*160/80)*1000)
        	    print("As N_info_quant > 8424 and Code rate > 1/4, TB size is : %r\n") %TBS
        	    print("Average throughput : %r bps") %Average_Througput
        	else:
        	    TBS = 8*math.ceil((N_info_quant+24)/8)-24
        	    Average_Througput = ((TBS*160/80)*1000)
        	    print("As N_info_quant < 8424 and Code rate > 1/4,TB size is : %r\n")%TBS
        	    print("Average throughput : %r bps") %Average_Througput
        
        # Further enhancements for LDPCgraph selection pending
        #if TBS <= 292:
        	#print "LDPCgraph2"
        #else:
        	#print "TBS > 292"
        #if TBS <= 3824:
        	#if Modulation_order <= (67/100):
        		#print "LDPCgraph2"
        	#else:
        		#print "Modulation_order is > 0.67"
        #else:
        	#print "TBS is > 3824"
        
        #if Modulation_order <= (25/100):
        	#print "LDPCgraph2"
        #else:
        	#print "LDPCgraph1"
        raw_input()
