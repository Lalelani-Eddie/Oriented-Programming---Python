#PROGRAM TO WORK OUT VECTORS
#BY LALELANI EDDIE NENE
#01 JUNE 2021

#Inputs of the strings of vector A
string1 = input("Enter vector A:\n")
if len(string1)>5:
    a = string1[0:2]
    a = int(a)
    b = string1[3:5]
    b = int(b)
    c = string1[6:8]
    c = int(c)
    vectorA = [a,b,c]
else:
    a = int(string1[0])
    b = int(string1[2])
    c = int(string1[4])
    vectorA = [a,b,c]
#Inputs of the strings of vector B
string2 = input("Enter vector B:\n")

if len(string2)>5:
    d = string2[0:2]
    d =int(d)
    e = string2[3:5]
    e =int(e)
    f = string2[5:8]
    f =int(f)
    vectorB = [d,e,f]
else:
    d = int(string2[0]) 
    e = int(string2[2])
    f = int(string2[4])
    vectorB = [d,e,f]
#calculations of the vector dot product
A = a*d
B = b*e
C = c*f

#calculations of the vector sum
print(f"A+B = [{a+d}, {b+e}, {c+f}]")

print("A.B =", A+B+C)

from math import sqrt
#calculations of the magnitude of the vector 
magA = sqrt(a*a+b*b+c*c)
magB = sqrt(d*d+e*e+f*f)
if magA<1 :
    print("|A| =", str(round(magA, 2))+"0")
    print("|B| =", str(round(magB, 2))+"0")

else:
    
    print("|A| =", round(magA, 2))
    print("|B| =", round(magB, 2))
