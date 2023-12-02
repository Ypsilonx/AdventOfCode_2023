import os
import requests
from datetime import datetime

session_token = os.environ.get('SESSION_TOKEN')

def correct_url(year, day_number):
    web_aoc = f'https://adventofcode.com/{year}/day/{day_number}/input'
    web_aoc_entering = f'https://adventofcode.com/{year}/day/{day_number}'
    try:
        headers = {'Cookie': f'session={session_token}'}
        raw = requests.get(web_aoc, headers=headers)
        entering = requests.get(web_aoc_entering, headers=headers)
        return raw, entering
    except:
        year = input('year?')
        day_number = input('day?')
        return requests.get(web_aoc, headers=headers), requests.get(web_aoc_entering, headers=headers)

year = datetime.now().year
day_number = datetime.now().day
folder = f"AdventOfCode_{year}_{day_number}_day"
python_file = f"{day_number}_12_{year}.py"
input_file = f'{day_number}_12_{year}_input.txt'
entering_file = f'{day_number}_12_{year}_entering.md'

os.makedirs(folder, exist_ok=True)
# path_for_python_file = os.path.join(folder, python_file)
path_for_input_file = os.path.join(folder, input_file)
path_for_entering_file = os.path.join(folder, entering_file)
raw = correct_url(year, day_number)[0]
entering = correct_url(year, day_number)[1]

# with open(path_for_python_file, 'w') as f:
#     f.write("\n")
with open(path_for_entering_file, 'wb') as f:
    f.write(entering.content)
with open(path_for_input_file, 'wb') as f:
    f.write(raw.content)
# with open("README.md", "a") as f:
#     f.write(f"\n\n#### {day_number}_12_{year}\n")
