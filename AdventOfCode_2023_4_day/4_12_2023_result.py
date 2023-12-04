# FIRST PART:

import re

# soubor_s_daty = 'AdventOfCode_2023_4_day\\4_12_2023_input.txt'
soubor_s_daty = 'test_folder\\test.txt'

with open(soubor_s_daty, 'r') as file:
    all_cards_entry = [radek.strip() for radek in file.readlines() if radek.strip()]

#     cards = [len(set.intersection(*({int(n) for n in part.split()} for part in line.split(':')[1].split('|')))) for line in file]
    
# print(cards)
# print(sum(round(2 ** (card - 1)) for card in cards))

# wins = [0] * len(cards)
# for i, c in reversed(list(enumerate(cards))):
#     wins[i] = 1 + sum(wins[i+1:i+1+c])
# print(sum(wins))

card_dict = {}
for item in all_cards_entry:
    card, value = item.split(':')
    card = card.strip()
    value = value.strip()
    values_list = value.split('|')
    my_values = values_list[0].strip().split()
    game_values = values_list[1].strip().split()
    card_dict[card] = {'My_numbers': my_values, 'Game_numbers': game_values}

# print(card_dict)

result_dict = {}
for card, numbers in card_dict.items():
    my_numbers = numbers['My_numbers']
    game_numbers = numbers['Game_numbers']
    common_numbers = list(set(my_numbers) & set(game_numbers))
    result_dict[card] = {'Common_numbers': common_numbers}
    
# print(result_dict)

result_dict_with_counts = {}
for card, numbers in result_dict.items():
    common_numbers = numbers['Common_numbers']
    count_common_numbers = len(common_numbers)
    result_dict_with_counts[card] = {'Common_numbers': common_numbers, 'Count': count_common_numbers}

# print(result_dict_with_counts)

pattern = re.compile(r"Card\s+\d+")

count_for_card = []
for i in range(len(all_cards_entry)):
    matches = pattern.findall(all_cards_entry[i])
    for match in matches:
        # print(match)
        count_for_card.append(result_dict_with_counts[match]['Count'])

print(count_for_card)

values_of_cards = []
for count in count_for_card:
    if count == 1:
        result = 1
    elif count >= 2:
        result = 2 ** (count-1)
    else:
        result = 0
    values_of_cards.append(result)
    
# print(sum(values_of_cards))

# SECOND PART:

wins = [0] * len(count_for_card)
# print(list(enumerate(count_for_card)))
for i, c in reversed(list(enumerate(count_for_card))):
    # print(f'i = {i}')
    # print(f'c = {c}')
    # print(wins[i+1:i+1])
    # print(wins[i+1:i+1+c])
    wins[i] = 1 + sum(wins[i+1:i+1+c])
    # print(f'wins = {wins[i]}')
print(sum(wins))