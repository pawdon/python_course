def triangle(h: int, a: int, char='*'):
    for i in range(1, h + 1):
        x = round(i * a / h)
        if x == 0:
            x = 1
        print(char * x)


triangle(10, 4)
