types = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points = {'X': 1, 'Y': 2, 'Z': 3}
total_points = 0
for i in open('./data.txt'):
    elf, me = i.replace("\n", "").split(" ")
    if types[elf] == me:
        total_points += points[me] + 6
    elif draws[elf] == me:
     total_points += points[me] + 3
    else:
        total_points += points[me]
print(total_points)
