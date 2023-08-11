# a = "mateen nawaz"

# para = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged 86."

# str1 = "welcomeMateen86"
# str2 = "welcomeMateeen     "

# print(a)
# print(a.upper())
# print(a.lower())
# print(a.rstrip())
# print(a.replace("Nawaz", "Mirani"))
# print(a.capitalize())
# print(a.__len__())



# print(para.__len__())
# print(para.split(" "))
# print(para.center(100))

# Count is used for count the words pressence in the string
# print(para.count('a'))
# print(a.endswith('waz')) # it check's that the given string ends on this character


# Find() this method is used the find the searching index
# print(para.find('scrambled'))

# index() this method is throw an error if string not exist
# print(para.index('Mateen'))


# It return true only if A-Z, a-z, 0-9
# print(str1.isalnum())

# It return true only if A-Z, a-z
# print(str2.isalpha())

# It return true only if all character of string small
# print(str2.islower())

# It return true only if all character of string printable
# print(str2.isprintable())

# It return true only if string contain any white-space
# print(str2.isspace())


# It return true only if the the letter of each word in string is capitalize
# print(str2.istitle())


# This method is used to swap between lower and upper cases of letter
# print(str2.swapcase())

# This method is used to capitalize the each starting letter of word
# print(para.title())


# Conditional statements
# x = int(input("Please enter your age: "))
# print("enter value of x is: ", x)

# if(x == 18):
#     print("You've to drive the bike!")
# elif( x > 18):
#     print("You've to drive a car!")
# else:
#     print("Invalid input")



# Another example related to conditions
# applePrice = int(input("Please enter a apple price: "))
# budget = int(input("Please enter a budget: "))

# if(budget - applePrice > 100):
#     print("Please buy more apple")
# elif(budget - applePrice == 100):
#     print ('Please buy just 1kg more apple.')
# else:
#     print("Please do not buy any more apple!")



# Match or switch cases

# y = int(input("Please enter a value of y: "))

# match y:
#     case 0:
#         print(y, "is equal to zero")
#     case _ if y >= 100:
#         print("Entered value is greater than: ", y)
#     case _ if y < 100:
#         print("Entered value is less than: ", y)
    
#     case _ : 
#         print("Invalid input!")



# Loops

# 1. uses of for loop with string
# myName = "Mateen"

# for i in myName:
#     print(i)
    
#     if(i == 'n'):
#         newChar = input("Please enter a new alternative letter: ")
#         updated = myName.replace(i, newChar)
#         print(updated)


# 2. uses of loop with list
# itemList = ["Apple", "Mango", "Banana", "Orange"]

# for index, item in enumerate(itemList):
#     print(item)
    
#     if item == "Banana":
#         newInp = input("Please enter a new value: ")
#         itemList[index] = newInp
#         print(itemList)
        

# Range 
# for i in range(1, 20001):
#     print(i)

# for x in range(1, 18, 2):
#     print(x)


# while loop
# i = 0
# while(i < 6):
#     print(i)
#     i = i + 1

# print("Done with the loop")

# Decrement loop
# x = 8
# while (x > 0):
#     print(x)
#     x = x - 1
# else:
#     print("after completing the loop")
    
    
# Uses of break statement
# for i in range(10):
#     if(i == 8):
#         break
#     print("8 X ", i + 1, "=", 8 * (i + 1))

# print("Loop ko chor kr nikal gaya!")


# uses of continue statement
# for i in range(10):
#     if(i == 9):
#         continue
#     print("8 X ", i + 1, "=", 8 * (i + 1))

# print("Iteration ko chor kr nikal gaya!")

# Implement Do-while loop
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if(i%100 == 0):
#         break

# print("Loop terminate")


# Let's start with the functions
def calculcateMean(a,b):
    mean = (a*b)/(a+b)
    print("Mean of two number is: ", mean)
    

calculcateMean(8, 6)


def greeting(x):
    if(x == 6 & x <= 10):
        print("Good Morning!, Mateen")
    elif (x > 10 & x <= 12):
        print('Good Afternoon!, Mateen')
    else:
        print("Good Night!, Mateen")
        


greeting(8)