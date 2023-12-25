from collections import Counter


# soubor_s_daty = 'AdventOfCode_2023_7_day\\7_12_2023_input.txt'
soubor_s_daty = 'test_folder\\test.txt'

with open(soubor_s_daty, 'r') as f:
    karty_v_rukou = [(line.split()[0], int(line.split()[1])) for line in f]
# print(karty_v_rukou)
# [('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)]

hodnoceni_karet_vstup = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2"
hodnoceni_karet = {hodnota: index for index, hodnota in enumerate(reversed(hodnoceni_karet_vstup.split(', ')))}
# print(hodnoceni_karet)
# {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'Q': 9, 'K': 10, 'A': 11}
pouze_hodnoceni = tuple(hodnoceni_karet[char] for char in hodnoceni_karet)
# print(pouze_hodnoceni)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

nahrazeni_karet_hodnotou = sorted((v for k, v in Counter().items()), reverse=True)
print(nahrazeni_karet_hodnotou)