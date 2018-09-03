import math																# for floor function
import string															# for replace function
print "\nThis utility is for Resource Allocation Type-0 only\nPlease refer to 38.214 Section5.1.2.2.1"
P = int(raw_input("Enter value of P> "))
N_BWP_start = int(raw_input("Enter start PRB number of BWP > "))
N_BWP_size = int(raw_input("Enter the size of BWP> "))

Size_RBG_0 = (P-N_BWP_start)%P
Number_of_middle_RBGs = math.floor((N_BWP_size-Size_RBG_0)/P)
size_of_last_RBG = N_BWP_size - Size_RBG_0 - P*Number_of_middle_RBGs

if size_of_last_RBG > 0:
	Total_RBG = Number_of_middle_RBGs + 2
else:
	Total_RBG = Number_of_middle_RBGs + 1

bitmap_list = [1]*int(Total_RBG)
bitmap_string = ''.join(str(x) for x in bitmap_list)
print "\n \nThe size of the first RBG is %r" %Size_RBG_0
print "The number of RBGs in middle of size %r are %r" %(P,Number_of_middle_RBGs)
print "The size of the last RBG in the BWP is %r" %size_of_last_RBG
print "Total number of RBGs in the BWP is %r" %Total_RBG
new_bitmap = string.replace(bitmap_string,"," , "")
print "Bitmap to use = %r" %new_bitmap
raw_input()