if __name__ == '__main__':
    a, b = 0, 1
    while a < 1000:
        print(a, end=',')
        a, b = b, a + b
    print()
