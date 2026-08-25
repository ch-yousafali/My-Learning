# import pyjokes

# print("Importing python jokes")
# print(pyjokes.get_joke())

# # I have installed a module called pyjokes to get jokes in python programming language


# print( '''''

# this is yousuf 
#       am a python developer
#       i am learning python programming language 
#       and wanna in software development field
#       ''')


# # I have used triple quotes to print a multi-line string in python programming language



# import pyttsx3

# # print ("this is yousuf")
# engine = pyttsx3.init()
# engine.say("this is yousuf")
# engine.runAndWait()

# # I install a module called pyttsx3 to convert text to speech in python programming language


# import os
# directory_path = "/"
# files = os.listdir(directory_path)
# for items in files:
#     print(files)


# # How you can access the directories using python 

# a = 43
# b = 4.4
# c = 'yousuf'
# print (type(c))
# print(type(b))
# print(type(a))


# # I have used type() function to check the data type of the variable in python programming language


# import pyjokes

# print("Importing python jokes")
# print(pyjokes.get_joke())

# # I have installed a module called pyjokes to get jokes in python programming language


# print( '''''

# this is yousuf 
#       am a python developer
#       i am learning python programming language 
#       and wanna in software development field
#       ''')


# # I have used triple quotes to print a multi-line string in python programming language



# import pyttsx3

# # print ("this is yousuf")
# engine = pyttsx3.init()
# engine.say("this is yousuf")
# engine.runAndWait()

# # I install a module called pyttsx3 to convert text to speech in python programming language


# import os
# directory_path = "/"
# files = os.listdir(directory_path)
# for items in files:
#     print(files)


# # How you can access the directories using python 

# a = 43
# b = 4.4
# c = 'yousuf'
# print (type(c))
# print(type(b))
# print(type(a))


# # I have used type() function to check the data type of the variable in python programming language


# a = '32.2'
# print(type(a))
# b = float(a)
# print(type(b))

# # I have used float() function to convert a string to a floating-point number in python programming language


# a = input("Enter a number: ")
# b = input("Enter another number: ")
# print('Number 1: ', a)
# print('Number 2: ', b)
# print("The sum of the two numbers is: ", a + b)
# print("the sum of two number is ; ", int(a) + int(b))

# # I have used input() function to take input from the user and then I have used int() function to convert the string input to an integer 


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("a is greater than b: ", a > b)

# # I have used comparison operator '>' to compare two numbers and print the result in python programming language

# name = "Yousuf"
# name_sort = name [0:4]
# print(name_sort)

# character = name[1]
# print(character)

# # I have used string slicing to extract a portion of the string and also to access a specific character in the string 

# name = "Yousuf"

# print(name[-1:-4])
# print(name[0:3])
# print(name[:1])
# print(name[1:])

# # I have used negative indexing to access characters from the end of the string and also used string slicing to extract specific portions of the string 

# b ="abcdefghijklmnopqrstuvwxyz"
# print(b[0:6:3])

# # this is how the string slicing works, the first number is the starting index, the second number is the ending index, and the third number is the step. In this case, it will start from index 0 and go up to index 6 and with a 3 step, it will print the characters at index 0,3, and 6 which are a and d


# word ="abcdefghijklmnopqrstuvwxyz"
# print(len(word))
# print(word.endswith('t'))
# print(word.endswith('z'))
# print(word.startswith('a'))
# print(word.startswith('b'))
# print(word.capitalize())
# print(word.replace('a', 'Z'))

# # I have used len() function to get the length of the string, endswith() method to check if the string ends with a specific character, and startswith() method to check if the string starts with a specific character 



# print("Hello this is Yousuf", "\nI am a python developer", "\nI am learning python programming language", "\nAnd wanna in software development field in Future")
# print("this is \"yousuf\", ")

# # I have used \n to print the string in a new line, know as escape sequesnce character in python

# name = input("Enter your name: ")
# print("Hello Good Morning ", name)

# # another way to print the name of the user is by using f-string 

# print(f"Hello Good Morning {name}")

# # one more method is 

# print("Hello " + name + " Good Morning")

# leter = ''' Dear name
# I am pleased to inform you that you have been selected for the position of |position| at our company. We were impressed with your qualifications and experience, and we believe that you will be a valuable addition to our team.   '''


