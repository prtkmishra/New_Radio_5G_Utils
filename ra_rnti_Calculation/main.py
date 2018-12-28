from NR_5G_PRACH_RARNTI_Calculation import RaRntiCalculator as ra_calc
import os
rat_type = raw_input("Is RAT Type TDD or FDD > ").upper()
config_idx = int(raw_input("INPUT: Prach Config Index > "))
tdd_periodicity = int(raw_input("INPUT: TDD periodicity in ms > "))
if __name__ == "__main__":
    
    """ This constructor should be initialised with 
        arg1 : RAT_TYPE valid values: "FDD", "TDD" 
        arg2 : PRACH config index valid values: "0:255" 
        arg3 : TDD periodicity valid values: "please refer to 3GPP spec 38.213" 
        arg4 : In case user wants to give own file name, else leave blank" 
    """
    ra_calc_obj = ra_calc(rat_type,config_idx,tdd_periodicity)
    ra_calc_obj.calc_valid_ra_slot()