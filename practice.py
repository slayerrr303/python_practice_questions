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

player1 = input("Player 1, enter your move (rock, paper, or scissors): ").lower()
player2 = input("Player 2, enter your move (rock, paper, or scissors): ").lower()
if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


