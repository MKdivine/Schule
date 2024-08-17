def fibonacci(x):
    i=1
    fibo = [0,1]
    value = 0
    while value < x:
        if ((value + fibo[i]) < x):
            if fibo[i] % 2 == 0:
                value += fibo[i]
        else:
            return value
        fibo.append(fibo[i] + fibo[i-1])
        i += 1
        #print (fibo)
    print (len(fibo))
    return value

Zahl = 4
Potenz = 6
Zielzahl = Zahl*(10**Potenz)
#print(Zielzahl)    

print(fibonacci(Zielzahl))    