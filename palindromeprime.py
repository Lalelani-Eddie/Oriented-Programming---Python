#Program to print the palindromic prime numbers 
#By Lalelani Eddie Nene 
# 15 April 2021

lower = int(input("Enter the start point N:\n"))
upper = int(input("Enter the end point M:\n"))
print("The palindromic primes are:")
for num in range(lower,upper+1):
    reverse = int(str(num)[::-1])
    if num == reverse:
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                print(num)
