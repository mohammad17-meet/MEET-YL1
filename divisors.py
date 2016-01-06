def divisors():
    n = int(input("give number:"))
    number=1
    while (number <= n):
        if(n%number == 0):
            print(number)
        number+=1
