class Elf:

    name = ""
    carrying = []

    def __init__(self, name, carrying):

        self.name = name
        self.carrying = carrying

    def howMuchCarrying(self):
        return sum(self.carrying)


with open('./input.txt') as f:
    lines = f.readlines()
    lines = [x.replace('\n', '') for x in lines]
    elves = []
    elfName = f"Elf{elves.__len__() + 1}"
    currCalories = []
    for x in lines:
        if x == '':
            elves.append(Elf(elfName, currCalories))
            elfName = f"Elf{elves.__len__() + 1}"
            currCalories = []
        else:
            currCalorie = int(x)
            currCalories.append(currCalorie)

    mostCaloriesElf = Elf("Test", [0])
    secondMostCaloriesElf = Elf("Test2", [0])
    thirdMostCalroiesElf = Elf("Test3", [0])
    for elf in elves:
        top3 = 'No'
        if elf.howMuchCarrying() > thirdMostCalroiesElf.howMuchCarrying():
            top3 = 3
            if elf.howMuchCarrying() > secondMostCaloriesElf.howMuchCarrying():
                top3 = 2
                if elf.howMuchCarrying() > mostCaloriesElf.howMuchCarrying():
                    top3 = 1
        if top3 == 3:
            thirdMostCalroiesElf = elf
        if top3 == 2:
            thirdMostCalroiesElf = secondMostCaloriesElf
            secondMostCaloriesElf = elf
        if top3 == 1:
            thirdMostCalroiesElf = secondMostCaloriesElf
            secondMostCaloriesElf = mostCaloriesElf
            mostCaloriesElf = elf

    print(f"{mostCaloriesElf.name}, {mostCaloriesElf.howMuchCarrying()} (Part 1)")

    topThreeElfCalories = mostCaloriesElf.howMuchCarrying(
    ) + secondMostCaloriesElf.howMuchCarrying() + thirdMostCalroiesElf.howMuchCarrying()
    print(f"Top Three Elves are carrying {topThreeElfCalories} kcal. (Part 2)")
