# 1. Take 3 numbers and print the largest number

# num1=int(input('enter the first number:'))
# num2=int(input('enter the second number:'))
# num3=int(input('enter the third number:'))
# if num1>num2 and num1>num3:
#     print(f'{num1} is the largest number')
# elif num2>num1 and num2>num3:
#     print(f'{num2} is the largest number')
# elif num3>num2 and num3>num1:
#     print(f'{num3} is the largest number')
    

# 2. Take a month number (1–12) and print the month name

# month = int(input("Enter month number (1-12): "))

# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("May")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("August")
# elif month == 9:
#     print("September")
# elif month == 10:
#     print("October")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")
# else:
#     print("Invalid month number!")



# 3. Write a program to swap two variables3.

# a=int(input('enter first number:'))
# b=int(input('enter second number:'))
# #before swaping
# print('a=',a)
# print('b=',b)
# #after swaping
# print('a=',b)
# print('b=',a)




# 4. You are developing a simple ticket booking system for a movie theatre. The ticket
# price depends on the age of the person and whether they have a membership card. If
# the person is under 12, the ticket is free. If the person is between 12 and 60: if they
# have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
# person is above 60, they get a senior citizen discount, and then ticket costs Rs 100.
# Write a python program using nested if-else to calculate and print the ticket price
# based on the users age and membership status. 

# age = int(input("Enter your age: "))
# member = input("Do you have a membership card? (yes/no): ").lower()

# if age < 12:
#     print("Ticket Price: Free")

# else:
#     if age <= 60:
#         if member == "yes":
#             print("Ticket Price: Rs. 150")
#         else:
#             print("Ticket Price: Rs. 200")
#     else:
#         print("Ticket Price: Rs. 100")   # Senior citizen discount



# 5. A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
#  Next units: Rs 8
# If usage is > 300 units:
#  First 100: Rs 5
#  Next 200: Rs 8
#  Remaining: Rs 10

# units = int(input("Enter electricity usage in units: "))

# if units < 100:
#     cost = units * 5

# elif units <= 300:
#     cost = (100 * 5) + ((units - 100) * 8)

# else:  # units > 300
#     cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)

# print("Total Electricity Bill: Rs", cost)


# 6. Write a complete Python program that:
#  Asks Player 1 to enter their move ( input: rock, paper, or scissors)
#  Asks Player 2 to enter their move ( input: rock, paper, or scissors)
#  Uses only nested if and else statements
#  Prints who wins or if it's a tie

# player1 = input("Player 1, enter your move (rock, paper, or scissors): ").lower()
# player2 = input("Player 2, enter your move (rock, paper, or scissors): ").lower()
# if player1 == player2:
#     print("It's a tie!")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")
# elif player1 == "scissors":
#     if player2 == "paper":
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")

# 7. A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest possible
# number of desks that can be purchased. The program should read three integers: the
# number of students in each of the three classes, a, b and c respectively.
# Hint: In the first test there are three groups. The first group has 20 students and thus
# needs 10 desks. The second group has 21 students, so they can get by with no fewer
# than 11 desks. 11 desks are also enough for the third group of 22 students. So, we
# need 32 desks in total.


# a=int(input('enter number of students in first class:'))
# b=int(input('enter number of students in second class:'))
# c=int(input('enter number of students in third class:'))
# if a%2==0:
#     desk1=a//2
# else:
#     desk1=(a//2)+1
# if b%2==0:
#     desk2=b//2 
# else:
#     desk2=(b//2)+1
# if c%2==0:
#     desk3=c//2
# else:
#     desk3=(c//2)+1
# total_desks=desk1+desk2+desk3
# print('total number of desks required:',total_desks) 


# 8. In a smart building lift system, the lift is currently at floor 5. A person presses
# floor 3. Write a program to decide and display whether the lift should go up, go
# down, or stay at current floor.

