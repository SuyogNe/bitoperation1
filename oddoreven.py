def isEvenOdd(n):
    if(n ^ 1 == n+1):
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if isEvenOdd(num):
    print(num,"even number.")
else:
    print(num,"odd number.")