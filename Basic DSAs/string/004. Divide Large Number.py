def divide_large_number(number_str, divisor):
    number = int(number_str)
    result = number // divisor

    return result


number_str = "1260257"
divisor = 37
result = divide_large_number(number_str, divisor)
print(result)