# current_floor = 5
# requested_floor = int(input("Enter the floor number you want to go to (0-10): "))
# if requested_floor < current_floor:
#     print("The lift is going down.")
# elif requested_floor > current_floor:
#     print("The lift is going up.")
# else:
#     print("The lift is staying at the current floor.")

# 9. Write a Python program that takes a number as input, first checks if it is positive
# if yes then check whether it is even or odd.

# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is positive.")

#     if num % 2 == 0:
#         print("It is even.")
#     else:
#         print("It is odd.")

# else:
#     print("The number is not positive.")


# 10. Take two numbers and find the greater of the two. If they are equal, check if the
# number is positive, negative, or zero.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}.")
# else:
#     if num1 > 0:
#         print("Both numbers are equal and positive.")
#     elif num1 < 0:
#         print("Both numbers are equal and negative.")
#     else:
#         print("Both numbers are equal to zero.")

# 11. Accept input from user If given number is a multiple of both 3 and 5 prints "Fizz
# Buzz" instead of number If given number is a multiple of 3 but not 5 prints "Fizz"
# instead of number If given number is a multiple of 5 but not 3 prints "Buzz"instead
# of number If given number is not multiple of 3 or 5 prints value as usual.

# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("Fizz Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)


# 12. Snapple is a famous tea drink brand from Queens, New York. Each bottle cap
# comes with a silly fun fact.

# import random

# # Generate a random number between 0 and 5
# num = random.randint(0, 5)

# print("Random number:", num)

# if num == 0:
#     print("Flamingos turn pink from eating shrimp.")
# elif num == 1:
#     print("The only food that doesn't spoil is honey.")
# elif num == 2:
#     print("Shrimp can only swim backwards.")
# elif num == 3:
#     print("A taste bud's life span is about 10 days.")
# elif num == 4:
#     print("It is impossible to sneeze while sleeping.")
# elif num == 5:
#     print("It is illegal to sing off-key in North Carolina.")


# 13. A store gives a 20% discount if the total purchase is above RS 1000 AND the
# customer is a member, or a 10% discount if the purchase is above RS 1000 but the
# customer is not a member. Write a program that takes total_amount and
# is_member (True/False) as input and prints the final amount after applying the
# correct discount (or no discount).

# total_amount = float(input("Enter the total purchase amount: "))
# is_member = input("Are you a member? (yes/no): ").strip().lower()

# if total_amount > 1000:
#     if is_member == "yes":
#         discount = total_amount * 0.2
#     else:
#         discount = total_amount * 0.1
#     final_amount = total_amount - discount
#     print(f"Final amount after discount: Rs {final_amount:.2f}")
# else:
#     print(f"No discount applied. Final amount: Rs {total_amount:.2f}")

# 14. Create a weight conversion program that:
#  Asks the user what their Earth weight is (as a float).
#  Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the
# destination planet.
# To calculate the user's weight: destination weight=Earth weight × relative gravity


# earth_weight = float(input("Enter your weight on Earth (kg): "))
# planet = int(input("Enter planet number (1–7): "))

# if planet == 1:
#     relative_gravity = 0.38
#     planet_name = "Mercury"
# elif planet == 2:
#     relative_gravity = 0.91
#     planet_name = "Venus"
# elif planet == 3:
#     relative_gravity = 0.38
#     planet_name = "Mars"
# elif planet == 4:
#     relative_gravity = 2.53
#     planet_name = "Jupiter"
# elif planet == 5:
#     relative_gravity = 1.07
#     planet_name = "Saturn"
# elif planet == 6:
#     relative_gravity = 0.89
#     planet_name = "Uranus"
# elif planet == 7:
#     relative_gravity = 1.14
#     planet_name = "Neptune"
# else:
#     print("Invalid planet number.")
#     exit()

# destination_weight = earth_weight * relative_gravity

# print(f"Your weight on {planet_name} would be: {destination_weight} kg")


# 15. WAP which accepts marks of four subjects and display total marks, percentage and
# grade. Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>
# pass, less than 40 –> fail

