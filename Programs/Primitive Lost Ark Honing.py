#PYTHON TIME
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
NumofIterations = 500000

### COST ###
#UPDATE THESE
DestructionStonesCost = 68 / 10     # Destruction Stone Crystals
HonorLeapStonesCost = 161           # Honor Leapstones
SolarGraceCost = 34.5               # Solar Grace
SolarBlessingCost = 86.33           # Solar Blessing
SolarProtectionCost = 431.6667      # Solar Protection

#LVL 6 -> LVL7
ChanceToHone = 0.6
NumOfDestructionStones = 250
NumOfHonorLeapStones = 8


### HELP ITEMS ###
#Solar Grace
MaxSolarGrace = 12
SolarGraceBenefit = 0.0167

#Solar Blessing
MaxSolarBlessing = 6
SolarBlessingBenefit = 0.03333

#Solar Protection
MaxSolarProtection = 2
SolarProtectionBenefit = 0.1



#Help Usage
UsedSolarGrace = 0
UsedSolarBlessing = 0
UsedSolarProtection = 0


### ARRAY DECLARATIONS ###
Attempts = []
AttemptsforAVG = []
Costs = []
SolarHelp = []


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


#MaxHelp = MaxSolarGrace
for y in range(0, MaxHelp+1):
    for x in range(1, NumofIterations):
        if UserHelp == "G":
            UsedSolarGrace = y
        elif UserHelp == "B":
            UsedSolarBlessing = y
        elif UserHelp == "P":
            UsedSolarProtection = y
        elif UserHelp == "N":
            UsedSolarGrace = 0
            UsedSolarBlessing = 0
            UsedSolarProtection = 0
        TotalHelp = (SolarGraceBenefit * UsedSolarGrace) + (SolarBlessingBenefit * UsedSolarBlessing) + (SolarProtectionBenefit * UsedSolarProtection)
        HelpCost = (UsedSolarGrace * SolarGraceCost) + (UsedSolarBlessing * SolarBlessingCost) + (UsedSolarProtection * SolarProtectionCost)
        passfail = False
        NumofAttempts=0
        TotalCost = DestructionStonesCost * NumOfDestructionStones + HonorLeapStonesCost * NumOfHonorLeapStones + HelpCost
        ArtisanEnergy = 0
        while passfail == False:
            NumofAttempts += 1
            if random.random() >= ChanceToHone + ArtisanEnergy + TotalHelp:
                ArtisanEnergy += (ChanceToHone + (SolarGraceBenefit * UsedSolarGrace)) / 10                       
                if ArtisanEnergy >= 1:
                    break
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
    ###Debugging Purposes ###
    #print("Help used", y)
    #print("Number of Iterations: ", NumofIterations)
    #print("Average Number of Attempts: ", _sum(Attempts) / len(Attempts))
    #print("Average Cost: ", _sum(Costs) / len(Costs))
    ###
    SolarHelp.append(_sum(Costs) / len(Costs))
    AttemptsforAVG.append(_sum(Attempts) / len(Attempts))
print("Solar Help", "\tAverage Cost", "\tAverage Number of Attempts")
for i in SolarHelp:
    print(SolarHelp.index(i), "\t \t" , "%.2f"  %i, "\t" , "%.3f" %AttemptsforAVG[SolarHelp.index(i)])
