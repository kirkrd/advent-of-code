def checkCharIfInt(s):
    try:
      return type(int(s)) is int
    except ValueError:
        return False

with open('./input.txt') as f:
    lines = f.readlines()
    lines = [x.replace('\n', '') for x in lines]
    result = 0
    for line in lines:
        allNums = list(filter(lambda char: checkCharIfInt(char),  list(line)))
        result += int(allNums[0] + allNums[allNums.__len__() - 1])
    print(result)
