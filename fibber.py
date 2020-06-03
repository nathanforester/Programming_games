# need input of what to sum
# while the counter is less than the number of items entered
# sum = a + b # recursive sum
# a = b
# b = sum # exchange function
# count += 1 # increment the recursion of the sum
#
# # index the sum []
# # for loop may be needed
# n = int(input())
# x = [1,1]
# for i in range(2, n):
#     x.append(x[-1] + x[-2])
# print(', '.join(str(y) for y in x))
# F(n+1)

# 0, 1, 1, 2, 3, 5, 8, 13
# #  Every number in the Fibonacci sequence (starting from $2$) is the sum of the two numbers preceding
# a = 0
# b = 1
# counter = int(input())
# for numbers in range(2, counter):
#     sum_1 = a + b
#     a = b
#     b = sum_1
#     print(sum_1)


def fibonacci(counter):
    c = 0
    d = 1
    new_value = counter
    for numbers_list in range(2, new_value):
        sum_2 = c + d
        c = d
        d = sum_2
    return sum_2


counter = int(input())
print(fibonacci(counter))







