def fib(n, k):
    if n < 3:
        print(1)
    else:
        a, b = 1, 1
        for _ in range(3, n+1):
            a, b = b, (a*k+b)
        return b
print(fib(29,5))

a, b = 1, 0
for _ in range(0, 5):
    x = a+b
    a = b
    b = x
    print(x)