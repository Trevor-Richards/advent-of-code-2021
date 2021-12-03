input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

def calculate_gamma_rate(num_array):
    gamma_rate = ''
    lists = [list(map(int, i)) for i in zip(*map(str, num_array))]
    for lst in lists:
        if str(max(set(lst), key=lst.count)) == str(min(set(lst), key=lst.count)):
            gamma_rate += '1'
        else:
            gamma_rate += str(max(set(lst), key=lst.count))
    return gamma_rate

def flip_binary_bits(binary_num):
    return ''.join('1' if x == '0' else '0' for x in binary_num)

# Part 1
gamma_rate = calculate_gamma_rate(contents_split)
epsilon_rate = flip_binary_bits(gamma_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

#Part 2
contents_split_2 = contents_split[:]

oxygen_generator_rating = ''
CO2_scrubber_rating = ''

for index, num in enumerate(gamma_rate):
    numbers_for_removal = []
    for num in contents_split:
        if gamma_rate[index] != num[index]:
            numbers_for_removal.append(num)
    contents_split = [x for x in contents_split if x not in numbers_for_removal]
    gamma_rate = calculate_gamma_rate(contents_split)
    if len(contents_split) == 1:
        break

oxygen_generator_rating = contents_split[0]

for index, num in enumerate(epsilon_rate):
    numbers_for_removal = []
    for num in contents_split_2:
        if epsilon_rate[index] != num[index]:
            numbers_for_removal.append(num)
    contents_split_2 = [x for x in contents_split_2 if x not in numbers_for_removal]
    epsilon_rate = flip_binary_bits(calculate_gamma_rate(contents_split_2))
    if len(contents_split_2) == 1:
        break

CO2_scrubber_rating = contents_split_2[0]

print(int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2))
