from random import randint


class Dice:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = randint(1, 6)

# def roll_dice():


def print_dices(dicelist):
    for dice in dicelist:
        print("[%d], " % dice.value, end="", flush=True)

    print()


gameFinished = False
playersList = []


playerCount = int(input("how many players will participate?"))

for i in range(0, playerCount): # for (int i = 0; i < playercount; i++)
    print("Enter name for player ", (i + 1))
    playerName = input()
    playersList.append(playerName)

dices = [Dice(), Dice(), Dice(), Dice(), Dice()]

while not gameFinished:
    for currentPlayer in playersList:
        print("%s turn" % currentPlayer)
        # Roll all dice first time
        for dice in dices:
            dice.roll()

        for reroll_chance in range(0, 2):
            print_dices(dices)
            choice_indices = input ("Which indexes does player " + str(currentPlayer) + " want to reroll? ")
            choice_indices = choice_indices.split(' ')

            if choice_indices[0] != '':
                for choice in choice_indices:
                    choice = int(choice)
                    dices[choice].roll()
            else:
                break

        dicesPicked = input("Which dices would you like to use?")
        dicesPicked = dicesPicked.split(' ')

        dicesToSave = []
        for dice_index in dicesPicked:
            dice_index = int(dice_index)
            dicesToSave.append(dices[dice_index])
        print("Choosing following dices: ")
        print_dices(dicesToSave)

        # Kolla kåk o sånt






