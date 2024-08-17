def primzahlen(y):
    prime = []
    i = 2
    x = 2
    while len(prime) < y:
        while i % x != 0 and i != x :
            x += 1  
        if i == x: 
            prime.append(i)   
        i += 1    
        x = 2 
    return prime

#print(primzahlen(1000))

def primfaktorzerlegung(x):
    i = 0

    LIMIT = 2000
    prim = primzahlen(LIMIT)


    Exit = ""
    while x != 1:
        while x % prim[i] != 0:
            if i == LIMIT-1:
                return "Zahl zu groß"
            else:
                i += 1
        x = x / prim[i]  
        Exit += str(prim[i]) + " "
        i = 0
    return Exit

print (primfaktorzerlegung(100000))