def fact(n):
    if n<0:
        print("Invalid number!")
        return None
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number to know the factorail: "))
result = fact(n)

if result is not None:
    print("Factorial = ",result)
