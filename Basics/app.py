# Problem 1
'''
Given an integer, n, print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''

# Solution


# def compute(num):
#     # Find the width of the largest binary value
#     width = len(bin(num).replace("0b", ""))

#     for index in range(1, num + 1):
#         dec_val = f"{index:>{width}}"
#         oct_val = f"{oct(index).replace('0o', ''):>{width}}"
#         hex_val = f"{hex(index).replace('0x', '').upper():>{width}}"
#         bin_val = f"{bin(index).replace('0b', ''):>{width}}"

#         print(f"{dec_val} {oct_val} {hex_val} {bin_val}")


# compute(17)

# Problem 2
'''
You are given a string  consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in .

It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit.

'''

import random
num = '100,000,000.000'


# def compute(num):
#     temp = ''
#     store = []
#     for item in num:
#         if item in [',', '.']:
#             store.append(temp)
#             temp = ''
#         else:
#             temp += item
#     store.append(temp)
#     return store


# def dispaly_results(res):
#     for item in res:
#         print(item)


# res = compute(num)
# dispaly_results(res)


# Problem 3
# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
# def sign_process(data):
#     signs = []
#     for item in data:
#         if item in ['+', '-']:
#             signs.append(item)
#     return signs


# data = ['x**3', '+', 'x**2', '+', 'x', '+', '1']
# first_item = data[0][-1]
# last_item = data[-1]
# store = 0
# while first_item == 0:

#     first_item -= 1


# def get_choices(options):
#     player_choice = input("Enter a choice (rock, paper, scissors): ")
#     options = ['rock', 'paper', 'scissors']
#     computer_choice = random.choice(options)
#     choices = {
#         "player": player_choice,
#         "computer": computer_choice
#     }

#     return choices


# food = ['pizza', 'burger', 'salad']
# dinner = random.choice(food)

# choice = get_choices()

# print(choice)

'''
Problem 4
https://www.hackerrank.com/challenges/compress-the-string/problem
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
'''

# store_data = []
# input_data = '1222311'


# def count_values(current_index, input_data):
#     count = 1

#     for index in range(current_index['index'], len(input_data)):
#         try:
#             if current_index['value'] == input_data[index + 1]:
#                 count += 1
#             else:
#                 break
#         except IndexError:
#             # Prevent out-of-range access
#             break
#     store_data.append((count, current_index['value']))


# for index in range(len(input_data)):
#     current_index = {
#         'index': index,
#         'value': input_data[index]
#     }

#     count_values(current_index, input_data)

# print(store_data)


'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. 
You like all the integers in set  and dislike all the integers in set . Your initial happiness is . 
For each  integer in the array, if , you add  to your happiness. 
If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input
3 2
1 5 3
3 1
5 7
'''

n_m_values = input()
data_array = input()
set_a = input()
set_b = input()


n, m = map(int, n_m_values.split())
data_array = list(map(int, data_array.split()))
set_a = set(map(int, set_a.split()))
set_b = set(map(int, set_b.split()))


control_a = 0
control_b = 0

for item in data_array:
    if item in set_a:
        control_a += 1
    if item in set_b:
        control_b += 1

print(control_a - control_b)
