########################################################################################################################################
# New Radio 5G Physical layer utilities for test driven development
# Some of the scripts have been ported to flask api and rendered using AWS EC2 instance. 
# work in progress for remaining utilities
########################################################################################################################################

3GPP_NR_5G_PDSCH_Resource_Allocation_Type1.py 
  Description : This utility is to generate Resource Index Value (RIV) for RA Type -1
  Usage : Direct script execution

3GPP_NR_5G_PDSCH_Resource_Allocation_Type_0.py
  Desciption : This Utility is to generate frequency domain resource assignment bitmap for RA type-0
  usage : Direct script execution
  
3GPP_NR_5G_PDSCH_Transport_Block_Size.py
  Description : This utility is to calculate PDSCH/ PUSCH Transport Block size with intermediate N_info values
  Usage : Direct script execution. Porting to flask api in progress
 
3GPP_NR_5G_PUCCH_Resource_Index.py
  Desciption : This utility is to calculate dedicated  PUCCH resource index
  Usage : Direct script execution
  
3GPP_NR_5G_PUSCH_Resource_Allocation_TimeDomain.py
  Description : This utility is to calculate Start and length indicator value (SLIV) for PUSCH
  Usage : Direct script execution
  
PDSCH_RA_TimeDomain
  Description : This utility is to calculate Start and length indicator value (SLIV) for PDSCH
  Usage : 1. main.py 
          2. access http://52.91.0.194:5001/

3GPP_NR_5G_SSB_Indexes.py
  Description : This utility is to calculate the start symbol index of SSB in NR5G
  usage : Direct script execution
  
SUM_KR_LDPC
  Description : This utility is to calculate sum of Kr in LDPC for PUCCH sequence
  Usage : 1. main.py
          2. access http://52.91.0.194:5001/

ra_rnti_Calculation
  Description : This utility is to calculate ra-rnti based on mandatory parameters
  Usage : 1. main.py 
          2. access http://52.91.0.194:5001/
