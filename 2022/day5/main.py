import re
stack1 = ["W", "P", "G", "Z", "V", "S", "B"]
stack2 = ["F", "Z", "C", "B", "V", "J"]
stack3 = ["C", "D", "Z", "N", "H", "M", "L", "V"]
stack4 = ["B", "J", "F", "P", "Z", "M", "D", "L"]
stack5 = ["H", "Q", "B", "J", "G", "C", "F", "V"]
stack6 = ["B", "L", "S", "T", "Q", "F", "G"]
stack7 = ["V", "Z", "C", "G", "L"]
stack8 = ["G", "L", "N"]
stack9 = ["C", "H", "F", "J"]

# Create a list of lists
lists = [stack1, stack2, stack3, stack4,
         stack5, stack6, stack7, stack8, stack9]


def move_items(lists, num_items, src_index, dest_index):
    # Remove the specified number of items from the source list
    src_items = lists[src_index][:num_items]
    for item in src_items:
        lists[src_index].remove(item)
    # Insert the items at the start of the destination list
    for item in src_items:
        lists[dest_index].insert(0, item)


def makeLineToInstruction(line: str):
    line = line.replace('\n', '')
    # Replace all occurrences of the specified strings
    numbers = re.findall(r"\b\d+\b", line)

    # Convert the string numbers to integer numbers
    numbers = list(map(int, numbers))
    return numbers


inputs = open("./input.txt").readlines()

craneInstructions = [makeLineToInstruction(x) for x in inputs]
for instruction in craneInstructions:
    move_items(lists, instruction[0], instruction[1] - 1, instruction[2] - 1)
order = []

for i, stack in enumerate(lists):
    print(f"{i + 1}: {stack[0]}")
    order.append(stack[0])

answer = "".join(order)
print(f"The answer for Day 5 Part 1 is: {answer}")
