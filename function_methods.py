# # functions 
# print('a value')
# print(input('ask for a value'))

# # methods -> functions of datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('e','3'))


# # other functions
# print(abs(-123))
# print(max(10,4))
# print(min(0,1))
# print(len('test'))


# pythagoras theorem
side_a = int(input('The width of the triangle:'))
side_b = int(input('The height of the triangle:'))
hypotenuse = (side_a ** 2 + pow(side_b,2)) ** (1/2)
print('The hypotenuse is: ', round(hypotenuse,2))