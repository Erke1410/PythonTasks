num = int(input("Enter a number: "))
x = range(1, num)
listX = []
for element in x:
    if num % element == 0:
        listX.append(element)
        # listX.sort()

print(listX)