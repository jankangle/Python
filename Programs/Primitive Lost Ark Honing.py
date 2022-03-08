#PYTHON TIME
from pydoc import doc
import random

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
NumofIterations = 100000


### COST ###
#UPDATE THESE
DestructionStonesCost = 93 / 10     # Destruction Stone Crystals
HonorLeapStonesCost = 168           # Honor Leapstones
SolarGraceCost = 60                 # Solar Grace
SolarBlessingCost = 245           # Solar Blessing
SolarProtectionCost = 560      # Solar Protection

HoneLVL = int(input("Enter Weapon Hone LVL Target: "))
if HoneLVL == 7:
    ChanceToHone = 0.60
    NumOfDestructionStones = 250
    NumOfHonorLeapStones = 8
    SolarGraceBenefit = 0.0167
    SolarBlessingBenefit = 0.03333
    SolarProtectionBenefit = 0.1
elif HoneLVL == 8:
    ChanceToHone = 0.45
    NumOfDestructionStones = 258
    NumOfHonorLeapStones = 8
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 9:
    ChanceToHone = 0.30
    NumOfDestructionStones = 258
    NumOfHonorLeapStones = 8 
    SolarGraceBenefit = 0.0084
    SolarBlessingBenefit = 0.0167
    SolarProtectionBenefit = 0.05
elif HoneLVL == 10:
    ChanceToHone = 0.30
    NumOfDestructionStones = 320
    NumOfHonorLeapStones = 10
    SolarGraceBenefit = 0.0084
    SolarBlessingBenefit = 0.0167
    SolarProtectionBenefit = 0.05
### Experimental Benefits ###
elif HoneLVL == 11:
    ChanceToHone = 0.30
    NumOfDestructionStones = 320
    NumOfHonorLeapStones = 10
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 12:
    ChanceToHone = 0.30
    NumOfDestructionStones = 320
    NumOfHonorLeapStones = 10
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 13:
    ChanceToHone = 0.15
    NumOfDestructionStones = 380
    NumOfHonorLeapStones = 10
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 14:
    ChanceToHone = 0.15
    NumOfDestructionStones = 380
    NumOfHonorLeapStones = 12
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
elif HoneLVL == 15:
    ChanceToHone = 0.1
    NumOfDestructionStones = 380
    NumOfHonorLeapStones = 12
    SolarGraceBenefit = 0.0125
    SolarBlessingBenefit = 0.025
    SolarProtectionBenefit = 0.075
else:
    print("Wrong")
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
elif UserHelp == "B":
    MaxHelp = MaxSolarBlessing
elif UserHelp == "P":
    MaxHelp = MaxSolarProtection
elif UserHelp == "N":
    MaxHelp = 0
else:
    exit()

for z in range(0, 5):
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
                        ArtisanEnergy += (ChanceToHone + (SolarGraceBenefit * UsedSolarGrace) + PityChance) * 0.465
                                    
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
            if y == MaxMaxHelp:
                break

        ###Debugging Purposes ###
        #print("Help used", y)
        #print("Number of Iterations: ", NumofIterations)
        #print("Average Number of Attempts: ", _sum(Attempts) / len(Attempts))
        #print("Average Cost: ", _sum(Costs) / len(Costs))
        ###
        ArtisanEnergy = (((z) * ChanceToHone) + (SolarGraceBenefit * _sum(LowestCost))) * 0.465

        SolarHelp.append(_sum(Costs) / len(Costs))
        AttemptsforAVG.append(_sum(Attempts) / len(Attempts))
        if ArtisanEnergy >= 1:
            nut = True
            break
    LowestCost.append(SolarHelp.index(min(SolarHelp)))
    if nut == True:
        break
    #print("Solar Help", "\tAverage Cost", "\tAverage Number of Attempts")
    #for i in SolarHelp:
    #    print(SolarHelp.index(i), "\t \t" , "%.2f"  %i, "\t" , "%.3f" %AttemptsforAVG[SolarHelp.index(i)])

    print( "%.2f" % min(SolarHelp), "\t",SolarHelp.index(min(SolarHelp)))#, "\t", "%.3f" % ArtisanEnergy)

