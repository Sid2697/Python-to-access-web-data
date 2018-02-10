import re
file = open('Text2.txt', 'r')
i = 0
ans = 0
numbers = list()
for lines in file:
    lines = lines.rstrip()
    y = re.findall('[0-9]+', lines)
    for entries in y:
        numbers.append(entries)

for data in numbers:
    data = int(data)
    ans += data
print(ans)
