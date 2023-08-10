import time
# timeStamp = time.strftime('%H:%M:%S')
# print(timeStamp)

timeStamp1 = int(time.strftime('%H'))
print(timeStamp1)

# timeStamp2 = time.strftime('%M')
# print(timeStamp2)

# timeStamp3 = time.strftime('%S')
# print(timeStamp3)

if(timeStamp1 >= 5 & timeStamp1 < 10):
    print("Good Morning, Mateen")

elif(timeStamp1 >= 10 & timeStamp1 <= 14):
    print('Good Afternoon, Mateen')

elif(timeStamp1 > 14 & timeStamp1 <= 18):
    print("Good Evening, Mateen")

else:
    print("Good Night, Mateen")