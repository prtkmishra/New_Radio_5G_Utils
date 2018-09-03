DL_Carrier_Freq = int(raw_input("DL_Carrier_Freq : " ))
Center_Freq_PA_Sep = int(raw_input("Center_Freq_PA_Sep : " ))
SCS = int(raw_input("Subcarrier Spacing : " ))
SSB_Offset_to_PA = int(raw_input("SSB_Offset_to_PA : " ))
SSB_SC_OFFSET = int(raw_input("SSB_SC_OFFSET : " ))

AbsoluteFrequencyPointA = ((DL_Carrier_Freq +((Center_Freq_PA_Sep*SCS)/100)))
Absolute_Freq_SSB_Start = (((AbsoluteFrequencyPointA*100)+(180*SSB_Offset_to_PA)+(15*SSB_SC_OFFSET))/100)
AbsoluteFrequencySSB = Absolute_Freq_SSB_Start+36

print "AbsoluteFrequencyPointA : ", AbsoluteFrequencyPointA
print "AbsoluteFrequencySSB : ", AbsoluteFrequencySSB