# name = input ("Enter your name: ")
# position = input("Enter the position you have been selected for: ")
# print(leter.replace("name", name).replace("|position|", position))

# # one thing to remember, if you try to do this sepretely, it will not work because the first replace() method will return a new string and the second replace() method will be applied to the original string, not the modified string. So you have to chain the replace() methods together to get the desired result.


# space = "this is a double   space"

# print(space.find("  "))

# # here i used find() method to find the index of the first occurrence of the double space in the string. It will return the index of the first character of the double space. and if the double space is not found, it will return -1.

# space = "this is a double  space"
# print(space)
# print(space.replace("  ", " "). replace("double", "single"))


# friends = ["Yousuf", "Ali", "Ahmed", "Hassan", "Sami"]

# print(friends[0])

# friends[0] = "Yousuf Ali"

# print(friends[0])

# friends.append("Omar")
# print(friends)
# friends.insert(2, "Zain")
# print(friends)
# friends.remove("Hassan")
# print(friends)
# friends.pop()
# print(friends)

# # I have created a list of friends and then I have accessed the first element of the list using indexing and then I have modified the first element of the list by assigning a new value to it. remember that lists are mutable, which means you can change their elements after they have been created. but not strings and yes indexing works in the same way as it does in strings, you can access the elements of the list using their index.

# l1 = [1, 2, 3, 4, 5]
# l1.reverse()
# print(l1)
# l1.sort()
# print(l1)




# friends =("Yousuf", "Ali", "Ahmed", "Hassan", "Sami")
# # to create and empty tuple you can use empty parentheses like this: 
# empty_tuple = ()
# print(empty_tuple)
# print(friends[0])
# print(type(friends))


# # I have created a tuple of friends and then I have accessed the first element of the tuple using indexing and then I have printed the type of the tuple. remember that tuples are immutable, which means you cannot change their elements after they have been created. but you can access the elements of the tuple using their index just like lists and strings.


# a = (0, 23, 'apple ', 'grapes', 32, 23)

# i = a.index(23)
# print(i)

# # what actually happes here, when the program finds the value it returns, it immediately, here i have two 23 in the above tuple but the very early one was on 1 index it returned me 1 but if it is not at the 1 index it will return the index of the second 23 which is 5, but it will not return both of them, it will return the index of the first occurrence of the value in the tuple.

# a = (0, 23, 'apple ', 'grapes', 32, 23)

# print(2 in a)

# # here i have used the 'in' operator to check if the value 2 is present in the tuple or not. it will return True if the value is present in the tuple and False if it is not present in the tuple.


# fruits = []

# f1 = input("Enter the name of the fruit: ")
# fruits.append(f1)

# f2 = input("Enter the name of the fruit: ")
# fruits.append(f2)

# f3 = input("Enter the name of the fruit: ")
# fruits.append(f3)

# print(fruits)


# # here i have created an empty list called fruits and then i have taken input from the user three times to get the name of the fruit and then i have appended the name of the fruit to the list using the append() method. finally, i have printed the list of fruits.



# marks = []
# m1 = input("Enter the marks of the student: ")
# marks.append(m1)
# m2 = input("Enter the marks of the student: ")
# marks.append(m2)
# m3 = input("Enter the marks of the student: ")
# marks.append(m3)
# m4 = input("Enter the marks of the student: ")
# marks.append(m4)
# m5 = input("Enter the marks of the student: ")
# marks.append(m5)

# print(marks)
# marks.sort()
# print(marks)


# marks = []
# m1 = int(input("Enter the marks of the student: "))
# marks.append(m1)
# m2 = int(input("Enter the marks of the student: "))
# marks.append(m2)
# m3 = int(input("Enter the marks of the student: "))
# marks.append(m3)
# m4 = int(input("Enter the marks of the student: "))
# marks.append(m4)
# m5 = int(input("Enter the marks of the student: "))
# marks.append(m5)

# print(marks)
# marks.sort()
# print(marks)



# # here note that it will sort the marks but the data type is string it will sort the numbers as comes first so if you have to do it properly you have to convert the input to integer before appending it to the list, otherwise it will sort the numbers as strings and not as integers. so you can use int() function to convert the input to integer before appending it to the list.


