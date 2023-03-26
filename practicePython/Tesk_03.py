a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3 ,4, 2, 1, 4, 2]
listA = []
listB = []
for element in a:
    if element<5: print(element)

for num in b:
    if num < 5:
        listA.append(num)
        listA.sort()
print(listA)
print()

num = int(input("Enter a number: "))
for n in b:
    if n < num:
        listB.append(n)
        listB.sort()
print(listB)
