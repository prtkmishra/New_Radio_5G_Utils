# import math																# for floor function
import string															# for replace function
print "\nThis utility is for Resource Allocation in Time domain only\nPlease refer to 38.214 Section5.1.2.1\n"
# Time_Domain_Resource_Index = int(raw_input("Time_Domain_Resource_Index in DCI(3bits)> ")) 
# PDSCH_Mapping_Type = raw_input("A or B > ").upper()

# if PDSCH_Mapping_Type == "A":
	# print "Valid start(S) value {0,1,2,3} for SLIV\nValid Lenth(L) value {10,11,12,13,14}\n"
# else:
	# print "Valid start(S) value {0,1,2,3,4,5,6,7,8,9,10,11,12} for SLIV\nValid Length(L) value {2,4,7}\n"

Start_Symbol = int(raw_input("Please enter the Start (S) Value> "))
Length_Value = int(raw_input("Please enter the Length (L) Value> "))
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
raw_input()