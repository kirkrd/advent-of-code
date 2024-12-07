locations_to_check = []

with open('./input.txt') as f:
    lines = f.readlines()
    lines = [x.replace('\n', '') for x in lines]
    left_list = []
    right_list = []
    total_distance = 0
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
        distance = abs(x - y)
        print(x, y)
        total_distance = total_distance + distance

    print("Answer", total_distance)
