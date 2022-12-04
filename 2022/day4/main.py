inputs = open("./input.txt").readlines()
inputlist = [x.replace('\n', '').split(" ") for x in inputs]
inputlistfixed = [x[0].split(",") for x in inputlist]
count = 0
for pair in inputlistfixed:
    rangeElf1 = range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1]))
    rangeElf2 = range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1]))
    sameInFirst = True
    sameInSecond = True
    for num in rangeElf1:
        if num in rangeElf2:
            continue
        else:
            sameInFirst = False
            break
    for num in rangeElf2:
        if num in rangeElf1:
            continue
        else:
            sameInSecond = False
            break
    if sameInFirst or sameInSecond:
        count += 1


print(f"Total elf pairs: {count}. {inputlistfixed.__len__()}")
