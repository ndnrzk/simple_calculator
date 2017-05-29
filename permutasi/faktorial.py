def factorial():
    n = int(input("n:"))
    last = 1
    number = 1
    while True :
        number = number * n
        n = n-1
        if n < last :
            break
    print (number)

factorial ()