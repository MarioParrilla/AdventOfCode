max = 0
tmp = 0
for i in open('./data.txt'):
    if (i == '\n'):
        if (tmp > max):
            max = tmp
        tmp = 0
        continue
    tmp += int(i)
print(max)
