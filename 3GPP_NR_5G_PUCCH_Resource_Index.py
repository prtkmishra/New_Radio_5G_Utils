##########################################################################
# This utility is used to calculate dedicated  PUCCH resource index
# Based on 38.213 9.2.3
##########################################################################

import math


resourceList = int(raw_input("resourceList < "))
PUCCH_resource_indicator = int(raw_input("PUCCH_resource_indicator < "))
number_of_CCEs_in_CORESET = int(raw_input("number_of_CCEs_in_CORESET < "))
index_of_a_first_CCE = int(raw_input("index_of_a_first_CCE < "))

if resourceList > 8:
    if PUCCH_resource_indicator < resourceList%8:
        rPUCCH = math.floor((index_of_a_first_CCE*math.ceil(resourceList/8))/number_of_CCEs_in_CORESET)+(PUCCH_resource_indicator*math.ceil(resourceList/8))

    else:
        rPUCCH = math.floor((index_of_a_first_CCE*math.ceil(resourceList/8))/number_of_CCEs_in_CORESET)+(PUCCH_resource_indicator*math.ceil(resourceList/8)) + (resourceList%8)
else:
        print "For PUCCH resource refer to Table Table 9.2.3-2 in 38.213"
        
print "PUCCH resource index rPUCCH = %r" %rPUCCH