# # Input marks of four subjects
# m1 = float(input("Enter marks of subject 1: "))
# m2 = float(input("Enter marks of subject 2: "))
# m3 = float(input("Enter marks of subject 3: "))
# m4 = float(input("Enter marks of subject 4: "))

# # Calculate total and percentage
# total = m1 + m2 + m3 + m4
# percentage = (total / 400) * 100

# # Display total and percentage
# print("Total Marks =", total)
# print("Percentage =", percentage)

# # Determine grade
# if percentage > 70:
#     print("Grade: Distinction")
# elif percentage > 60:
#     print("Grade: First Division")
# elif percentage > 40:
#     print("Grade: Pass")
# else:
#     print("Grade: Fail")


# 16. Write a program to accept the cost price of a bike and display the road tax to be
# paid according to the following criteria:
# Cost price (in Rs) Tax
# >100000 15%
# >50000 and <=100000 10%
# <=50000 5%

# cost_price = float(input("Enter the cost price of the bike: "))

# if cost_price > 100000:
#     tax = 0.15 * cost_price      # 15%
# elif cost_price > 50000 and cost_price <= 100000:
#     tax = 0.10 * cost_price      # 10%
# else:
#     tax = 0.05 * cost_price      # 5%

# print("Road tax to be paid: Rs", tax)

# 17. A company decided to give bonus to employee according to following criteria: Time period of service Bonus More than 10 years 10% >=6 and <=10 8% Less than 6 years 5%

# service_years = float(input("Enter years of service: "))
# salary = float(input("Enter employee salary: "))

# if service_years > 10:
#     bonus = 0.10 * salary      # 10%
# elif service_years >= 6 and service_years <= 10:
#     bonus = 0.08 * salary      # 8%
# else:
#     bonus = 0.05 * salary      # 5%

# print("Bonus Amount: Rs", bonus)


# 18. Ask the user for a subject score. If it's above 90, congratulate him. If it's between
# 50 and 90, suggest improvement. Otherwise, advise on retaking the course.

# score = float(input("Enter your subject score: "))

# if score > 90:
#     print("Congratulations! Excellent performance!")
# elif score >= 50 and score <= 90:
#     print("Good job, but you can improve further.")
# else:
#     print("You should consider retaking the course for better understanding.")


# 19. Write a program to determine if a candidate is eligible for a job: If the candidate's
# age is >= 18, check if they have a degree. If they have a degree, check their work
# experience: More than 3 years: Display "Highly Eligible." 1-3 years: Display
# "Eligible." Less than 1 year: Display "Under Review."

# age = int(input("Enter candidate's age: "))

# if age >= 18:
#     degree = input("Do you have a degree? (yes/no): ").lower()

#     if degree == "yes":
#         experience = float(input("Enter years of work experience: "))

#         if experience > 3:
#             print("Highly Eligible.")
#         elif experience >= 1:
#             print("Eligible.")
#         else:
#             print("Under Review.")
#     else:
#         print("Not Eligible: Degree required.")
# else:
#     print("Not Eligible: Minimum age is 18.")


# 20. Accept the age, gender ('M', 'F'), number of days and display the wages
# accordingly.
# Age Gender Wage/day
# >=18 and <30 M 700
# F 750
# >=30 and <=40 M 800
# F 850

# age = int(input("Enter age: "))
# gender = input("Enter gender (M/F): ").upper()
# days = int(input("Enter number of working days: "))

# # Determine wage per day
# if age >= 18 and age < 30:
#     if gender == "M":
#         wage_per_day = 700
#     elif gender == "F":
#         wage_per_day = 750
#     else:
#         print("Invalid gender")
#         exit()

# elif age >= 30 and age <= 40:
#     if gender == "M":
#         wage_per_day = 800
#     elif gender == "F":
#         wage_per_day = 850
#     else:
#         print("Invalid gender")
#         exit()

