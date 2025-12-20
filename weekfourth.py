
#question 1
# for i in range(1,5):
#     if i%2==0:
#         print(f'number {i} is even')
#     else:
#         print(f'number {i} is odd')


#question 2
# list=[10,20,30,40]
# total=0
# for i in list:
#     total+=i
#     print(f'added {i} running total is {total}')
# print('-------------------' )
# print(f'final total is {total}')


#question 3
# student_names=['Ram','hari','sita']
# print('---Email Greetings Generated--- ')
# for name in student_names:
#     print(f'hi {name},your course approval is ready')


#question 4
# page_counts=[45,30,50,40]
# count=1
# print('---book chapter page counts---')
# for pages in page_counts:
#     print(f'chapter {count} has {pages} pages')
#     count+=1

# chapter_pages = [45, 30, 50, 40]

# print("--- Book Chapter Summary ---")

# for i in range(len(chapter_pages)):
#     print(f"Chapter {i + 1} has {chapter_pages[i]} pages.")
    

#question 5
# given_list = [4, 5, 3, 2]

# product = 1   

# for num in given_list:
#     product *= num

# print("Product of all elements:", product)


#question 6
# num = 11
# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)



#question 7
# students = [
#     {"name": "ram", "math_grade": 43},
#     {"name": "hari", "math_grade": 65},
#     {"name": "sita", "math_grade": 90}
# ]

# for s in students:
#     if s["math_grade"] >= 70:
#         s["status"] = "Approved"
#     else:
#         s["status"] = "Rejected"

# print(students)



#question 8
# a = [1,2,3,4,5]
# b = [3,4,5,6,7]

# for i in a:
#     if i in b:
#         print(i)


#question 9
# lst = [1,2,3,4]
# print(lst[0], lst[-1])


#question 10
# lst = [1,2,3,4]
# for i in lst:
#     if i != 3:
#         print(i)

#question 11
# lst = [1,2,3,4]
# lst[1] = "a"
# lst.remove(3)
# print(lst)

#question 12
# lst = [1,2,3,4,5]
# even = []
# odd = []

# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even:", even)
# print("Odd:", odd)


#question 13
# num = 7
# count = 0

# for i in range(1, num+1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")


#question 14
# lst = [1,2,3,4,"a","b"]
# int_list = []
# str_list = []

# for i in lst:
#     if type(i) == int:
#         int_list.append(i)
#     else:
#         str_list.append(i)

# print(int_list)
# print(str_list)


#question 15
# s = "abc123"
# letters = digits = 0

# for i in s:
#     if i.isalpha():
#         letters += 1
#     elif i.isdigit():
#         digits += 1

# print("Letters:", letters)
# print("Digits:", digits)


#question 16
# username = input("Username: ")
# password = input("Password: ")

# if username and len(password) >= 6:
#     print("Valid")
# else:
#     print("Invalid")

#question 17
# num = 8
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#question 18
# num = 5
# fact = 1

# for i in range(1, num+1):
#     fact *= i

# print(fact)

#question 19
# for i in range(1, 9):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i*j)
#     print()

#question 20
# lst = [1,2,3,4]
# for i in lst:
#     if i < 3:
#         print(i)

#question 21
# total = 0
# for i in range(1, 51):
#     if i % 2 != 0:
#         total += i
# print(total)


#question 22
# total = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         total += i
# print(total)

#question 23
# s = "hello world python"
# count = 0

# for i in s:
#     if i == " ":
#         count += 1

# print(count)


#question 24
# lst = [1,2,3,4]
# new = []

# for i in lst:
#     new.append(i**3)

# print(new)


#question 25
# a = "programming"
# print(a[::-1])


#question 26
# for i in range(50):
#     if i == 8:
#         break
#     print(i)


#question 27
# s = "python"
# for i in s:
#     print(i)


#question 28
# a = ["ram","shyam",1,2]

# for i in a:
#     if type(i) == str:
#         print("Hello!", i)


#question 29
# a = ["ram","shyam",1,2]
# new = []

# for i in a:
#     new.append("Dr." + str(i))

# print(new)


#question 30
# lst = [1,2,3,4]
# new = []

# for i in lst:
#     new.append(i*i)

# print(new)



#question 31
# lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
# new = []

# for i in lst1:
#     if i > 0:
#         new.append(i)

# print(new)


#question 32
# lst = [0,1,2,3,4,5,6]

# for i in lst:
#     if i != 3 and i != 6:
#         print(i)


#question 33
# lst = [1,"a",2.5]
# types = []

# for i in lst:
#     types.append(type(i))

# print(types)


#question 34
# for i in range(5):
#     print(i)
# else:
#     print("Done")



#question 35
# for i in range(105, 0, -7):
#     print(i)


#question 36
# bad_chars = [';', ':', '!', "*"]
# string = "py;th* o:n ! ;py * t*h:o !n"

# for ch in bad_chars:
#     string = string.replace(ch, "")

# print(string.replace(" ", ""))


#question 37
# lst = [1,2,3,4,5,6]
# even = odd = 0

# for i in lst:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even, "Odd:", odd)



#question 38
# total = 0
# for i in range(3, 100):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i

# print(total)



#question 39
# even = odd = 0

# for i in range(1,101):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i

# print(even, odd)



#question 40
# num = 121
# if str(num) == str(num)[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#question 41
# num = 153
# temp = num
# sum = 0

# while temp > 0:
#     d = temp % 10
#     sum += d**3
#     temp //= 10

# if sum == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


#question 42
# s = "programming"
# result = ""

# for i in s:
#     if i not in "aeiouAEIOU":
#         result += i

# print(result)




























