locations_to_check = []

with open('./input.txt') as f:
    lines = f.readlines()
    lines = [x.replace('\n', '') for x in lines]
    left_list = []
    right_list = []
    total_distance = 0
    simularity_score = 0
    for line in lines:
        splitline = line.split("   ")
        if splitline[0] != "":
            left_list.append(int(splitline[0]))
        if splitline.__len__() > 1 and splitline[1] != "":
            right_list.append(int(splitline[1]))

    left_list.sort()
    right_list.sort()
    for i, x in enumerate(left_list):
        y = right_list[i]
        number_of_hits_in_right_list = right_list.count(x) * x
        distance = abs(x - y)
        total_distance = total_distance + distance
        simularity_score = simularity_score + number_of_hits_in_right_list

    print("Answer Part 1: ", total_distance)
    print("Answer Part 2: ", simularity_score)
