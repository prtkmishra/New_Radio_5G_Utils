#########################################################
# This util is to calculate PDSCH TB size for NR 5G
# For Ninfo < 3824, please refer to table in 38.214 as mentioned in the script
# Further enhancements for LDPCgraph selection pending
#########################################################

import math
from sys import exit
print "Please use the appropriate table in the script for 64QAM and 256QAM"

MCS_Table = int(raw_input("""Please state the MCS table to use
							0 - 64QAM
							1 - 256QAM
							> """))

IMCS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
if MCS_Table == 0:
	""" For 64QAM"""
	Qm = [2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,2,4,6]
	R = [120,157,193,251,308,379,449,526,602,679,340,378,434,490,553,616,658,438,466,517,567,616,666,719,772,822,873,910,948]
else:
	""" For 256QAM"""
	Qm = [2,2,2,2,2,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,8,8,8,8,8,8,8,8,2,4,6,8]
	R = [120,193,308,449,602,378,434,490,553,616,658,466,517,567,616,666,719,772,822,873,682.5,711,754,797,841,885,916.5,948]


Layers = [1,2,3,4,5,6,7,8]
xOverhead = [0, 6, 12, 18]
NRB_SC = 12

MCS = int(raw_input("Enter the MCS value> "))
MCS_Index = IMCS.index(MCS)
Modulation_order = Qm.pop(MCS_Index)
Code_Rate = R.pop(MCS_Index)/1024.00000
print "The code rate used is %r and modulation order is %r" %(Code_Rate, Modulation_order)
numlayers = int(raw_input("Enter number of layers> "))
Nsh_Sym = int(raw_input("Number of symbols of the PDSCH allocation within the slot> "))
NPRB_DMRS = int(raw_input("Number of REs for DM-RS per PRB> "))
Overhead = int(raw_input("Overhead configured by higher layer parameter Xoh-PDSCH> "))
Total_prbs = int(raw_input("Total number of allocated PRBs for the UE> "))


nre_prb = (NRB_SC*Nsh_Sym)-NPRB_DMRS-Overhead
NRE = min(156,nre_prb)*Total_prbs
N_info = NRE*Code_Rate*Modulation_order*numlayers
print "Intermediate number of information bits are %r" %N_info

if N_info <= 3824:
	n = max(3, math.floor(math.log(N_info,2))-6)
	N_info_quant_1 = max(24,math.pow(2,n)*math.floor(N_info/math.pow(2,n)))
	print "\nquantized intermediate number of information bits : %r\nFor TBS please refer to table 5.1.3.2-2 in 38.214" %N_info_quant_1
	raw_input()
	exit()
else:
	n = math.floor(math.log(N_info-24,2))-5
	N_info_quant = max(3840, math.pow(2,n)*math.ceil((N_info-24)/math.pow(2,n)))
	print "quantized intermediate number of information bits : %r\n" %N_info_quant


if Code_Rate <=0.25:
	C = math.ceil((N_info_quant+24)/3816)
	TBS = 8*C*math.ceil((N_info_quant+24)/(8*C))-24
	print "Code rate > 1/4 and TB size is : %r\n" %TBS
else:
	if N_info_quant > 8424:
		C = math.ceil((N_info_quant+24)/8424)
		TBS = 8*C*math.ceil((N_info_quant+24)/(8*C))-24
		Average_Througput = ((TBS*160/80)*1000)
		print "As N_info_quant > 8424 and Code rate > 1/4, TB size is : %r\n" %TBS
		print "Average throughput : %r bps" %Average_Througput
	else:
		TBS = 8*math.ceil((N_info_quant+24)/8)-24
		Average_Througput = ((TBS*160/80)*1000)
		print "As N_info_quant < 8424 and Code rate > 1/4,TB size is : %r\n" %TBS
		print "Average throughput : %r bps" %Average_Througput

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
