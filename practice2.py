# items=[3,5,7,9,11,13]
# item=items.pop(4)
# items.insert(1,item)
# items.append(item)
# print(items)


# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# common_elements = first_set.intersection(second_set)
# print("Common elements:", common_elements)
# first_set.difference_update(common_elements)
# print("Updated first set:", first_set)



# st='12345'
# for i in st:
#     print(i,end=' ')

# items=[1,2,3,4,5]
# odd=[]
# even=[]
# for i in items:
#     if i%2==0:
#         print('even')
#         even.append(i)
#     else:
#         print('odd')
#         odd.append(i)
# print('odd=',odd)
# print('even=',even)    


# items=[1,2,'a','b',3,4,5]
# number=[]
# letters=[]
# for i in items:
#     if isinstance(i,int):
#         number.append(i)
#     else:
#         letters.append(i)
# print(number)
# print(letters)

# items=[1,2,20,-22,'a','b',3,-4,5]
# number=[]
# letters=[]
# even=[]
# odd=[]
# for i in items:
#     if isinstance(i,int):
#         number.append(i)
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     else:
#         letters.append(i)
# print('number=',number)
# print('letters=',letters)
# print('even=',even)
# print('odd=',odd)




# question NO.4

# password = ""

# while len(password) < 8:
#     password = input("Enter password: ")

#     if len(password) < 8:
#         print("Security Alert: Password must be 8+ characters")

# print("Password accepted")



# question NO.5
# total = 0
# counter = 1

# while counter <= 50:
#     total = total + counter
#     counter = counter + 1

# print("Final Sum:", total)






# num = int(input("Enter a number: "))
# i = 1

# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i = i + 1






import random

secret = random.randint(1, 50)
attempts = 7

while attempts > 0:
    guess = int(input("Guess the number (1-50): "))
    attempts = attempts - 1

    if guess == secret:
        print("🎉 Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The number was:", secret)



