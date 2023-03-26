# word = input("Enter a word: ")
# word = str(word)
# reverse = word[:: -1]
# print(reverse)
# if word == reverse:
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) - 1 - i]
    return x


word = input('give me a word:\n')
x = reverse(word)
if x == word:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

# x = input("Enter a word: ")
# a = x.split()
# a.reverse()
# print(" ".join(a))
