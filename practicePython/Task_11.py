num = int(input('Enter a number: '))
check = [x for x in range(2, num) if num % x == 0]


def is_prime_number(number):
    if number >= 1:
        if len(check) == 0:
            print("Its prime number")
        else:
            print("Its not prime number")
    else:
        print("Its not prime number")


is_prime_number(num)
