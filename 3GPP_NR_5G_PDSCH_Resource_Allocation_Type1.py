import math
from sys import exit
print "This script is to calculate Resource Allocation Type 1 Bits"
Total_RBs = int(raw_input("Number of total RBs : "))
RB_len = int(raw_input("Length of RB/UE : "))
RB_start = int(raw_input("Start of RB/UE : "))
bit_len = math.ceil(math.log(RB_len*(RB_len+1)/2,2))
print bit_len
bitmap_list = [1]*int(bit_len)
bitmap = ''.join(str(x) for x in bitmap_list)
# print bitmap


## RIV not for test plan
if (RB_len-1)<=math.floor(Total_RBs/2):
	RIV = Total_RBs*(RB_len-1)+RB_start
	# print "case 1"
else:
	RIV = Total_RBs*(Total_RBs-RB_len+1)+(Total_RBs-1-RB_start)
	# print "case 2"
print "RIV: %i" %RIV
def dec_to_bin(x):
    return int(bin(x)[2:])
print "Decimal of RIV : ", dec_to_bin(RIV)
print "Hex value for CRM command :", hex(RIV)

raw_input()