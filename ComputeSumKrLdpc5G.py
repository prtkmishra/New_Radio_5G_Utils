##############################################################
# This util is to calculate O_ack value for HARQ Ack/Nack over
# PUSCH.
# This util can be useful in calculating resources used for
# HARQ over PUSCH
# Please refer to 38.211 for details
##############################################################
import math
import numpy as np


graph  = raw_input("LDPCgraph1 or LDPCgraph2? > ")
TbSize = float(raw_input("TBSize > "))
O_ack  =  float(raw_input("number of HARQ-ACK bits > "))
Beta_Offset = float(raw_input("Beta_Offset > "))
N_rb = float(raw_input("number of UL RBs > "))
N_Ul_Len = float(raw_input("Length of ULSCH in Symbols > "))
Alpha = raw_input("Scaling(Alpha) > ")


if graph == 1:# LDPCgraph1
    Kcb = 8448
else: # LDPCgraph2
    Kcb = 3840


if TbSize > 3824:
    TbCrcLength = 24
else:
    TbCrcLength = 16


B = TbSize+ TbCrcLength

if B <= Kcb:
    L = 0
    C = 1
    Bprime = B
else:
    L = 24
    C = int(math.ceil(B/(Kcb-L)))
    Bprime = B+C*L

Kprime = Bprime / C * np.ones((1,C))

if graph == 1:# LDPCgraph1
    Kb = 22
else: # LDPCgraph2
    if B > 640:
        Kb = 10
    elif B > 560:
        Kb = 9
    elif B > 192:
        Kb = 8
    else:
        Kb = 6

print "Kb is %i" %Kb
Z_values = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,22,24,26,28,30,32,36,40,44,48,52,56,60,64,72,80,88,96,104,112,120,128,144,160,176,192,208,224,240,256,288,320,352,384]

for Zc in Z_values:
	Z = Kb*Zc
	if Z >= (math.ceil(Bprime/C)/Kb):
		# print "Zc is %i" %Zc
		break

if graph == 1:# LDPCgraph1
    K = 22*Z
else: # LDPCgraph2
    K = 10*Z

print "K is %i" %K
print "\n Number of Codeblocks : %i" %C
sumKr = C*K
print "sumKr is %i" %sumKr

A = math.ceil(((O_ack+0)*Beta_Offset*(12*N_rb*(N_Ul_Len-1)))/sumKr)
print ((O_ack+0)*Beta_Offset*(12*N_rb*(N_Ul_Len-1)))
print A
Scaling = float(Alpha)
B = math.ceil(Scaling*(12*N_rb*(N_Ul_Len-3)))

print B

Q_ack = min(A,B)
print "\n number of REs per symbol : %i" %(12*N_rb)
print "\n Q_ack value is : %i" %Q_ack
