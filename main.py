import random as r
import matplotlib.pyplot as plt


def empricalProbs(trial):
    probs1 = []
    probs2 = []
    probs3 = []
    firstCounter, secondCounter, thirdCounter = 0, 0, 0

    for _ in range(1, trial + 1):
        numberOfListDice = []
        for x in range(5):
            dice = r.randint(1, 6)
            numberOfListDice.append(dice)

        if 3 in numberOfListDice:
            firstCounter += 1

        probs1.append(firstCounter / _)

    for _ in range(1, trial + 1):
        numberOfListDice = []
        for x in range(4):
            dice = r.randint(1, 6)
            numberOfListDice.append(dice)

        if 3 in numberOfListDice:
            secondCounter += 1
        probs2.append(secondCounter / _)

    for _ in range(1, trial + 1):
        numberOfListDice = []
        for x in range(4):
            dice = r.randrange(1, 6, 2)
            numberOfListDice.append(dice)
        if 3 in numberOfListDice:
            thirdCounter += 1
        probs3.append(thirdCounter / _)

    return firstCounter, secondCounter, thirdCounter, probs1, probs2, probs3


firstCounter, secondCounter, thirdCounter, probs1, probs2, probs3 = empricalProbs(1000000)


def outputTheoreticalProbs():
    print("Theoretical Solutions")
    print(round(1 - (5 / 6) * (5 / 6) * (5 / 6) * (5 / 6) * (5 / 6), 4))
    print(round(1 - (5 / 6) * (5 / 6) * (5 / 6) * (5 / 6), 4))
    print(round(1 - (2 / 3) * (2 / 3) * (2 / 3) * (2 / 3), 4))


def outputEmprical(probs):
    print("Experimental Solutions")
    print(round(probs[9], 4), round(probs[49], 4), round(probs[99], 4), round(probs[499], 4), round(probs[999], 4),
          round(probs[4999], 4), round(probs[9999], 4), round(probs[49999], 4),
          round(probs[99999], 4), round(probs[499999], 4), round(probs[999999], 4))


def drawGraph(probs):
    plt.plot([probs[9], probs[49], probs[99], probs[499], probs[999], probs[4999], probs[9999], probs[49999],
              probs[99999], probs[499999], probs[999999]])

    plt.show()


outputTheoreticalProbs()
outputEmprical(probs1)
outputEmprical(probs2)
outputEmprical(probs3)
drawGraph(probs1)
drawGraph(probs2)
drawGraph(probs3)
