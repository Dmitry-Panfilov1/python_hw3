n = int(input('enter massive size: '))
list_1 = []
for i in range(n):
    list_1.insert(i, int(input(f'enter element {i + 1}: ')))
print(*list_1)
x = int(input('enter x value: '))
divMax = 0
divMin = 5
closeNum = 0
for i in range(n):
    if list_1[i] > x:
       if x / list_1[i] > divMax:
            closeNum = list_1[i]
            divMax = x / list_1[i]
    else:
        if x / list_1[i] < divMin:
            closeNum = list_1[i]
            divRem = x / list_1[i]
print(closeNum)