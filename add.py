def add(a, b, *c):
    __sum = a + b
    for i in list(c):
        __sum += i
    return __sum