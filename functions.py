# n = 0
# while n < 10:
#     n = n+1
#     print(n)


# n = 1
# while n < 8:
#     n = n+1
#     print(n)

num_list = list(range(1,10))

odd_nums = []
even_nums = []


for x in num_list:
    if x % 2 == 0:
        even_nums.append(x)
    else: 
        odd_nums.append(x)
    
print(odd_nums)
# [1,3,5,7,9]

# while should_run:
# user_input = input("Do you want another one?")