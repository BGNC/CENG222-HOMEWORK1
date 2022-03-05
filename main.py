import random as r
import matplotlib.pyplot as plt

numberOfEvents = 1000000
ct1 = 0
ct2 = 0
ct3 = 0

probs1 = []

for x in range(1, numberOfEvents+1):
    listOfDice = []
    for i in range(5):
        dice = r.randint(1, 6)
        listOfDice.append(dice)

    if 3 in listOfDice:
        ct1 += 1
        probs1.append(ct1 / x)
        if (2 or 4 or 6) in listOfDice:
            ct2 += 1

        evenCounter = 0
        for c in listOfDice:

            if c == (2 or 4 or 6):
                evenCounter += 1
        if evenCounter == 1:
            ct3 += 1




print(ct1 / numberOfEvents)

print(ct2 / numberOfEvents)

print(ct3 / numberOfEvents)

plt.plot(probs1)
plt.show()