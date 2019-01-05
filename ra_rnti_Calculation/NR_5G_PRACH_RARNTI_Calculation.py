###########################################################
# This util is to calculate RA-RNTI in NR5G
# Based on 38.321 and 38.211
# Currently limitation :
#                       Random access configurations for FR1 and unpaired spectrum
#                       only for NUL carrier
#                       Only for FR1 (30Khz)
#
###########################################################
import math
import pandas as pd
import os

# s_id
# t_id
# f_id

TOTAL_NUM_SLOTS_IN_ONE_SF = 20
SFN_WRAP_AROUND = 1024

class RaRntiCalculator:
    input_file_name = ""
    rat_type        = 0
    config_idx      = 0
    tdd_periodicity = 0
    prach_cfg_idx_list = []
    x = []
    y = []
    prach_duration_list = []
    starting_symbol_list = []
    sf_number =    []
    slot_num_sf = []
    
    def __init__(self, rat_type, config_idx, tdd_periodicity, input_file_name='./ra_rnti_Calculation/InputData/Input.xlsx'):
        self.rat_type = rat_type
        self.config_idx = int(config_idx)
        self.tdd_periodicity = int(tdd_periodicity)
        self.input_file_name = input_file_name
        for i in range(0,TOTAL_NUM_SLOTS_IN_ONE_SF):
             self.slot_num_sf.append(i)
    
    
    def calc_rarnti(self):
        """ Function to calculate ra rnti """
        
    def tdd_slot(self):
            tdd_periodicity_slot = (self.tdd_periodicity*2)-1
            valid_ra_slot = []
            for i in self.slot_num_sf:
                if i%tdd_periodicity_slot == 0:
                    valid_slots = self.slot_num_sf.pop(i-1)
                    valid_ra_slot.append(i)
            valid_ra_slot.remove(0)
            #print "\nValid RA slot number(s)",valid_ra_slot
        
    def fdd_slot(self):
        valid_ra_slot = []
        for i in self.sf_number:
            valid_slots = (2*i)-1
            valid_ra_slot.append(valid_slots)
            # #print "\nValid RA slot number(s)",valid_ra_slot
            #return str(valid_ra_slot)
        return valid_ra_slot
    
    def init_data_set(self):
        table_df = pd.DataFrame()
        config_idx_df = pd.DataFrame()
        column_name = ['PRACH_CFG_IDX', 'PREAMBLE_FRMT', 'X', 'Y', 'SF_NUM', 'START_SYM', 'PRACH_SLOT_SF', 'TD_PRACH_OCC', 'DUR']
        table_df = pd.read_excel(self.input_file_name, header=None, names = column_name ,skiprows=3)
        config_idx_df = table_df.loc[table_df['PRACH_CFG_IDX'] == self.config_idx]
        #print config_idx_df.head()
        
        self.prach_cfg_idx_list = table_df['PRACH_CFG_IDX'].values.tolist()
        self.x = table_df['X'].values.tolist()
        self.y = table_df['Y'].values.tolist()
        self.prach_duration_list = table_df['DUR'].values.tolist()
        self.starting_symbol_list = table_df['START_SYM'].values.tolist()
        self.sf_number = config_idx_df['SF_NUM'].values.tolist()
        print(self.sf_number)
        transStr = []
        if type(self.sf_number[0])!= int:
           try:
               transStr = str(self.sf_number[0]).split(',')
               transStr = [int(x) for x in transStr]
           except:
               transStr.append(int(self.sf_number[0]))
           print(transStr)
           self.sf_number = transStr

        '''
        if type(self.sf_number[0])!= int:
            self.sf_number = [s.encode('ascii', 'ignore') for s in self.sf_number]
            
            self.sf_number = [int(x.strip('\'')) for x in self.sf_number[0].split(',')]
        '''
        print("\nBelow is a list of valid prach SF:{}".format(self.sf_number))
        
    def calc_valid_ra_slot(self):
    
        finalRetVal = []
        """ To calculate valid ra slot where UE can 
            transmit RACH based on PRACH configuration index"""
        self.init_data_set()
        """ """
        prach_cfg_idx = self.prach_cfg_idx_list.index(self.config_idx)
        prach_duration = self.prach_duration_list.pop(prach_cfg_idx)
        starting_symbol = self.starting_symbol_list.pop(prach_cfg_idx)
        x_idx = self.x.pop(prach_cfg_idx)
        y_idx = self.y.pop(prach_cfg_idx)
        prach_strt_symbol = self.starting_symbol_list.pop(prach_cfg_idx)
        
        #print "\nFor Prach Config Index %i\nPrach duration = %i symbols \nPRACH Starting symbol = %i" %(self.config_idx, prach_duration,starting_symbol)
        valid_prach_sfn = []
        for sfn in range(0,SFN_WRAP_AROUND):
            if sfn%x_idx == y_idx:
                valid_prach_sfn.append(sfn)
        #print "\nBelow is a list of valid prach SFN\n",valid_prach_sfn
        #print "\nPrach starting symbol = ",prach_strt_symbol
        #print "Valid Subframes in the every valid SFN = ", self.sf_number
        if self.rat_type == "TDD":
            self.tdd_slot()
        else:
            finalRetVal = self.fdd_slot()
        return finalRetVal
