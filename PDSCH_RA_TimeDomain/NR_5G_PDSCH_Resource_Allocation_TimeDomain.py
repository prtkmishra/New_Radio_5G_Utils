""" Script to calculate Start and Length indicator value (SLIV)
for New Radio 5G Physical layer Downlink Shared Channel (PDSCH)
in time domain.
based on 3GPP 38.214 secton 5.1
"""

import math																# for floor function
import string															# for replace function

class TdResourceAllocation:
    start_symbol = 0
    length_value = 0
    # Start_Symbol = int(raw_input("Please enter the Start (S) Value> "))
    # Length_Value = int(raw_input("Please enter the Length (L) Value> "))

    def __init__(self, start_symbol, length_value):
        self.start_symbol = int(start_symbol)
        self.length_value = int(length_value)        

    def tdrscCalculator(self):
        if self.length_value <= 14-self.start_symbol:
            if self.length_value-1 <8:
                SLIV = 14*(self.length_value-1)+self.start_symbol
                return "\nThe SLIV is = " + str(SLIV)
                #print "\nSLIV in CRM command %r" %hex(SLIV)
            else:
                SLIV = 14*(14-self.length_value+1)+(14-1-self.start_symbol)
                return "\nThe SLIV is = " + str(SLIV)
                #print "\nSLIV in CRM command %r" %hex(SLIV)
        else:
            return "The Value of L does not satisfy '0<L<=14-S'\nPlease refer to 38.214 Section 5.1.2.1"
