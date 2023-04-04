n = int(input('enter massive size: '))
list_1 = []
for i in range(n):
    list_1.insert(i, int(input(f'enter element {i + 1}: '))) 
print(*list_1)
x = int(input('enter x value: '))
index = 0
for i in range(n):
    if list_1[i] == x:
        index += 1
print(index)