"""
Script to calculate Start and Length indicator value (SLIV)
for New Radio 5G Physical layer Downlink Shared Channel (PDSCH)
in time domain.
based on 3GPP 38.214 secton 5.1
"""

import math																# for floor function
import string															# for replace function

class TdResourceAllocation:
    print "\nThis utility is for Resource Allocation in Time domain only\nPlease refer to 38.214 Section5.1.2.1\n"
    start_symbol = 0
    length_value = 0
    # Start_Symbol = int(raw_input("Please enter the Start (S) Value> "))
    # Length_Value = int(raw_input("Please enter the Length (L) Value> "))

    def __init_(self, start_symbol, length_value):
        self.start_symbol = start_symbol
        self.length_value = length_value        

if Length_Value <= 14-Start_Symbol:
	if Length_Value-1 <8:
		SLIV = 14*(Length_Value-1)+Start_Symbol
		print "\nThe SLIV is %r" %SLIV
		print "\nSLIV in CRM command %r" %hex(SLIV)
	else:
		SLIV = 14*(14-Length_Value+1)+(14-1-Start_Symbol)
		print "\nThe SLIV is %r" %SLIV
		print "\nSLIV in CRM command %r" %hex(SLIV)
else:
	print "The Value of L does not satisfy '0<L<=14-S'\nPlease refer to 38.214 Section 5.1.2.1"
#raw_input()
