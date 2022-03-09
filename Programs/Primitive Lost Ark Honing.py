#PYTHON TIME
import random
import timeit
def _sum(arr):
    sum =0
    for i in arr:
        sum += i
    return(sum)

def print2darray(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()


NumofIterations = 1000000


### COST ###
#UPDATE THESE
CrystalToGold = 806/95

DestructionStonesCost = 108 / 10      # Destruction Stone Crystals
GuardianStoneCost = 65 / 10           # Guardian Stone Crystals  
HonorLeapStonesCost = 213             # Honor Leapstones
SolarGraceCost = 75                   # Solar Grace
#SolarGraceCost = CrystalToGold * 80 / 20 #Crystal Price
SolarBlessingCost = 287               # Solar Blessing
SolarProtectionCost = 694             # Solar Protection

HoneLVL = int(input("Enter Item Hone LVL Target: "))
ArmOrWeap = input("(W)eapon or (A)rmor: ")


if HoneLVL == 7:
    ChanceToHone = 0.60
    NumOfDestructionStones = 250
    NumOfGuardianStones = 156
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 8
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 4
    SolarGraceBenefit = 0.0167
    SolarBlessingBenefit = 0.03333
    SolarProtectionBenefit = 0.1
elif HoneLVL == 8:
    ChanceToHone = 0.45
    NumOfDestructionStones = 258
    NumOfGuardianStones = 156
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 8
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 4
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 9:
    ChanceToHone = 0.30
    NumOfDestructionStones = 258
    NumOfGuardianStones = 156
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 8
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 4
    SolarGraceBenefit = 0.0084
    SolarBlessingBenefit = 0.0167
    SolarProtectionBenefit = 0.05
elif HoneLVL == 10:
    ChanceToHone = 0.30
    NumOfDestructionStones = 320
    NumOfGuardianStones = 192
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 10
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 6
    SolarGraceBenefit = 0.0084
    SolarBlessingBenefit = 0.0167
    SolarProtectionBenefit = 0.05
### Experimental Benefits ###
elif HoneLVL == 11:
    ChanceToHone = 0.30
    NumOfDestructionStones = 320
    NumOfGuardianStones = 192
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 10
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 6
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 12:
    ChanceToHone = 0.30
    NumOfDestructionStones = 320
    NumOfGuardianStones = 192
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 10
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 6
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 13:
    ChanceToHone = 0.15
    NumOfDestructionStones = 380
    NumOfGuardianStones = 228
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 10
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 6
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 14:
    ChanceToHone = 0.15
    NumOfDestructionStones = 380
    NumOfGuardianStones = 228
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 12
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 6
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 15:
    ChanceToHone = 0.1
    NumOfDestructionStones = 380
    NumOfGuardianStones = 228
    if ArmOrWeap == "W":
        NumOfHonorLeapStones = 12
    elif ArmOrWeap == "A":
        NumOfHonorLeapStones = 6
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
else:
    print("Wrong")
    exit()  
if ArmOrWeap == "A" or ArmOrWeap == "W":
    NumOfDestructionStones = NumOfGuardianStones
else:
    print("Bro why", ArmOrWeap)
    exit()
PityChance = ChanceToHone * 0.1
### MAX HELP ITEMS ###
MaxSolarGrace = 12
MaxSolarBlessing = 6
MaxSolarProtection = 2

### ARRAY DECLARATIONS ###
#Attempts = []
#AttemptsforAVG = []
#Costs = []
#SolarHelp = []
LowestCost = []


### Which Help? ###
UserHelp = input("AYO choose (G)race, (B)lessing, (P)rotection, or (N)one: ")
if UserHelp == "G":
    MaxHelp = MaxSolarGrace
    HelpType = "Grace"
elif UserHelp == "B":
    MaxHelp = MaxSolarBlessing
    HelpType = "Blessing"
elif UserHelp == "P":
    MaxHelp = MaxSolarProtection
    HelpType = "Protection"
elif UserHelp == "N":
    MaxHelp = 0
else:
    exit()

start = timeit.default_timer()
print(str(HoneLVL) + ArmOrWeap, HelpType)
print("Attempt #", "\tHelp Used")
for z in range(0, 15):
    nut = False
    Attempts = []
    AttemptsforAVG = []
    Costs = []
    SolarHelp = []
    for y in range(0, MaxHelp+1):
        UsedSolarGrace = 0
        UsedSolarBlessing = 0
        UsedSolarProtection = 0
        if UserHelp == "G":
            UsedSolarGrace = y
            UsedBenefit = SolarGraceBenefit
            NumUsed = UsedSolarGrace
        elif UserHelp == "B":
            UsedSolarBlessing = y
            UsedBenefit = SolarBlessingBenefit
            NumUsed = UsedSolarBlessing
        elif UserHelp == "P":
            UsedSolarProtection = y
            UsedBenefit = SolarProtectionBenefit
            NumUsed = UsedSolarProtection
        elif UserHelp == "N":
            UsedBenefit = 0
            NumUsed = 0
        MaxMaxHelp = -1
        TotalPityChance = z*PityChance
        ArtisanEnergy = ((z * ChanceToHone) + (SolarGraceBenefit * _sum(LowestCost))) * 0.465
        PotentialArtisan = (ChanceToHone + (UsedBenefit * y) + TotalPityChance) * 0.465
        if ArtisanEnergy + PotentialArtisan >= 1:
            MaxMaxHelp = y
            UsedBenefit = y
        elif ArtisanEnergy >= 1:
            MaxMaxHelp = y - 1
        for x in range(1, NumofIterations):
            TotalHelp = (SolarGraceBenefit * UsedSolarGrace) + (SolarBlessingBenefit * UsedSolarBlessing) + (SolarProtectionBenefit * UsedSolarProtection)
            HelpCost = (UsedSolarGrace * SolarGraceCost) + (UsedSolarBlessing * SolarBlessingCost) + (UsedSolarProtection * SolarProtectionCost)
            passfail = False
            NumofAttempts = 0
            TotalCost = DestructionStonesCost * NumOfDestructionStones + HonorLeapStonesCost * NumOfHonorLeapStones + HelpCost
            if z == 0:
                ArtisanEnergy = 0
            else:
                ArtisanEnergy = ((z * ChanceToHone) + (SolarGraceBenefit * _sum(LowestCost))) * 0.465
            PityChance = 0
            #MaxMaxHelp = -1
            #for i in range(0, MaxHelp+1):
            ##    TotalPityChance = z*PityChance
             #   PotentialArtisan = (ChanceToHone + (UsedBenefit * i) + TotalPityChance) * 0.465
             #   if ArtisanEnergy + PotentialArtisan >= 1:
             #       MaxMaxHelp = i
          
            while passfail == False:
                NumofAttempts += 1

                if (NumofAttempts > 1):
                    if random.random() >= ChanceToHone + TotalHelp + PityChance:
                        ArtisanEnergy += (ChanceToHone + (UsedBenefit * NumUsed) + PityChance) *0.465              
                        if ArtisanEnergy >= 1:
                            #print("pity")
                            NumofAttempts += 1
                            passfail = True
                    else:
                        passfail = True

                else:
                    
                    if random.random() >= ChanceToHone + TotalHelp:
                        ArtisanEnergy += (ChanceToHone + (UsedBenefit * NumUsed) + PityChance) * 0.465
                                    
                        if ArtisanEnergy >= 1:
                            NumofAttempts += 1
                            passfail = True
                    else:
                        passfail = True

            TotalCost *= NumofAttempts
            ###Debugging Purposes ###
            #print("Help Number: " ,y)
            #print("Final Cost: ", TotalCost)
            #print("Number of Attempts: ", NumofAttempts)
            ###
            Attempts.append(NumofAttempts)
            Costs.append(TotalCost)
        #if y == MaxMaxHelp:
        #    nut = True
        #    break

        ###Debugging Purposes ###
        #print("Help used", y)
        #print("Number of Iterations: ", NumofIterations)
        #print("Average Number of Attempts: ", _sum(Attempts) / len(Attempts))
        #print("Average Cost: ", _sum(Costs) / len(Costs))
        ###
        ArtisanEnergy = (((z) * ChanceToHone) + (SolarGraceBenefit * _sum(LowestCost))) * 0.465
        #print(ArtisanEnergy)

        SolarHelp.append(_sum(Costs) / len(Costs))
        AttemptsforAVG.append(_sum(Attempts) / len(Attempts))
        if ArtisanEnergy >= 1:
            nut = True
            LowestCost.append(SolarHelp.index(min(SolarHelp)))
            break
    if nut == True:
        LowestCost.append(MaxMaxHelp)
    else:
        LowestCost.append(SolarHelp.index(min(SolarHelp)))

    #print("Solar Help", "\tAverage Cost", "\tAverage Number of Attempts")
    #for i in SolarHelp:
    #    print(SolarHelp.index(i), "\t \t" , "%.2f"  %i, "\t" , "%.3f" %AttemptsforAVG[SolarHelp.index(i)])

    #print( "%.2f" % min(SolarHelp), "\t",SolarHelp.index(min(SolarHelp)), "\t\t%.3f" % ArtisanEnergy)#, "\t", "%.3f" % ArtisanEnergy)
    #print(z+1, "\t\t",SolarHelp.index(min(SolarHelp)),"\t\t%.3f" % ArtisanEnergy)
    print(z+1, "\t\t",SolarHelp.index(min(SolarHelp)))
    if nut == True:
        break
stop = timeit.default_timer()
print("Average Cost: ","%.2f" % (_sum(SolarHelp)/len(SolarHelp)))
print('Program Run Time: ', "%.2f"  % (stop - start), "seconds")