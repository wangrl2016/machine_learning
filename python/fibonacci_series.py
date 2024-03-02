if __name__ == '__main__':
    # The variables a and b simultaneously get the new values 0 and 1.
    a, b = 0, 1
    # The `while` loop executes as long as the condition (here: a < 1000) remain true.
    while a < 1000:
        # Indentation is Python's way of grouping statements.
        # The keyword argument `end` can be used to avoid the newline after the output.
        print(a, end=',')
        # The expressions on the right-hand side are all evaluated first before any of the
        # assignments take place.
        a, b = b, a + b
    # Flush end print function.
    print()
