inputs = open("./input.txt").readlines()
inputlist = [x.replace('\n', '').split(" ") for x in inputs]
inputlistfixed = [x[0].split(",") for x in inputlist]
count = 0
exampleCount = 0
countOverlapAtAll = 0
exampleData = [[range(2, 4), range(6, 8)], [range(2, 3), range(4, 5)],
               [range(5, 7), range(7, 9)], [range(2, 8), range(3, 7)], [
    range(6, 6), range(4, 6)],
    [range(2, 6), range(4, 8)]]


def range_fully_covers_other(first: range, second: range):
    firstList = [*first, first.stop] if first.start != first.stop else [
        first.start, first.stop]
    secondList = [*second, second.stop] if second.start != second.stop else [
        second.start, second.stop]
    isEveryIn1 = all(x in firstList for x in secondList)
    isEveryIn2 = all(x in secondList for x in firstList)
    # print(f"First: {firstList} <-- {first}")
    # print(f"Second: {secondList} <-- {second}")
    return isEveryIn1 or isEveryIn2


def range_overlap(range1, range2):
    """Whether range1 and range2 overlap."""
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 <= y2 and y1 <= x2


for pair in exampleData:
    if range_fully_covers_other(pair[0], pair[1]):
        exampleCount += 1
print(f"Example Reference Count: {exampleCount} (2)")
for pair in inputlistfixed:
    firstElfAssignments = pair[0].split("-")
    secondElfAssigments = pair[1].split("-")
    elf1Range = range(int(firstElfAssignments[0]), int(firstElfAssignments[1]))
    elf2Range = range(int(secondElfAssigments[0]), int(secondElfAssigments[1]))
    if range_fully_covers_other(elf1Range, elf2Range):
        count += 1
    if range_overlap(elf1Range, elf2Range):
        countOverlapAtAll += 1


print(f"Total Pairs that fully contain each other: {count} (Part 1)")
print(f"Total Pairs that overlap at all {countOverlapAtAll} (Part 2)")
print(f"Total Pairs: {inputlistfixed.__len__()}")
