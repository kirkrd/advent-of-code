with open('./data/task1input.txt') as f:
    lines = f.readlines()
    lines = [int(x.replace('\n',"")) for x in lines]

    lastSum = None
    latestNumbers = []
    increased = 0
    decreased = 0
    same = 0
    hasAchivedThree = False
    for index, x in enumerate(lines):
      try:
        a = lines[index]
        b = lines[index + 1]
        c = lines[index + 2]
        currSum = sum([a,b,c])
        if lastSum:
          if currSum > lastSum:
            increased+=1
          elif currSum < lastSum:
            decreased+=1
          else:
            same+=1
        lastSum = currSum
      except IndexError:
        break
    print("Increased:", increased)
    print("Decreased", decreased)
    print("Same", same)