# Function to produce final result when values in Reg0_46 and Reg6_46 become equal

def meeta():
    global stall_withforwarding
    print ('\n')
    print("The Given Inputs are ", ANI_46,"and",NIK_46)
    stall_withforwarding = stall_withforwarding + 1
    print("Dot Product: ", Reg1_46)
    print ("Stalls With Forwarding",stall_withforwarding) 
    print("This is Dot Product Using Forwarding to Reduce Stalls")
    exit()

# INPUTS
ANI_46 = "014535846"
NIK_46 = "014489852"

Reg0_46=0 # First register in MIPS is 0

Reg1_46=0 # Sum of the values are stored

Reg2_46=[] # Reg2_46 and Reg3_46 store the first and second input
Reg3_46=[] 

Reg4_46=0*1 # Reg4_46 and Reg5_46 indicate the next value
Reg5_46=0*1 

Reg6_46 = int(len(ANI_46)) 

stall_withforwarding=0

for value in ANI_46:
    Reg2_46.append(value) 

for value in NIK_46:
    Reg3_46.append(value) 

# Execution of Logic
Reg1_46=(Reg0_46 + Reg0_46)                       
while(1):
 if Reg6_46==Reg0_46:                           
    meeta()
 else:
    if(Reg2_46):                          
        True

    if(Reg2_46[Reg4_46])!="":                      
        if(Reg3_46):                  
            True
    
    if len(Reg2_46)>=0:       
        if(Reg3_46[Reg5_46])!="":                   
            if(Reg2_46):                  
                True                        

    if(Reg2_46[Reg4_46]):                      
        if len(Reg3_46)>=0:                 
            if(Reg3_46[Reg5_46])!="":            
                if(Reg2_46):              
                    True                            
                            
    if(Reg2_46[Reg4_46]):                   
        temp_46 = float(Reg2_46[Reg4_46])        
        temp_46 = temp_46 + 0     
        if float(Reg3_46[Reg5_46]) >= 0:               
            stall_withforwarding=stall_withforwarding+1               
            pass   # Stall occurs and hence No Operation (NOP)      
            

    if(Reg3_46[Reg5_46]):                  
        temp1_46 = float(Reg3_46[Reg5_46])        
        temp_46 = temp1_46 + 0 
        if len(Reg3_46) >= 0:                   
            if(Reg3_46[Reg5_46])!="":               
             True

    if float(Reg3_46[Reg5_46])>=0:                
            stall_withforwarding=stall_withforwarding+1               
            pass                       
    
                                                                    
    if(Reg3_46[Reg5_46]):                      
        if(Reg2_46[Reg4_46])!="":                      
            True        
        Reg2_46[Reg4_46] = float(Reg2_46[Reg4_46])*float(Reg3_46[Reg5_46])  
        Reg1_46 = Reg1_46 + float(Reg2_46[Reg4_46])           
        Reg1_46 = Reg1_46                     
        print(Reg2_46[0:Reg4_46])

    Reg4_46=Reg4_46+1                           #Increment counter addiu $r3 $r3 #4
    Reg5_46=Reg5_46+1                           #Increment counter addiu $r5 $r5 #4 
    Reg6_46=Reg6_46-1