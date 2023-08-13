import time
# timeStamp = time.strftime('%H:%M:%S')
# print(timeStamp)

timeStamp1 = int(time.strftime('%H'))
print(timeStamp1)


# timeStamp1 = int(input("Please enter hour: "))
# timeStamp2 = time.strftime('%M')
# print(timeStamp2)

# timeStamp3 = time.strftime('%S')
# print(timeStamp3)12


if(timeStamp1 >= 5 and timeStamp1 < 10):
    print("Good Morning, Mateen")

elif(timeStamp1 >= 10 and timeStamp1 <= 14):
    print('Good Afternoon, Mateen')

elif(timeStamp1 > 14 and timeStamp1 <= 18):
    print("Good Evening, Mateen")

else:
    print("Good Night, Mateen")