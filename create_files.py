import os

folder = "AdventOfCode_2023"

os.makedirs(folder, exist_ok=True)

files = []
for i in range(1,25):
    soubor = f"{i}_12_2023.py"
    files.append(soubor)

# print(files)

for file in files:
    path_for_file = os.path.join(folder, file)
    with open(path_for_file, 'w') as f:
        f.write("\n")