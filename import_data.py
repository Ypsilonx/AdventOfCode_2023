import os
import requests
from datetime import datetime

session_token = '53616c7465645f5f0090ea0358348e0d7f23775763cfac10a782773567b49b855ac14bf4c12de84546daf0a2be8db4a06ccebacc85f4be2eb2382a329bb8b39e'

def correct_url(year, day_number):
    web_aoc = f'https://adventofcode.com/{year}/day/{day_number}/input'
    try:
        headers = {'Cookie': f'session={session_token}'}
        return requests.get(web_aoc, headers=headers)
    except:
        year = input('year?')
        day_number = input('day?')
        return requests.get(web_aoc, headers=headers)

year = datetime.now().year
day_number = datetime.now().day
folder = f"AdventOfCode_{year}_{day_number}_day"
python_file = f"{day_number}_12_{year}.py"
input_file = f'{day_number}_12_{year}_input.txt'

os.makedirs(folder, exist_ok=True)
path_for_python_file = os.path.join(folder, python_file)
path_for_input_file = os.path.join(folder, input_file)
raw = correct_url(year, day_number)

# with open(path_for_python_file, 'w') as f:
#     f.write("\n")
with open(path_for_input_file, 'wb') as f:
    f.write(raw.content)
with open("README.md", "a") as f:
    f.write(f"\n\n#### {day_number}_12_{year}\n")
