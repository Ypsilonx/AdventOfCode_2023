# FIRST PART:

import re

path_input_data = 'AdventOfCode_2023_1_day\\1_12_2023_input.txt' # G:\\Locations_EU\\OST\\EU_S\\SVS\\01_Personal\\CCT\\AoC_2023\\1_12_2023_input.txt'

def find_numbers(row):
    numbers = re.findall(r'\d', row)
    if numbers:
        return f'{numbers[0]}{numbers[-1]}'
    else:
        return None

all_result = []
with open(path_input_data, 'r') as file:
    for row in file:
        result = find_numbers(row)
        if result:
            #print(result)
            all_result.append(int(result))
            
suma = sum(all_result)
print(suma)

# SECOND PART:

import re

def find_numbers(row, numbers_str):
    positions = []
    for number, str_number in enumerate(numbers_str, start=1):
        indexes = [ind.start() for ind in re.finditer(str_number, row)]
        for index in indexes:
            if index >= 0:
                positions.append([index,str(number)])
    return positions

path_input_data = 'AdventOfCode_2023_1_day\\1_12_2023_input.txt'
word_numbers = "one, two, three, four, five, six, seven, eight, nine".split(", ")
digits = "123456789"

with open(path_input_data, 'r') as file:
    suma = 0
    for row in file:
        numbers_in_lines = []
        numbers_in_lines += find_numbers(row, word_numbers) #find indexes of all "word numbers"
        numbers_in_lines += find_numbers(row, digits) #find indexes of all "ciphers"
        numbers_in_lines.sort() #sort list
        result = int(numbers_in_lines[0][1] + numbers_in_lines[-1][1]) #get first and last number
        suma += result

print(suma)
