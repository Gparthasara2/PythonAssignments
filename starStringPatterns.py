# # num = int(input("Enter the number"))
# #
# # count = 0
# # sum = 0
# # i = 1
# # while i < num / 2:
# #     if num % i == 0:
# #         print(str(i) + " ")
# #         count += 1
# #         sum += i
# #
# #     i += 1
# #
# # print("The number of factors is " + str(count))
# # print("The sum of the factors is " + str(sum))
# #
# #
# # j = 3
# # flag = 0
# #
# # if num % 2 == 0:
# #     print(str(num) + " is not a prime number")
# # else:
# #     while j < num / 2:
# #
# #         if j % 2 != 0:
# #
# #             if num % j == 0:
# #                 print(str(num) + " is not a prime")
# #                 break
# #
# #         j += 1
# #     else:
# #         print(str(num) + " is a prime number")
#
#
# # data = range(4,9,2)
# # print(type(data))
# # for d in data:
# #     print(d)
#
# num = int(input("Enter the number"))
#
# for i in range(num + 1):
#     for j in range(i):
#         print("*", end=" ")
#
#     print()
#
# print()
# print()
#
# for i in range(num, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#
#     print()
#
# print()
# print()
#
# k = 2 * num - 2
# for i in range(0, num):
#
#     for j in range(0, k):
#         print(end=" ")
#
#     k -= 2
#
#     for j in range(i + 1):
#         print("*", end=" ")
#
#     print()
#
# print()
# print()
#
# k = 2 * num - 2
# for i in range(0, num):
#
#     for j in range(i + 1):
#         print("*", end=" ")
#
#     k -= 2
#     for j in range(0, k):
#         print(end=" ")
#
#     print()
# # for i in range()

# data = "PYTHON"
# count = 0
# for i in range(len(data)+1):
#
#     for j in range(len(data)-i):
#         count += 1
#         print(end=" ")
#
#     print(data[:i])
#
# i=6
# print(count)
# print(data[:i])

day_dict = {0:"MONDAY" , 1:"TUESDAY" , 2: "WEDNESDAY",  3:"THURSDAY", 4: "FRIDAY", 5: "SATURDAY",6:'SUNDAY' }
day = input("Enter the day of the firstof the month")
day = int(day_dict[day.upper()])
d = int(input("Enter the day you need to find"))
if d > 31 or d <= 0:
    print("Invalid Date")

else:


    print( str(d) + " is " + day_dict[(day + d % 7 - 1) % 7])
# print(day_dict.keys(d(day + d % 7 - 1) % 7))
