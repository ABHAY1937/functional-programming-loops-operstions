def fact(num):
    i = 1
    fact = 1
    while (i <= num):
        fact *= i
        i += 1
    print(fact)
fact(5)