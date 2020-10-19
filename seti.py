def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    if decimal_number > 0:
        return decimal_to_binary(decimal_number // 2) + [decimal_number % 2]
    else:
        return []


def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    result = 0
    n = 0
    for i in reversed(binary_digits):
        result += i * 2 ** n
        n += 1
    return result


def decimal_to_base(decimal_number, dest_base):
    """Returns the digits in destination_base representation of the decimal number"""
    if decimal_number > 0:
        return decimal_to_base(decimal_number // dest_base, dest_base) + [decimal_number % dest_base]
    else:
        return []


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    result = 0
    n = 0
    for i in reversed(digits):
        result += i * original_base ** n
        n += 1
    return result


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    result = ""
    hex_dict = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    for x in digits:
        if not x < base:
            raise ValueError("At last one of the digits in the list is greater then base")
    if (base > 16):
        raise ValueError("The input parameter base is greater then 16")

    for x in digits:
        if (x < 10):
            result += str(x)
        else:
            result += hex_dict[x]
    return result


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    return decimal_to_base(base_to_decimal(original_digits, original_base), destination_base)


print(decimal_to_binary(20) == [1, 0, 1, 0, 0])
print(binary_to_decimal([1, 0, 1, 0, 0]))
print(decimal_to_base(20, 8))
print(base_to_decimal([2, 4], 8))
print(digits_as_string([2, 15, 9, 11], 16))
print(convert_base([1, 1, 2, 0], 3, 2))
