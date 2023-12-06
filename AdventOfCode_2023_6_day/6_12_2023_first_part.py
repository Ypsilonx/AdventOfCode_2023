import pandas as pd
import numpy as np

soubor_s_daty = '6_12_2023_input.txt'

def vypocet_moznosti(time, distance):
    posibility_win_race = []
    for i in range(0, time):
        speed = i * 1
        race = time - i
        race_dist = race * speed
        if race_dist > distance:
            posibility_win_race.append(i)
    
    return len(posibility_win_race)

def pocet_moznosti(data):
    number_posibility = []
    for i in data:
        x, y = i
        number_posibility.append(vypocet_moznosti(x, y))
    # print(number_posibility)     
    return np.prod(number_posibility)

with open(soubor_s_daty, 'r') as file:
    vstupni_data = [radek.strip() for radek in file.readlines() if radek.strip()]  

result_dict = {}
for line in vstupni_data:
    parts = line.split()
    key = parts[0].rstrip(':')
    values = [int(value) for value in parts[1:]]
    result_dict[key] = values
# print(result_dict)

result_pairs = list(zip(result_dict['Time'], result_dict['Distance']))
# print(result_pairs)

print(pocet_moznosti(result_pairs))