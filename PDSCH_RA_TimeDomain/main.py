from NR_5G_PDSCH_Resource_Allocation_TimeDomain import TdResourceAllocation as td_calc
import os

start_symbol = raw_input("Value of Start Symbol >  ")

length_value = raw_input("value of PDSCH symbol in Length ")

if __name__ == "__main__":
    
    """ This constructor should be initialised with 
        arg1 : Valid values of PDSCH Start Symbols 
        arg2 : Valid values of PDSCH length in symbols" 
     """
    td_calc_obj = td_calc(start_symbol,length_value)
    td_calc_obj.tdrscCalculator()
