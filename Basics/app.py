# Problem 1
'''
Given an integer, n, print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''

# Solution


def compute(num):
    # Find the width of the largest binary value
    width = len(bin(num).replace("0b", ""))

    for index in range(1, num + 1):
        dec_val = f"{index:>{width}}"
        oct_val = f"{oct(index).replace('0o', ''):>{width}}"
        hex_val = f"{hex(index).replace('0x', '').upper():>{width}}"
        bin_val = f"{bin(index).replace('0b', ''):>{width}}"

        print(f"{dec_val} {oct_val} {hex_val} {bin_val}")


compute(17)
