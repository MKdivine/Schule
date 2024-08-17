def mathfunction(x):
    i=0
    value = 0
    while i < x:
        if i%3 == 0 or i%5 == 0:
            value = value +  i
        i += 1
    return value

print(mathfunction(1000))

