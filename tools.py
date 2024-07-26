# f strings
# user_name = 'Paul'
# user_age = 16
# user_information = f'{user_name} is {user_age} year old'
# bad_approach = user_name + ' is ' + str(user_age) + ' years old' # bad aproach
# print(user_information)


# single line if statements
# user_name = 'Ana'
# user_age = 20
# user_status = 'Adult' if user_age >= 18 else 'Child'

# if user_age < 18:
#     user_status = 'Child'
# else:
#     user_status = 'Adult'

# list comprehension
#simple_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a','b','c') if j == 'a']
# for i in range(0,10,1):
#     simple_list.append(i)
#print(simple_list)

# lambda functions
# def double_value(num):
#     return num * 2
# double_value = lambda num: num * 2
# print(double_value(10)) 

# # some functions want a function as an argument
# random_list = [('Anna', 25), ('Paul', 30),('Lisa', 10)]
# sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])
# print(sorted_list)

# exercise
battleship_board = [f'{letter}{num}' for letter in ('A','B','C','D','E') for num in range(1,6) if f'{letter}{num}' != 'C3']
print(battleship_board)