# l = [1, 2, 3, 4, 5]
# print(sum(l))

# # here i have used the sum() function to get the sum of all the elements in the list. it will return the sum of all the elements in the list.

# marks = {

#     "haryy": 100,
#     "ali": 88,
#     "ahmed": 92,
#     "hassan": 95,
#     "sami": 90
# }

# print(marks)
# print(marks["haryy"])
# print(marks["ahmed"])
# print(marks["ali"])

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get("haryy"))

# marks.update({"haryy": 98})
# print(marks)


# # here i have created a dictionary called marks and then i have accessed the value of the key "haryy" using indexing and then i have printed the items, keys, values, and get() method of the dictionary. finally, i have updated the value of the key "haryy" to 98 using the update() method of the dictionary.



# s = {1, 2, 4, 5, 5}
# print(type(s))
# e = set()
# print(type(e))


# # sets are made in {} and they are unordered colllections of unique elements, to make an empty set you have to use the set() function because if you use {} it will create an empty dictionary and not an empty set. so you can use set() function to create an empty set.



# s = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
# print(s)
# s.pop()
# print(s)

# # pop removes the random element from the set and returns it, since sets are unordered collections of unique elements, you cannot predict which element will be removed when you use the pop() method. so it will remove a random element from the set and return it.

# meaning = {
#     "Python": "A high-level programming language that is widely used for web development, data analysis, artificial intelligence, and scientific computing.",

#     "Java": "A high-level programming language that is widely used for building enterprise applications, mobile applications, and web applications.",

#     "JavaScript": "A high-level programming language that is widely used for building interactive web applications and is also used for server-side programming with Node.js.",
#     "C++": "A high-level programming language that is widely used for building system software, game development, and high-performance applications.",

#     "Ruby": "A high-level programming language that is widely used for web development and is known for its simplicity and productivity.",

#     "PHP": "A high-level programming language that is widely used for web development and is known for its ease of use and flexibility.",

#     "Swift": "A high-level programming language that is widely used for building iOS and macOS applications and is known for its speed and safety.",

#     "Go": "A high-level programming language that is widely used for building scalable and efficient applications and is known for its simplicity and performance.",

#     "Rust": "A high-level programming language that is widely used for building safe and concurrent applications and is known for its memory safety and performance.",
#     "Kotlin": "A high-level programming language that is widely used for building Android applications and is known for its conciseness."
# }

# meanings = input("Enter the name of the programming language: ")
# print(meaning[meanings])

# # so what I did here i created a dictionary called meaning that contains the names of programming languages as keys and their meanings as values. then I took input from the user to get the name of the programming language and then I printed the meaning of the programming language using indexing with the key provided by the user.  





# n = int(input ("Enter a Number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i
# print("The factorial of the number is: ", product)


# n = int(input("Enter a Number: "))

# for i in range (1, n + 1):
#     print (" "* (n - i), end = "")
#     print ("*" * (2*i - 1), end = "" )
#     print(" ")



# n = int(input("Enter a Number: "))
# for i in range (1, n + 1):
#     print (" " * (i - n), end = "")
#     print("*" * i, end = "")
#     print(" ")

# # logics i had used, 01 

# n = int(input("Enter a Number: "))
# for i in range (1, n + 1):
#     print (" " * (i - n), end = "")
#     print("*" * i, end = "")
#     print(" ")


# # logic 02, 

# n = int(input("Enter a Number: "))
# for i in range (1, n + 1):
#     print("*" * i, end = "")
#     print(" ")



# n = int(input("Enter a Number: "))
# for i in range (1, n + 1):
#     if (i ==1 or i == n):
#         print("*" * n, end = "")
#         print(" ")
#     else:
#         print("*", end = "")
#         print(" " * (n - 2), end = "")
#         print("*", end = "")
#         print(" ")


# # remember, that if i input the number 5 the loop gonna run for 5 times, here is how if the value of the i is equals to 1 or is equals to the value of the number that we have entered, then the loop gonna execute the if block and it will print the star n times, otherwise it will execute the else block and it will print a star followed by n-2 spaces and then another star, this way we can create a hollow square pattern of stars.


# n = int(input("Enter a Number: "))
# for i in range (1, 11):
#     print(f"{n} x {11- i} = {n*(11-i)}")

