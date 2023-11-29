import os
import requests
from datetime import datetime

def correct_url(year, day_number):
    web_aoc = f'https://adventofcode.com/{year}/day/{day_number}/input'
    try:
        return requests.get(web_aoc)
    except:
        year = input('year?')
        day_number = input('day?')
        return requests.get(web_aoc)
    

year = datetime.now().year
day_number = datetime.now().day
folder = f"AdventOfCode_{year}_{day_number}_day"
python_file = f"{day_number}_12_{year}.py"
input_file = f'{day_number}_12_{year}_input.txt'

os.makedirs(folder, exist_ok=True)
path_for_python_file = os.path.join(folder, python_file)
path_for_input_file = os.path.join(folder, input_file)
raw = correct_url(year, day_number)

with open(path_for_python_file, 'w') as f:
    f.write("\n")
with open(path_for_input_file, 'wb') as f:
    f.write(raw.content)
with open("README.md", "a") as f:
    f.write(f"\n\n#### {day_number}_12_{year}\n - new puzzles\n - new day\n - new knowledge")
