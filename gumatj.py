#Program to print Quinary numbers
#By Lalelani Eddie Nene
#14 May 2021


def decimal_to_gumatj(a):
   k = str(a)
   k = (k[1:2])
   return int(k)*(5)+int(a)

def gumatj_multiply(a, b):
   a = (a*b)
   k = str(a)
   return int(k[1:2])*5+int(k)
def gumatj_add(a, b):
   a = (a+b)
   k = str(a)
   return int(k[1:2])*5+2

def gumatj_to_decimal(a):
   b = str(a)
   b = b[1:2]
   return (a-int(b)*5)



choice = input ("Choose test:\n")
action = choice[:1]
print ("calling function")
if action == 'g' or action == 'd':
   num = int(choice[2:])
   if action == 'g':
      answer = gumatj_to_decimal (num)
   else:
      answer = decimal_to_gumatj (num)
elif action == 'a' or action == 'm':
   num1, num2 = map (int, choice[2:].split(" "))
   if action == 'a':
      answer = gumatj_add (num1, num2)
   else:
      answer = gumatj_multiply (num1, num2)
print ("called function")
print (answer)