# print("Table Ends here! ") 

# # here i printed the table in reverse order, so the loop will run for 10 times and it will print the multiplication of the number with 10, 9, 8, 7, 6, 5, 4, 3, 2, and 1 in each iteration of the loop. finally, it will print "Table Ends here!" after the loop is finished.


# def avg():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     c = int(input("Enter the third number: "))  
#     average = (a + b + c) / 3
#     return average


# print("The average of the three numbers is: ", avg())


# # here i have defined a function called avg() that takes no parameters and returns the average of three numbers entered by the user. inside the function, i have taken input from the user for three numbers, calculated the average by adding the three numbers and dividing by 3, and then returned the average. finally, i have called the function and printed the result.

# def goodDay(name, ending):
#     print ("Good Day! " + name)
#     print(ending)  

# goodDay("Harry", "Thanks")

# # here i used arguments in the function, the function goodDay() takes two parameters, name and ending. when we call the function, we pass the values "Harry" and "Thanks" as arguments to the function. inside the function, it will print "Good Day! Harry" and then it will print "Thanks".

# # Recurssion is, a prgramming technique where a function calls itself to solve a problem, the best example is of factorial 


# def fac(n):
#     if (n ==1 or n == 0):
#         return 1 
#     return n * fac(n-1)

# print(fac(n= int(input("Enter a Number: "))), "Is the factorial of the number you entered! ")


# # practing randomly, a python atm that works okay, haha! 

# account_balance = 100
# attempts = 5
# deposit_amount = None
# withdraw_amount = None
# print("Welcome to Python's ATM")


# while attempts > 0:
    
#     user_input = input("To withdraw cash press 'W' and to Deposit cash press 'D': ").lower()
    
    
#     if user_input == 'w':
#         print("You pressed W for the withdraw.")
#         withdraw_amount = int(input("Please, Enter the amount: "))
        
#         if withdraw_amount > account_balance:
#             print("You have insufficient funds. Please deposit more cash.")
#         else:
#             account_balance -= withdraw_amount 
#             print(f"You withdrew the following: {withdraw_amount}")
#             print("Your remaining balance is:", account_balance)
#             print("Thanks for using our services, ")

#         break 
        
#     elif user_input == 'd':
#         print("You pressed D for deposit.")
#         deposit_amount = int (input("enter the amount to deposit, "))
#         print(f"You are depositing the following amount {deposit_amount}")
#         account_balance += deposit_amount
#         print("Your new balance is, ", account_balance)
#         print("Thanks for using our services, ")
#         break
        
#     else:
#         attempts -= 1  
        
#         if attempts > 0:
#             print(f"Please enter the right letter. You have {attempts} tries left.\n")
#         else:
#             print("You have 0 tries left. Security lockdown. Exiting ATM.")


# # maza ayaa, sach maa, that was amazingggg!
# # now lets create the digital meezan bank application the process gonna be the same but, a little appendment will be a user name and passcode, 



# correct_user = "Qamar7788"
# correct_pass = "meezanpass@123"

# account_balance = 100
# login_attempts = 5

# print("Welcome to Meezan Bank")

# while login_attempts > 0:
    
#     user_name = input("Enter your username: ")
#     password = input("Enter your password: ")
    
#     if user_name == correct_user and password == correct_pass:
#         print("\nLogin successful! Welcome to Meezan Bank's ATM.")
        
#         user_input = input("To withdraw cash press 'W' and to Deposit cash press 'D': ").lower()
        
#         if user_input == 'w':
#             print("You pressed W for withdraw.")
#             withdraw_amount = int(input("Please enter the amount: "))
            
#             if withdraw_amount > account_balance:
#                 print("You have insufficient funds. Please deposit more cash.")
#             else:
#                 account_balance -= withdraw_amount 
#                 print(f"You withdrew the following: {withdraw_amount}")
#                 print("Your remaining balance is:", account_balance)
#                 print("Thanks for using our services.")
                
#         elif user_input == 'd':
#             print("You pressed D for deposit.")
#             deposit_amount = int(input("Enter the amount to deposit: "))
#             print(f"You are depositing the following amount: {deposit_amount}")
#             account_balance += deposit_amount
#             print("Your new balance is:", account_balance)
#             print("Thanks for using our services.")
            
