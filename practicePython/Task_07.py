a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
listA = []
# for elem in a:
#     if elem % 2==0: listA.append(elem)
# print(listA)

listB = [number for number in a if number % 2 == 0]

print(listB)