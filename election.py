#PROGRAM FOR ELECTIONS 
#BY LALELANI EDDIE NENE
#01 JUNE 2021

print("Independent Electoral Commission")
print("--------------------------------")
Lst_votes = []
string = input("Enter the names of parties (terminated by DONE):\n")
while string != "DONE":
    Lst_votes.append(string)
    string = input()
print()
print("Vote counts:")

Lst_votes.sort()
output_lst = []
for output in Lst_votes:
    duplicated_values = Lst_votes.count(output)
    if output not in output_lst:
        output_lst.append(output)
        print(format(output,"10"),"-",duplicated_values)