#         else:
#             print("Invalid selection.")
        
#         break 

#     else:
#         login_attempts -= 1  
        
#         if login_attempts > 0:
#             print(f"You entered the wrong credentials. Please try again. You have {login_attempts} tries left.\n")
#         else:
#             print("You have 0 tries left. Security lockdown. Exiting system.")




# print("Welcome to Digital, Meezan Bank")
# print ("This is the login page of our bank's application")

# correct_user_name = "Yousufali0830"
# correct_password = "Meezanpass@123"

# login_attempts = 5

# while login_attempts > 0:
#     user_name = input ("Please Enter the User Name! ")
#     user_password = input ("Please Enter the Password! ")

#     if user_name == correct_user_name and user_password == correct_password:
#         print ("Welcome to Meezan Bank application, Yousuf ALi")
#         user_input = input("Enter W to withdraw")
#         break




#     else:
#         login_attempts -= 1
#         print("You entered wrong credendials, ")
#         print(f"You have {login_attempts} left ")
#         if login_attempts == 0:
#             print("This account has been locked, due to security purpose, please come back after 24Hours")
#             print("Thanks for using the application")



# # Will do it later, done for now 



# def greatest(a, b, c):
#     if (a>b and a> c):
#         return a
#     elif (b>a and b> c):
#         return b
#     else:
#         (c>a and c> b)
#         return c

# a = int(input ("Enter a Value: "))
# b = int(input ("Enter a Value: "))
# c = int(input ("Enter a Value: "))
# print(greatest(a, b, c))


# def f_to_c(f):
#     return 5*(f-32)/9

# f = int (input(" Enter a value in Farenheit: "))
# c = f_to_c(f)
# print(f"{round(c, 2)} Degree Celius")

# # here i have used the round function to round off the value, upto two decimal places, to avoid new lines in python we use the end function 


# print ("a")
# print ("b")

# print ("c", end="")
# print ("d", end="")


# # this is how we can avoid new lines in python, using the end function 


# def sum(n):
#     if n == 1:
#         return 1
#     return sum (n-1)+ n


# n = int(input ("enter the number, "))
# print(sum(n))

# def pattern(n):
#     if n == 0:
#         print("")
#         return
#     print("*"* n)
#     pattern(n-1)

# pattern(3)

# def rem(l, word):
#     for items in l:
#         l.remove(word)
#         return  l

# l = ["Harry", "Rohan", "Shubam", "Ali", "an" ]
# print(rem(l, "an"))

# #  write a python program to remove the given word from the list and strip it at the same time, 


# def rem(l, word):
#     n = []
#     for items in l:
#         if not (items == word):
#             n.append(items.strip(word))
#     return n 

# l = ["Harry", "Rohan", "Shubam", "Ali", "an"]

# word = "AbC"

# for index, char in enumerate(word):
#     print(index, char)

# # enumerate is a builtin function in python used to return the value with index number, and if you try to print only index it will only print the index and if you want to print the character it will do so as you say, if you want to print both of them, you can do that as well,  

# wor = "ABC"
# for index, char in enumerate(wor):
#     print(index)



# '''
# 1 for snake 
# 0 for water
# -1 for Gun 
# '''


# print("1 is for Snake, 0 is for Water, and -1 is for Gun")
# computer = -1
# youstr = input("Enter you Choice: ")

# youDic = {
#     "s": 1,
#     "w": 0,
#     "g": -1 
# }


# you = youDic[youstr]

# if computer == you:
#     print("Its a Draw! ")
# else:
        
#     if computer == -1 and you == 1:
#         print("You Win! ")
#     elif computer == 1 and you == 0:
#         print("You Lose! ")
#     elif computer == 1 and you == -1:
#         print("You Win! ")
#     elif computer == -1 and you == 0:
#         print("You Lose! ")
#     else:
#         print("Something Went Wrong! ")

# f = open("text.txt")
# data = f.read()
# print (data)
# f.close ()

# st = "this is yousuf, learning the python, have solved today some leetcode problems, today is september 16 2025"

# f = open("myfile.txt", "w")
# f.write(st)
# f.close()

# # now this creates a txt file and store the strings data in that file 


