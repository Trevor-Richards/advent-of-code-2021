input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()


def compare(array):
    difference_counter = 0

    for index, num in enumerate(array):
        if index > 0:
            previous = int(array[index - 1])
            if int(num) > previous:
                difference_counter += 1

    return difference_counter

#Part 1
print(compare(contents_split))

#Part 2
sums = []
for index, num in enumerate(contents_split):
    if index > 1:
        previous = int(contents_split[index - 1])
        previous_2 = int(contents_split[index - 2])
        sum = int(num) + previous + previous_2
        sums.append(sum)
        
print(compare(sums))

