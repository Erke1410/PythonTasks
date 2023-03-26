number = int(input("How many Fibonacci numbers do you want: "))


def write_fibonacci_sequence(num):
    list_a = []
    a = 1
    if num == 1:
        list_a = [1]
    elif num >= 2:
        list_a = [1, 1]
        while a < (num - 1):
            list_a.append(list_a[a] + list_a[a - 1])
            a += 1
    return list_a


seq = write_fibonacci_sequence(number)
print(seq)