# f=open("myfile.txt")
# content = f.read()
# user_input = input("Enter a word to check in the file 'myfile.txt' ")
# if (user_input in content):
#     print("Yes! ")
# else:
#     print("No! ")
# f.close()

# import random 
# def game():
#     print("You are playing the game! ")
#     score = random.randint (1, 62)
#     with open ("myfile.txt") as f:
#         hiscore = f.read()
#         if hiscore != "":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"Your Score is {score}")
#     if score > hiscore:
#         with open("myfile.txt", "w") as f:
#             f.write(str(score))

#     return score


# game()

# def generateTables(n):
#     tables = ""
#     for i in range (1, 11):
#         tables += f"{n} x {i} = {n*i}\n"

#     with open (f"tables/table_{n}.txt", "w") as f :
#         f.write(tables)

# for i in range(2, 21):
#     generateTables(i)

# # abe or bss nae dil krr rhaa kuch be krnaa koooo 


# with open("text.txt", "w") as f:
#     f.write("")

# # to vipeout the content of a file we do the upper code 

# class Employee:
#     name = "harry"
#     language = "Python"
#     Salary = 12000

# harry = Employee()
# harry.name = "Harry Halison"
# print(harry.language, harry.Salary)

# Rohan = Employee()
# Rohan.name = "Rohan Roro"
# print(Rohan.language, Rohan.Salary)

# # here rohan.name is object attribute as they belong to some object while salary and language are class attribute as they belong to class employee, think of this in this way, a class where all students will get same lecture and an individual class where student might get good studies, or may be in detail and this is also known as instance attribute, 

# class Employee:
#     Languae = "Python"
#     Salary = 120000


# harry = Employee()
# harry.Languae = "JavaScript"
# print(harry.Languae)

# # here what happens the instance attribute will overright the previous value and take the new value, like here language is python by default but, if we look at the instance attribute i am assigning the langusge is JavaScript so it will take the new attribute instead of old one 

# class Employee:
#     Languge = "Go"
#     Salary = 1200000

#     def getinfo(self):
#         print(f"The salary is {self.Salary} and the language is {self.Languge}. ")

# harry = Employee()
# harry.getinfo()

# # so what is happening here is we are using the self parameter, what it is, we are actually pointing the name tag that refers to sepecific object like in the class we made the function but also, we want to, use that values so we gonna call the self parameter, more it is not necessary to use self word all the time you can even use banna 
  


# class Employee:
#     Languge = "Go"
#     Salary = 1200000

#     def getinfo(bananna):
#         print(f"The salary is {bananna.Salary} and the language is {bananna.Languge}. ")

# harry = Employee()
# harry.getinfo()

# class Employee:
#     Languge = "Go"
#     Salary = 1200000

#     def getinfo(bananna):
#         print(f"The salary is {bananna.Salary} and the language is {bananna.Languge}. ")


#     @staticmethod
#     def Greet():
#         print("Good Morning! ")

# harry = Employee()
# harry.getinfo()
# harry.Greet()

# # so what does the static method dis, it will bypass that ot does not need the object means self or something else and static method are decorator, 

# class Employee:
#     Language = "C++"
#     Salary = 130000

#     def __init__(self):
#         print("This is the Object, ")

#     def getinfo(self):
#         print(f"the language is {self.Language} and the salary is {self.Salary}. ")
#     @staticmethod
#     def greet():
#         print("Good Morning! ")

# harry = Employee()
# harry.greet()
# print(harry.Salary, harry.Language)

# # the init is a dunder method it is automatically called, and all the methods starting with the __ are dunder, only the init dunder method is called not all methods are always called, how it works 



# class Employee:
#     Language = "C++"
#     Salary = 130000

#     def __init__(self, name , salary, language):
#         # print("This is the Object, ")
#         self.name = name 
#         self.salary = salary
#         self.language = language

#     def getinfo(self):
#         print(f"the language is {self.Language} and the salary is {self.Salary}. ")
#     @staticmethod
#     def greet():
#         print("Good Morning! ")

# harry = Employee("harry", 120000, "Go")
# print(harry.name, harry.salary, harry.language)




