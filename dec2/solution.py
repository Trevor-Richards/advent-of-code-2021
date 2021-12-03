input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

#Part 1
horizontal_pos = 0
depth = 0

for instruction in contents_split:
    direction = instruction.split(' ')[0]
    value = int(instruction.split(' ')[1])
    if direction == 'forward':
        horizontal_pos += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value

print(horizontal_pos * depth)

#Part 2
horizontal_pos = 0
depth = 0
aim = 0


for instruction in contents_split:
    direction = instruction.split(' ')[0]
    value = int(instruction.split(' ')[1])
    if direction == 'forward':
        horizontal_pos += value
        depth += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value

print(horizontal_pos * depth)



