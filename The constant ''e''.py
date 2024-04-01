
#PROGRAM TO CALCULATE THE VALUE OF EULER CONSTANT
#BY LALELANI EDDIE NENE
#10 JUNE 2021


from math import factorial
def euler_constant(terms):
    a = 0
    for terms in range (0, terms+1):
        j = (terms)
        x = 1
        k = x**(terms)/(factorial(j))
        a += k
    return a
def main():
    
    n = eval(input("Enter the number of terms to use\n"))
    
    n = euler_constant(n)
    print("The aproximation of euler constant is : e ~", n)
    

   
if __name__=='__main__':
    main()
