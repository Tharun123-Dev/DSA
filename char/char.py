#aaabbbaacccb
#abcde---bde-false,ac--True
#google--el---false --gl--True


s = "aaabbccdab"
result =" "
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

# Add the last character
result += s[-1] + str(count)

print(result)


def fibonacci(n):
    if n == 0:
        return 0  
    elif n == 1:
        return 1   
    else:
        return fibonacci(n-1) + fibonacci(n-2) #---fib 2--fib1+fib0  #fib3---fib1+fib2

n_terms = 10
for i in range(n_terms):
    print(fibonacci(i), end=" ")

