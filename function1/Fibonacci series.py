def fibonacci(n):
    a = 0
    b = 1
    while n > 0:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        n = n - 1

# Test the function with a few values
fibonacci(0)
print()
fibonacci(1)
print()
fibonacci(2)
print()
fibonacci(3)
print()
fibonacci(4)
print()
fibonacci(5)
print()
fibonacci(6)
