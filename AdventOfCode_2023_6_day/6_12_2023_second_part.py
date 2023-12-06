
soubor_s_daty = '6_12_2023_input.txt'

def vypocet_moznosti(zavod):
    pocet_moznosti = 1
    for time, distance in zavod:
        posibility_win_race = 0
        for j in range(0, time + 1):
            if time != 0:
                start = (time - j) * j
            if start > distance:
                posibility_win_race += 1
        pocet_moznosti = pocet_moznosti * posibility_win_race
        
    return pocet_moznosti

with open(soubor_s_daty, 'r') as file:
    vstupni_data = [radek.strip() for radek in file.readlines() if radek.strip()]  

result_dict = {}
for line in vstupni_data:
    parts = line.split()
    key = parts[0].rstrip(':')
    values = [int(value) for value in parts[1:]]
    str_numbers = [str(num) for num in values]
    result_string = ''.join(str_numbers)
    result_number = int(result_string)
    result_dict[key] = result_number
print(result_dict)


print(vypocet_moznosti(zavod =[(result_dict['Time'], result_dict['Distance'])]))