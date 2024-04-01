#Program to print user month calendar
#By Lalelani Eddie Nene
#10 April 2021

month = input("Enter the month ('January', ...,'December'):\n")
day = input("Enter the start day ('Monday', ..., 'Sunday'):\n")
n = 1
print("Mo Tu We Th Fr Sa Su")
for k in range (0,7):
    print(format(n+k, "2"), end=" ")
print()
for a in range (7,14):
    print(format(n+a, "2"), end=" ")
print()
for b in range (14,21):
    print(format(n+b, "2"), end=" ")
print()
for c in range (21,28):
    print(format(n+c, "2"), end=" ")
print()
for d in range (28,30):
    print(format(n+d, "2"), end=" ")
print()
