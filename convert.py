#Prgram to transforming a date and time.
#By Lalelani Eddie Nene
#30 April 2021

time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")
hour = int(time[11:13])
minutes = int(time[14:16])
month = int(time[5:7])
year = time[0:3]
unit = (time[8,10])
if hour in range(0,1):
    hour2 = 12
elif hour in range(13,14):
    hour2 = 1
if hour in range(14,15):
    hour2 = 2
if hour in range(15,16):
    hour2 = 3
if hour in range(16,17):
    hour2 = 4
if hour in range(17,18):
    hour2 = 5
if hour in range(18,19):
    hour2 = 6
if hour in range(19,20):
    hour2 = 7
if hour in range(20,21):
    hour2 = 8
if hour in range(22,23):
    hour2 = 9
if hour in range(23,24):
    hour2 = 10

if hour >= 12:
    k = 'pm'
else:
    k = 'am'
    
print(hour2,minutes, k)

if unit in range(4,21):
    n = 'th'
if unit in range(1,2):
    n = 'st'
if unit in range(2,3):
    n = 'nd'
if unit in range(3,4):
    n = 'rd'
z = int(f'{month}')
if month in range(1,2):
    z = 'January'
if month in range(2,3):
    z = 'February'
if month in range(3,4):
    z = 'March'
if month in range(4,5):
    z = 'April'
if month in range(5,6):
    z = 'May'
if month in range(6,7):
    z = 'June'
if month in range(7,8):
    z = 'July'
if month in range(8,9):
    z = 'August'
if month in range(9,10):
    z = 'September'
if month in range(10,11):
    z = 'October'
if month in range(11,12):
    z = 'November'
if month in range(12,13):  
    z = 'December'
    