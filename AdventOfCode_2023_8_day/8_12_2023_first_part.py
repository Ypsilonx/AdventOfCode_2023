from itertools import cycle

with open('8_12_2023_input.txt', 'rt') as f:
    radky = f.readlines()
    
if radky:
    prikazy_navigace = list(radky[0].strip())
    # print(prikazy_navigace)
    # ['R', 'L']
    instrukce_na_mape_bez_uprav = radky[1:]
    # print(instrukce_na_mape_bez_uprav)

instrukce_na_mape = [radek.strip() for radek in instrukce_na_mape_bez_uprav if radek.strip()]
# print(instrukce_na_mape)
# ['AAA = (BBB, CCC)', 'BBB = (DDD, EEE)', 'CCC = (ZZZ, GGG)', 'DDD = (DDD, DDD)', 'EEE = (EEE, EEE)', 'GGG = (GGG, GGG)', 'ZZZ = (ZZZ, ZZZ)']

slovnik_instrukci = {}
for item in instrukce_na_mape:
    vstupni_smer, dalsi_smer = map(str.strip, item.split('='))
    dalsi_smer = tuple(map(str.strip, dalsi_smer[1:-1].split(',')))
    slovnik_instrukci[vstupni_smer] = dalsi_smer
# print(slovnik_instrukci)
# {'AAA': ('BBB', 'CCC'), 'BBB': ('DDD', 'EEE'), 'CCC': ('ZZZ', 'GGG'), 'DDD': ('DDD', 'DDD'), 'EEE': ('EEE', 'EEE'), 'GGG': ('GGG', 'GGG'), 'ZZZ': ('ZZZ', 'ZZZ')}

def navigate(prikazy_navigace, slovnik_instrukci):
    aktualni_klic = 'AAA'
    vysledek = []
    pocet_prikazu = 0

    for prikaz in cycle(prikazy_navigace):
        if aktualni_klic == 'ZZZ':
            break

        if aktualni_klic in slovnik_instrukci:
            print(aktualni_klic)
            hodnoty = slovnik_instrukci[aktualni_klic]
            aktualni_klic = hodnoty[1] if prikaz == 'R' else hodnoty[0]
            vysledek.append(aktualni_klic)
            pocet_prikazu += 1
        else:
            print(f"Klíč '{aktualni_klic}' nenalezen ve slovníku instrukcí.")
            break

    return vysledek, pocet_prikazu

vysledek_navigace, pocet_prikazu = navigate(prikazy_navigace, slovnik_instrukci)
print(f"Celkový počet provedených navigačních příkazů: {pocet_prikazu}")