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
# def calculcateMean(a,b):
#     mean = (a*b)/(a+b)
#     print("Mean of two number is: ", mean)
    
# calculcateMean(8, 6)

# def greeting(x):
#     if(x == 6 & x <= 10):
#         print("Good Morning!, Mateen")
#     elif (x > 10 & x <= 12):
#         print('Good Afternoon!, Mateen')
#     else:
#         print("Good Night!, Mateen")
        
# greeting(8)


# 1. Default arguements
def average(a=9, b=1):
    print("The average of two number is: ", (a+b)/2)

# If i simply call the function then it will take the default args
average()

# IF i pass the args when calling the function then it replace the default args with passing args
average(5, 1)

# Change the keyword args
average(b=11, a=1)


# Example #2
def fullName(firstName, middleName="Nawaz", lastName="Mirani"):
    print("My full name is: ", firstName, middleName, lastName)

# IF function multiple parameters but we define all parameters as a default except 1 
fullName("Mateen")



# Args lengthe --> kind of tuple example
def averageUp(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print( "The average of numbers is: ", sum / len(numbers)) # len(numbers) define args counts
    
averageUp(8, 9, 18, 3, 7)


# Dictionary Example 
def disFun(**args):
    print("My full name is: ", args['fName'], args['mName'], args['lName'])

disFun(fName = "Mateen", mName = "Nawaz", lName = "Mirani")


# Returning value of function
def returnFun(*args):
    sum = 0
    for i in args:
        sum = sum + i
    
    return sum / len(args)

x = returnFun(9, 12, 3, 5)
print("The average of numbers is: ", x)


# Examples of list 
mixList = [1, 4, 7, 'Mateen', True, 3.2]

print(mixList)
print(type(mixList))
print(mixList[3])

# Access element of list in reverse orders
print(mixList[-4])
print(mixList[len(mixList) - 4])
print(mixList[6 - 4])
print(mixList[2])


# By using "in" keywords we check that this searching is in the list or not
if 9 in mixList:
    print("Yes")
else:
    print("No")
    

# Checking something from string
str8 = 'Mateen Nawaz'
if "een" in str8:
    print("Yes")
else:
    print("No")
    
    
    

# JumIndex in list
marks = [12, 32, 43, "Mateen", True, 43, 86, "Engineer"]

print(marks)

# start printing from index 1 and ends on 6
print(marks[1:6])


# start printing from index 1 and ends on 6 and jum with 2 indexs
print(marks[1:6:2])


# IF we empty the array then Python consider [0:len(marks)]
print(marks[:])


# Let we check that the negative numbers
print(marks[-1:-3])


# List comprehension
compList = [x for x in range(8)]
print(compList)


compList = [x*x for x in range(8)]
print(compList)


compList = [x for x in range(8) if x%2 == 0]
print(compList)


newList = [1, 2, 3, 4]
print(newList)


# Add new element in the end of array
newList.append(5)
print(newList)

# Reverse the order of element array
newList.reverse()
print(newList)

# Sorting the element of array in reverse orders
newList.sort(reverse=True)
print(newList)



# Return the index number of element
print(newList.index(2))


# Count the number of occurence in a list
print(newList.count(1))


# Make the copy of existing array
copiedArray = newList.copy()
copiedArray[0] = 12
print(copiedArray)


# Insert the new element into existing list element
copiedArray.insert(2, 86)
print(copiedArray)


# add new list into the existing list
m = [777, 888, 999]
newList.extend(m)
print(newList)

# Here we start with TUPLES
tup = (1, 21, 86)
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])

# If you write just one element inside the prenthesis then python consider the data type is int
# Tuples are unchangable
tup1 = (1)
print(type(tup1))


tup2 = (12, 21, 43, "Mateen", True, "Mirani", 89)
print(tup2)

# Slicing of tuple
tup3 = tup2[1:4]
print(tup3)


# Changed Tuples
countries = ("Pakistan", "UK", "Spain", "Germany", "Italy")
print(countries)

# change tuple into list
temp = list(countries)
print(temp)

# Now we can change the list 
temp.append("Europe")
print(temp)


# Remove an item from list
temp.pop(3)
print(temp)

countries = tuple(temp)
print(countries)

# concate the different tuples
tuple1 = (12, 32, "Mateen", 88)
tuple2 = (43, 86, "Mirani", True, "Pakistan")

print(tuple1 + tuple2)

# Count the element of tuple
print(tuple1.count(32))


# find the index of passing value on tuple
res = tuple1.index(12)
print(res)