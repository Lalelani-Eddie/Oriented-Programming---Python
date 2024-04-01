#PROGRAM TO ESTIMATE THE THE APPROXIMATE ROOT
#BY LALELANI EDDIE NENE
#12 JUNE 2021

def newton_raphson_method():
    # Xo which is equal to 2 
    x = 2 
    k = 0
    while k<1e-8 :
        k = (x**3 - 10)/(3*x**2)
        r = x - k
        x = r
    return x
    #let  f(xn)/f''(x) be equal to k     
  
    #let Xn+1 be equal to "root"
    

R = newton_raphson_method()
print (" The root of x^3 -10 is:", R)