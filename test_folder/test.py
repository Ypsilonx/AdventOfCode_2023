
soubor_s_daty = 'test_folder\\test.txt'
# soubor_s_daty = 'AdventOfCode_2023_2_day\\2_12_2023_input.txt'

with open(soubor_s_daty, 'r') as file:
    vstupni_data = file.read()

radky = vstupni_data.strip().split('\n')

seznam_ok_game = []
for radek in radky:
    game = radek.split(':')
    number_game = game[0].split(' ')
    game = game[1].split(';')
    
    all_handles = []
    for i in range(len(game)):
        game_handle = game[i].split(',')
        handle = [x.strip() for x in game_handle]
        all_handles.extend(handle)
    
    print(f'GAME {number_game[1]}:')
    print(all_handles)
    
    edit_all_handles = [x.split() for x in all_handles]
    
    print(edit_all_handles)
    
    check = []
    for z in edit_all_handles:
        print(z)
        if int(z[0]) <= 12 and z[1] == 'red':
            check.append(True)
        elif int(z[0]) <= 13 and z[1] == 'green':
            check.append(True)
        elif int(z[0]) <= 14 and z[1] == 'blue':
            check.append(True)
        else:
            check.append(False)
            
    print(check)
    count_true = check.count(True)
    count_check = len(check)
    
    if count_true == count_check:
        seznam_ok_game.append(int(number_game[1]))
print(sum(seznam_ok_game))





# soubor_s_daty = 'test_folder\\test.txt'
soubor_s_daty = 'AdventOfCode_2023_2_day\\2_12_2023_input.txt'

with open(soubor_s_daty, 'r') as file:
    vstupni_data = file.read()

radky = vstupni_data.strip().split('\n')

seznam_ok_game = []
for radek in radky:
    game = radek.split(':')
    number_game = game[0].split(' ')
    game = game[1].split(';')
    
    all_handles = []
    for i in range(len(game)):
        game_handle = game[i].split(',')
        handle = [x.strip() for x in game_handle]
        all_handles.extend(handle)
    
    print(f'GAME {number_game[1]}:')
    print(all_handles)
    
    edit_all_handles = [x.split() for x in all_handles]
    
    print(edit_all_handles)

    max_values = {}
    for item in edit_all_handles:
        key = item[1]
        value = int(item[0])
        
        if key not in max_values or value > max_values[key]:
            max_values[key] = value

    result = [(str(value), key) for key, value in max_values.items()]
    print(result)

    max_values_list = [int(item[0]) for item in result]
    
    product = 1
    for value in max_values_list:
        product *= value
        
    print(product)
        
    seznam_ok_game.append(product)
print(sum(seznam_ok_game))