# class Programmer:
#     Company = "Microsoft"
#     def __init__(self):
#         self.name =  input('Enter your name: ')
#         self.pincode = input("Enter your Pincode: ")
#         self.languages = input("Enter your Language: ")

# p = Programmer()
# print("Please Check the Info you Entered: ")
# print("You work at ", p.Company)
# print("Your name is ", p.name)
# print("Your Language is ", p.languages)
# print("Your Pincode is ", p.pincode)


# class Demo:
#     a = 4

# o = Demo()
# print(o.a)
# o.a = 0

# print(o.a)
# print(Demo.a)

# # on thing is here is that class is something that has been set so it wont change the attribute of the class 


# class Emplyee:
#     comapny = "Microsoft"
#     def show (self):
#         print(f"This is the Employee class, and the company is {self.comapny}")

# # here i have inherited the Employee class in the Programmer class, so the Programmer class will have access to the attributes and methods of the Employee class, and also it has its own attribute comapny which is different from the Employee class, so when we create an object of the Programmer class and call the show() method, it will print the company name as Google instead of Microsoft because it is using the comapny attribute of the Programmer class instead of the Employee class. but if we create an object of the Employee class and call the show() method, it will print the company name as Microsoft because it is using the comapny attribute of the Employee class.


# class Programmer(Emplyee):
#     comapny = "Google"
#     def show(self):
#         print(f"This is the Programmer class, and the company is {self.comapny}")
#     def showlanguage(self):
#         print("The language is Python! ")

# p = Programmer()
# e = Emplyee()

# print(p.showlanguage(),p.comapny, e.comapny)


# class Programmer :
#     name = "Yousuf"

# class A:
#     def __init__(self):
#         self.x = 10

# class B(A):
#     def __init__(self):
#         self.y = 20

# b = B()
# print(b.x)
# print(b.y)

# # Problem:

# # Given a list of integers, return a new list that contains only the unique elements that appear more than once — i.e. the duplicates. Preserve the order of first occurrence.

# # Example:
# # Input:  [1, 3, 2, 3, 4, 1, 5, 2, 6]
# # Output: [3, 1, 2]
# # Rules:

# # No importing any library
# # Don't use Counter or any shortcut
# # Write it from scratch using basic Python

# def find_duplicates(lst):
#     duplicates = []
#     seen = set()
    
#     for num in lst:
#         if num in seen and num not in duplicates:
#             duplicates.append(num)
#         else:
#             seen.add(num)
    
#     return duplicates   

# # Problem:

# # Write a function that checks if two strings are anagrams of each other. Two strings are anagrams if they contain the same characters in the same frequency, just in different order.

# # Examples:
# # "listen", "silent"  → True
# # "hello",  "world"   → False
# # "Triangle", "Integral" → True  (case insensitive)
# # Rules:

# # Case insensitive
# # No importing anything
# # No using sorted() — handle it manually

# def anagrams(word1, word2):
#     word1 = word1.lower()
#     word2 = word2.lower()

#     freq1 = {}
#     for letter in word1:
#         if letter in freq1:
#             freq1[letter] += 1
#         else:
#             freq1[letter] = 1

#     freq2 = {}
#     for letter in word2:
#         if letter in freq2:
#             freq2[letter] += 1
#         else:
#             freq2[letter] = 1

#     return freq1 == freq2

# print(anagrams("listen", "silent"))   # True
# print(anagrams("hello", "world"))     # False
# print(anagrams("Triangle", "Integral")) # True


# # Problem:

# # Write a function that takes a string and returns the first non-repeating character. If all characters repeat, return None.

# # Examples:
# # "swiss"   → "w"
# # "aabbcc"  → None
# # "abacaba" → "b"
# # Rules:

# # No imports
# # Case insensitive
# # Write steps in plain English first — then code

# def repeat(s):
#     character_count = {}
#     for char in s:
#         if char in character_count:
#             character_count[char] += 1
#         else:
#             character_count[char] = 1

#     for char in s:
#         if character_count[char] == 1:
#             return char
#     return None

# print(repeat("swiss"))   # "w"  
# print(repeat("aabbcc"))  # None
# print(repeat("abacaba")) # "b"

def find_duplicates(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    duplicates = []
    for num, count in counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates

print( find_duplicates([1, 3, 2, 3, 4, 1, 5, 2, 6]))  
