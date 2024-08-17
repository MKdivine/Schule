def primzahlen(y):
    prime = []
    i = 2
    x = 2
    while len(prime) < y:
        while i % x != 0 and i != x:
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
    ausgabe = []

    while x != 1:
        while x % prim[i] != 0:
            if i == LIMIT-1:
                return 0
            else:
                i += 1
        x = x / prim[i]
        ausgabe.append(prim[i]) 
        i = 0
    return ausgabe


def Output_function(number):
    Output = primfaktorzerlegung(number)
    Awnser = "Die Primfaktorzerlegung von " + str(number) + " = "
    i = 0
    
    if Output == 0:
        return "Die Zahl ist zu groß"
    else:
        print(Output)
        while i < len(Output)-1:
            Awnser += str(Output[i]) + "x"
            i += 1
        Awnser += str(Output[i])
        return Awnser


User_Input = 600851475143
print (Output_function(User_Input))
