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

num = '100,000,000.000'


def compute(num):
    temp = ''
    store = []
    for item in num:
        if item in [',', '.']:
            store.append(temp)
            temp = ''
        else:
            temp += item
    store.append(temp)
    return store


def dispaly_results(res):
    for item in res:
        print(item)


res = compute(num)
dispaly_results(res)
