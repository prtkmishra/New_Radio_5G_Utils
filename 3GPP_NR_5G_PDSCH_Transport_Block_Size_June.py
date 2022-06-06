"""
****************************************************************************
@Author     Prateek M

@file       3GPP_NR_5G_PDSCH_Transport_Block_Size_June.py

@brief      This utility is for calculating PDSCH TB size for NR5G (June Spec)
****************************************************************************
"""

# ***************************************************************************
#                       Standard library imports
# ***************************************************************************
import math
from sys import exit
# ***************************************************************************
#                      Related third party imports
# ***************************************************************************

# ***************************************************************************
#                Local application/library specific imports
# ***************************************************************************
IMCS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
LAYERS = [1,2,3,4,5,6,7,8]
XOVERHEAD = [0, 6, 12, 18]
NRB_SC = 12
class PDSCHTBSizeCalc():
	""" 
	Functions related to NR PDSCH TB size calculations,
	Methods: tbSizeCalculator(), ldpcGraph(),
	"""
	print("Please use the appropriate table in the script for 64QAM and 256QAM")
	def __init__(self) -> None:
		pass

	def tbSizeCalculator(self, MCS_Table=0, MCS=1, numlayers=1, Nsh_Sym=13, NPRB_DMRS=12, Overhead=0, Total_prbs=10):
		"""
		Function to calculate NR PDSCH/ PUSCH TB Size
		Inputs: 
			tbSizeCalculator(self, MCS_Table, MCS, numlayers, Nsh_Sym, NPRB_DMRS, Overhead, Total_prbs),
			MCS_Table = [0,1] i.e. 64QAM, 256QAM,
			MCS = [0:28],
			numlayers = [1:4],
			Nsh_Sym = [1:13] i.e. number of symbols allocated for PDSCH in a slot,
			NPRB_DMRS = [] i.e. number of REs reserved for DMRS in a PRB. Currently by default 12 for DMRS ADD POS=0,
			Overhead = [] i.e. Xoh is usually 0,
			Total_prbs = [1:273] i.e. Number of PRBs allocation for the UE
		Outputs:
			code rate
			Intermediate number of information bits
			N_info_quant
			TBSize
			Average Throughput (For reference only)
		"""
		if MCS_Table == 0:
			print('\nTable used is 64QAM')
			Qm = [2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,2,4,6]
			R = [120,157,193,251,308,379,449,526,602,679,340,378,434,490,553,616,658,438,466,517,567,616,666,719,772,822,873,910,948]
		else:
			print('\nTable used is 256QAM')
			Qm = [2,2,2,2,2,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,8,8,8,8,8,8,8,8,2,4,6,8]
			R = [120,193,308,449,602,378,434,490,553,616,658,466,517,567,616,666,719,772,822,873,682.5,711,754,797,841,885,916.5,948]
		
		MCS_Index = IMCS.index(MCS)
		Modulation_order = Qm.pop(MCS_Index)
		Code_Rate = R.pop(MCS_Index)/1024.00000
		print("\nThe code rate used is %r and modulation order is %r" %(Code_Rate, Modulation_order))
					
		nre_prb = (NRB_SC*Nsh_Sym)-NPRB_DMRS-Overhead
		NRE = min(156,nre_prb)*Total_prbs
		N_info = NRE*Code_Rate*Modulation_order*numlayers
		print("\nIntermediate number of information bits are %r" %N_info)
		
		if N_info <= 3824:
			n = max(3, math.floor(math.log(N_info,2))-6)
			N_info_quant_1 = max(24,math.pow(2,n)*math.floor(N_info/math.pow(2,n)))
			print("\nQuantized intermediate number of information bits : %r\nFor TBS please refer to table 5.1.3.2-2 in 38.214" %N_info_quant_1)
			exit()
		else:
			n = math.floor(math.log(N_info-24,2))-5
			N_info_quant = math.pow(2,n)*round((N_info-24)/math.pow(2,n))
			print("\nQuantized intermediate number of information bits : %r" %N_info_quant)
					
		if Code_Rate <=0.25:
			C = math.ceil((N_info_quant+24)/3816)
			TBS = 8*C*math.ceil((N_info_quant+24)/(8*C))-24
			print("\nCode rate > 1/4 and TB size is : %r\n" %TBS)
		else:
			if N_info_quant > 8424:
				C = math.ceil((N_info_quant+24)/8424)
				TBS = 8*C*math.ceil((N_info_quant+24)/(8*C))-24
				Average_Througput = ((TBS*160/80)*1000)
				print("\nAs N_info_quant > 8424 and Code rate > 1/4, TB size is : %r" %TBS)
				print("\nAverage throughput : {} bps" .format(str(Average_Througput)))
			else:
				TBS = 8*math.ceil((N_info_quant+24)/8)-24
				Average_Througput = ((TBS*160/80)*1000)
				print("\nAs N_info_quant < 8424 and Code rate > 1/4,TB size is : %r" %TBS)
				print("\nAverage throughput : {} bps" .format(str(Average_Througput)))
		return Modulation_order, TBS
	
	def ldpcGraph(self,Modulation_order, TBS):
		if TBS <= 292:
			print("LDPCgraph2")
		else:
			print("TBS > 292")
		if TBS <= 3824:
			if Modulation_order <= (67/100):
				print("LDPCgraph2")
			else:
				print("Modulation_order is > 0.67")
		else:
			print("TBS is > 3824")
		
		if Modulation_order <= (25/100):
			print("LDPCgraph2")
		else:
			print("LDPCgraph1")


if __name__ == "__main__":
	tbsize_calc = PDSCHTBSizeCalc()
	tbsize_calc.tbSizeCalculator(MCS_Table=0, MCS=9, numlayers=1, Nsh_Sym=6, NPRB_DMRS=12, Overhead=0, Total_prbs=10)