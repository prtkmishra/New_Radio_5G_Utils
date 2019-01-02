from NR_5G_PDSCH_Transport_Block_Size import TBCalculator 

import os

if __name__ == "__main__":
    """below variables to be initialised for TB calculation """
    MCS_Table = '64QAM'
    MCS = 20
    numlayers = 1
    Nsh_Sym = 2
    NPRB_DMRS = 1
    Overhead = 1
    Total_prbs = 2
    
    TBCalcObj = TBCalculator(MCS_Table, MCS, numlayers, Nsh_Sym, NPRB_DMRS, Overhead, Total_prbs)
    TBCalcObj.TBCalc()
