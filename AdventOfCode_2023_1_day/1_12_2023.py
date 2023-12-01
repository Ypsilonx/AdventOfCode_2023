# FIRST PART:

import re

path_input_data = '1_12_2023_input.txt' # G:\\Locations_EU\\OST\\EU_S\\SVS\\01_Personal\\CCT\\AoC_2023\\1_12_2023_input.txt'

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
            print(result)
            all_result.append(int(result))
            
suma = (all_result)
print(suma)

# SECOND PART:

import re

path_input_data = '1_12_2023_input.txt' # G:\\Locations_EU\\OST\\EU_S\\SVS\\01_Personal\\CCT\\AoC_2023\\1_12_2023_input.txt'

word_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def find_numbers(row):
    numbers = re.findall(r'(?:' + '|'.join(word_numbers.keys()) + r'|\d+)', row)
    
    if numbers:
        # Pokud jsou k dispozici čísla, vrátíme je jako tuple
        first_number = word_numbers.get(numbers[0], None) or int(numbers[0][0])
        print(first_number)
        last_number = word_numbers.get(numbers[-1], None) or int(numbers[-1][-1])
        print(last_number)
        
        if first_number is None:
            first_number = int(numbers[0])
            
        if last_number is None:
            last_number = int(numbers[-1])
        
        return first_number, last_number
    else:
        return None, None

all_result = []
with open(path_input_data, 'r') as file:
    for row in file:
        result = find_numbers(row)
        if result[0] is not None and result[1] is not None:
            print(result)
            result_1 = f'{result[0]}{result[1]}'
            print(result_1)
            all_result.extend(int(result_1))
            
suma = sum(all_result)
print(suma)
