text = input("Enter a word: ")
i = 0
j = len(text) - 1
is_palindrome = True

while i < j:
    if text[i] != text[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")