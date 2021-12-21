with open('./data/task1input.txt') as f:
    lines = f.readlines()
    lines = [int(x.replace('\n',"")) for x in lines]
    prev = None
    increased = 0
    decreased = 0
    na = 0
    for x in lines:
      if prev != None:
        if x > prev:
          increased+=1
        elif prev > x:
          decreased+=1
        else:
          na+=1
      prev = x
    print("Number of increased:", increased)
    print("Number of decreased:", decreased)
    print("Number of N/A:", na)