# else:
#     print("Age not eligible for wage calculation.")
#     exit()

# # Calculate total wages
# total_wage = wage_per_day * days

# print("Wage per day:", wage_per_day)
# print("Total wages for", days, "days:", total_wage)


# 21. Write a Python program to simulate a simple ATM with the following
# specifications:
#  Assume the card is valid (is_valid = True)
#  Initial account balance is 50000
#  Correct PIN is 123
#  After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
#  If user selects 1 then ask amount and deduct from balance
#  If user selects 2 then show current balance
#  If user selects 3 then print “Thank you for visiting”
#  Show proper messages for wrong PIN and invalid option Use nested if-else
# statements only.


# is_valid = True
# balance = 50000
# correct_pin = 123

# if is_valid:
#     pin = int(input("Enter your PIN: "))
    
#     if pin == correct_pin:
#         print("\nLogin Successful!")
#         print("1. Withdraw")
#         print("2. Check Balance")
#         print("3. Exit")

#         option = int(input("Enter your option: "))

#         if option == 1:
#             amount = int(input("Enter amount to withdraw: "))
#             if amount <= balance:
#                 balance -= amount
#                 print("Withdrawal successful!")
#                 print("Remaining Balance:", balance)
#             else:
#                 print("Insufficient balance!")
        
#         else:
#             if option == 2:
#                 print("Current Balance:", balance)
#             else:
#                 if option == 3:
#                     print("Thank you for visiting")
#                 else:
#                     print("Invalid option!")
#     else:
#         print("Wrong PIN!")
# else:
#     print("Card is not valid!")



# 22. Create a Python program that greets the user with the message "Welcome to the
# Magic Forest". Then, ask the user whether they want to go "north" or "south". If
# they choose "south", print "Game Over". If they choose "north", ask if they want to
# "cross the river" or "follow the path". If they choose "cross the river", print "Game
# Over". If they choose "follow the path", ask them to choose between "fairy","ogre",
# or "elf". If they choose "ogre" or "fairy", print "Game Over". If they choose "elf",
# print "You Win"

# print("Welcome to the Magic Forest")

# direction = input("Do you want to go 'north' or 'south'? ").lower()

# if direction == "south":
#     print("Game Over")
# elif direction == "north":
#     choice = input("Do you want to 'cross the river' or 'follow the path'? ").lower()

#     if choice == "cross the river":
#         print("Game Over")
#     elif choice == "follow the path":
#         creature = input("Choose one: 'fairy', 'ogre', or 'elf': ").lower()

#         if creature == "elf":
#             print("You Win")
#         elif creature == "fairy" or creature == "ogre":
#             print("Game Over")
#         else:
#             print("Invalid choice")
#     else:
#         print("Invalid choice")
# else:
#     print("Invalid choice")


# .23 Create a Python program that greets the user with the message "Welcome to the
# Haunted House". Then, ask the user whether they want to go "upstairs" or
# "downstairs". If they choose "downstairs", print "Game Over". If they choose
# "upstairs", ask if they want to "enter the room" or "stay outside". If they choose
# "enter the room", print "Game Over". If they choose "stay outside", ask them to
# choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
# "vampire", print "Game Over". If they choose "werewolf", print "You Win"



# print("Welcome to the Haunted House")

# choice1 = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

# if choice1 == "downstairs":
#     print("Game Over")
# elif choice1 == "upstairs":
#     choice2 = input("Do you want to 'enter the room' or 'stay outside'? ").lower()

#     if choice2 == "enter the room":
#         print("Game Over")
#     elif choice2 == "stay outside":
#         creature = input("Choose one: 'ghost', 'vampire', or 'werewolf': ").lower()

#         if creature == "werewolf":
#             print("You Win")
#         elif creature == "ghost" or creature == "vampire":
#             print("Game Over")
#         else:
#             print("Invalid choice")
#     else:
#         print("Invalid choice")
# else:
#     print("Invalid choice")







print('hello world')