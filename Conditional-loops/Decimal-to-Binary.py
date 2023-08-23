# Given a decimal number (integer N), convert it into binary and print.

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_num =""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //=2

    return binary_num

decimal_num = int(input())
binary_result = decimal_to_binary(decimal_num)
print(binary_result)
