from ComputeSumKrLdpc5G import ComputeSumKrLdpc as sumldpc
import os

#graph  = input("LDPCgraph1 or LDPCgraph2? > ")
#TbSize = float(input("TBSize > "))
#O_ack  =  float(input("number of HARQ-ACK bits > "))
#Beta_Offset = float(input("Beta_Offset > "))
#N_rb = float(input("number of UL RBs > "))
#N_Ul_Len = float(input("Length of ULSCH in Symbols > "))
#Alpha = input("Scaling(Alpha) > ")

graph = 1
TbSize = 24
O_ack = 2
Beta_Offset = 4
N_rb = 1
N_Ul_Len = 10
Alpha = 1

if __name__ == "__main__":
    
    """ This constructor should be initialised with 
        arg1 : Valid value of graph (1,2) 
        arg2 : Valid value of TB SIZE in numeric
        arg3 : Valid value of number of HARQ bits
        arg4 : Valid value of Beta Offset 
        arg5 : Valid value of  number of UL RBs
        arg6 : Valid value of length of ULSCH in Symbols
        arg7 : Valid value of Alpha
     """
    sumldpc_obj = sumldpc(graph, TbSize, O_ack, Beta_Offset, N_rb, N_Ul_Len, Alpha)
    sumldpc_obj.sum_kr()
