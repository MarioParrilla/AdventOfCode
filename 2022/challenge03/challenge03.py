import math

result = 0
for i in open('./data.txt'):
    x = i.replace("\n", "")
    print('{a}: {b}'.format(a=len(x),b=math.floor(len(x)/2)))
    p1 = x[0:math.floor(len(x)/2)]
    p2 = x[math.floor(len(x)/2):len(x)]
    print(x)
    print(p1)
    print(p2)

    matchedStr = ''
    for letter in p2:
        index = p1.find(letter)
        if index is not -1:
            matchedStr = p1[index]
            break
    codepoint = ord(matchedStr);
    if codepoint <= 90:
        result += (codepoint - 38)
        print(f"Letter: {matchedStr} | Points: {(codepoint - 38)}")
    else:
        result += (codepoint - 96)
        print(f"Letter: {matchedStr} | Points: {(codepoint - 96)}")
    print('----------------')
print(result)