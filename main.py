import random as r
import matplotlib.pyplot as plt


def probs(trial):
    probs1, probs2, probs3 = [], [], []
    firstCounter, secondCounter, thirdCounter = 0, 0, 0

    for _ in range(1, trial + 1):
        listOfDice = []
        for i in range(5):
            dice = r.randint(1, 6)
            listOfDice.append(dice)

        if 3 in listOfDice:
            firstCounter += 1
        probs1.append(firstCounter / _)

    for _ in range(1, trial + 1):
        listOfDice = []
        for i in range(4):
            dice = r.randint(1, 6)
            listOfDice.append(dice)

        if 3 in listOfDice:
            secondCounter += 1
        probs2.append(secondCounter / _)

    for _ in range(1, trial + 1):
        listOfDice = []
        for i in range(4):
            dice = r.randrange(1, 6, 2)
            listOfDice.append(dice)
        if 3 in listOfDice:
            thirdCounter += 1
        probs3.append(thirdCounter / _)

    return firstCounter, secondCounter, thirdCounter, probs1, probs2, probs3


def theoreticalSolutionsOutput():
    print("Theoretical Solutions")
    print(round(1 - (5 / 6) * (5 / 6) * (5 / 6) * (5 / 6) * (5 / 6), 4))
    print(round(1 - (5 / 6) * (5 / 6) * (5 / 6) * (5 / 6), 4))
    print(round(1 - (2 / 3) * (2 / 3) * (2 / 3) * (2 / 3), 4))


ct1, ct2, ct3, probs1, probs2, probs3 = probs(1000000)


def experimentalSolutionsOutput():
    print("Experimental Solutions")
    print(ct1 / 1000000)
    print(ct2 / 1000000)
    print(ct3 / 1000000)


def plotOutput():
    plt.plot([probs1[9], probs1[49], probs1[99], probs1[499], probs1[999], probs1[4999], probs1[9999], probs1[49999],
              probs1[99999], probs1[499999], probs1[999999]])

    plt.show()

    plt.plot([probs2[9], probs2[49], probs2[99], probs2[499], probs2[999], probs2[4999], probs2[9999], probs2[49999],

              probs2[99999], probs2[499999], probs2[999999]])

    plt.show()

    plt.plot([probs3[9], probs3[49], probs3[99], probs3[499], probs3[999], probs3[4999], probs3[9999], probs3[49999],

              probs3[99999], probs3[499999], probs3[999999]])
    plt.show()


theoreticalSolutionsOutput()
experimentalSolutionsOutput()
plotOutput()
