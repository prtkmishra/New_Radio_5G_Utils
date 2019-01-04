"""
This util is to calculate O_ack value for HARQ Ack/Nack over PUSCH.
This util can be useful in calculating resources used for
HARQ over PUSCH
Please refer to 38.211 for details
"""

import math
import numpy as np


class ComputeSumKrLdpc:
    """calculate TB CRC length for selected LDPC graph """
    graph  = "" 
    TbSize = 0
    O_ack  = 0
    Beta_Offset = 0
    N_rb = 0
    N_Ul_Len = 0 
    Alpha = 0    
    Z_values = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,22,24,26,28,30,32,36,40,44,48,52,56,60,64,72,80,88,96,104,112,120,128,144,160,176,192,208,224,240,256,288,320,352,384]
    
    def __init__(self, graph, TbSize, O_ack, Beta_Offset, N_rb, N_Ul_Len, Alpha):
        self.graph = graph
        self.TbSize = TbSize
        self.O_ack = O_ack
        self.Beta_Offset = Beta_Offset
        self.N_rb = N_rb
        self.N_Ul_Len = N_Ul_Len
        self.Alpha = Alpha

    def k_cb(self):   
        if self.graph == 1:# LDPCgraph1
            Kcb = 8448
        else: # LDPCgraph2
            Kcb = 3840
        return Kcb

    def tb_crc_len(self):

        if self.TbSize > 3824:
            TbCrcLength = 24
        else:
            TbCrcLength = 16
        B = self.TbSize+ TbCrcLength
        return B
            
    def calc_b_prime(self):
        B = self.tb_crc_len()
        Kcb = self.k_cb()
        Bprime = 0
        if B <= Kcb:
            L = 0
            C = 1
            Bprime = B
        else:
            L = 24
            C = int(math.ceil(B/(Kcb-L)))
            Bprime = B+C*L
        return (Bprime, C)
        Kprime = Bprime / C * np.ones((1,C))
        #return "The value of Kprime is "+Kprime


    def calc_Kb(self):
        B = self.tb_crc_len()
        if self.graph == 1:# LDPCgraph1
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
        return Kb


    def calc_z(self):
        Kb = int(self.calc_Kb())
        Bprime = 0
        C = 0
        (Bprime, C) = self.calc_b_prime()
        for Zc in self.Z_values:
            Z = Kb*Zc
            if Z >= (math.ceil((Bprime/C)/Kb)):
                 break
        return Z

    def calc_k(self):
        Z = self.calc_z()
        if self.graph == 1:# LDPCgraph1
            K = 22*Z
        else: # LDPCgraph2
            K = 10*Z
        return K

    def sum_kr(self):
        Bprime, C = self.calc_b_prime()
        K = self.calc_k()
        self.tb_crc_len()
        self.k_cb()
        sumKr = C*K
        return "sumKr is "+str(sumKr)
        A = math.ceil(((self.O_ack+0)*self.Beta_Offset*(12*self.N_rb*(self.N_Ul_Len-1)))/sumKr)
        return ((self.O_ack+0)*self.Beta_Offset*(12*self.N_rb*(self.N_Ul_Len-1)))
        return A
        Scaling = float(self.Alpha)
        B = math.ceil(Scaling*(12*self.N_rb*(self.N_Ul_Len-3)))
        return B
        Q_ack = min(A,B)
        return "\n number of REs per symbol : "+(12*self.N_rb)
        return "\n Q_ack value is : "+Q_ack
