#
# For example, suppose you have the following list of contents from six rucksacks:
#
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

import json

input = open('./input.txt')
inputs = input.readlines()
inputlist = [x.replace('\n', '').split(" ") for x in inputs]
summary = 0
theAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for code in inputlist:
    compartments = code[0]
    x = len(compartments)
    firstCompartment = [*compartments[:len(compartments) // 2]]
    secondCompartment = [*compartments[len(compartments) // 2:]]
    matchedType = ""

    for char in firstCompartment:
        for char2 in secondCompartment:
            if char2 == char:
                matchedType = char
    if matchedType.islower():
        summary += theAlphabet.index(matchedType) + 1
    else:
        summary += theAlphabet.index(matchedType.lower()) + 27

print(f"Final summary part 1: {summary}")

part2List = [inputlist[i:i + 3] for i in range(0, len(inputlist), 3)]
summaryPart2 = 0
for parts in part2List:
    matchedType = ""
    for char in parts[0][0]:
        for char2 in parts[1][0]:
            for char3 in parts[2][0]:
                if char == char2 and char2 == char3:
                    matchedType = char

    if matchedType.islower():
        summaryPart2 += theAlphabet.index(matchedType) + 1
    else:
        summaryPart2 += theAlphabet.index(matchedType.lower()) + 27

print(f"Final summary part 2: {summaryPart2}")
