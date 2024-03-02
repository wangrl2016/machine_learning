if __name__ == '__main__':
    # The operators +, -, * and / can be used to perform arithmetic.
    print(2 + 2)
    print(50 - 5 * 6)
    # Parenthese () can be used for grouping.
    print((50 - 5 * 6) / 4)
    # Division always returns a floating point number.
    print(8 / 5)

    # Floor division discard the fractional part.
    print(17 // 3)
    # The % operator returns the remainder of the division.
    print(17 % 3)
    # Use the operator to calculate powers.
    print(5 ** 2)

    # The equal sign(=) is used to assign a value to a variable.
    width = 20
    height = 5 * 9
    area = width * height
    print(area)

    # Operators with mixed type operands convert the integer operand to floating point.
    print(4 * 3.75 - 1)