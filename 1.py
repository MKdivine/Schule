#original by kuzze

def mathfunction(x):
    i=0
    value = 0
    while i < x:
        if i%3 == 0 or i%5 == 0:
            value = value +  i
        i += 1
    return value

print(mathfunction(1000))

#added another solution using a for loop
def mathloop(num):
    sum = 0
    for x in range(0, num):
        if x % 3 == 0 or x % 5 == 0:
            sum +=x
    return sum

print(mathloop(1000))


#soltion as lambda

lol = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(lol)
