# When values in Reg6_46 and Reg0_46 become equal it displays final output
def meeta():
    global stall_withoutforwarding
    print ('\n')
    print ('Student IDs are', ANI_46, 'and', NIK_46)
    stall_withoutforwarding = stall_withoutforwarding + 3  # 3 INSTRUCTION DELAY
    print ('Dot Product: ', Reg1_46)
    print ('Stalls Without Forwarding:', stall_withoutforwarding)
    print ('This is Dot Product of given inputs Without Forwarding\n')
    exit()

# INPUTS
ANI_46 = '014535846'
NIK_46 = '014489852'

Reg0_46 = 0        # First register in MIPS is 0
Reg1_46 = 0        # Sum of the values are stored
Reg2_46 = []       # Reg2_46 and Reg3_46 store the first and second input
Reg3_46 = []       
Reg4_46 = 0 * 1    # Reg4_46 and Reg5_46 indicate the next value
Reg5_46 = 0 * 1    

Reg6_46 = int(len(ANI_46)) 
stall_withoutforwarding = 0

for value in ANI_46:
    Reg2_46.append(value)

for value in NIK_46:
    Reg3_46.append(value)

# Execution of Logic

Reg1_46 = Reg0_46 + Reg0_46  # Adds the values in Register0
while 1:
    if Reg6_46 == Reg0_46:  # If value in Reg6_46 and R0 are equal then it'll produce output by calling function
        meeta()
    else:
        if Reg2_46:
            True

        if Reg2_46[Reg4_46] != '':  
            if Reg3_46:  
                True

        if len(Reg2_46) >= 0:  
            if Reg3_46[Reg5_46] != '':  
                if Reg2_46:  
                    True

        if Reg2_46[Reg4_46]:  
            if len(Reg3_46) >= 0:  
                stall_withoutforwarding = stall_withoutforwarding + 1
                pass  # Stall occurs and hence No Operation (NOP)

        if Reg2_46[Reg4_46]:  
            temp_46 = float(Reg2_46[Reg4_46])
            temp_46 = temp_46 + 0
            if float(Reg3_46[Reg5_46]) >= 0:  
                stall_withoutforwarding = stall_withoutforwarding + 1
                pass  

        if Reg3_46[Reg5_46]: 
            temp1_46 = float(Reg3_46[Reg5_46])
            temp1_46 = temp1_46 + 0
            stall_withoutforwarding = stall_withoutforwarding + 1
            pass  

        if Reg3_46[Reg5_46] != '':  
            if Reg2_46: 
                True

        if len(Reg3_46) >= 0:  
            stall_withoutforwarding = stall_withoutforwarding + 1
            pass  

        if float(Reg3_46[Reg5_46]) >= 0:  
            stall_withoutforwarding = stall_withoutforwarding + 1
            pass  

        if Reg3_46[Reg5_46]:  
            Reg2_46[Reg4_46] = float(Reg2_46[Reg4_46]) * float(Reg3_46[Reg5_46])
            stall_withoutforwarding = stall_withoutforwarding + 1
            pass  

        if Reg3_46[Reg5_46] != '':  
            if Reg2_46[Reg4_46] != '':  
                Reg1_46 = Reg1_46 + float(Reg2_46[Reg4_46])  
                Reg1_46 = Reg1_46  
        Reg4_46 = Reg4_46 + 1  
        Reg5_46 = Reg5_46 + 1 

        if Reg6_46:  
            stall_withoutforwarding = stall_withoutforwarding + 1
            pass  
        if Reg6_46 != '': 
            stall_withoutforwarding = stall_withoutforwarding + 1
            pass  

        if len(str(Reg6_46)) >= 0:  
            if Reg6_46 == Reg6_46: 
                Reg6_46 = Reg6_46 - 1  
        print (Reg2_46[0:Reg4_46])