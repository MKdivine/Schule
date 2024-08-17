def sum_even_fibonacci(limit):
    a, b = 1, 2  # Initialisiere die ersten beiden Fibonacci-Zahlen, wobei b die erste gerade Zahl ist
    even_sum = 0  # Variable zur Speicherung der Summe der geraden Fibonacci-Zahlen

    while a <= limit:
        if a % 2 == 0:
            even_sum += a  # Addiere die gerade Fibonacci-Zahl zur Summe
        a, b = b, a + b  # Berechne die nächsten Fibonacci-Zahlen

    return even_sum

# Berechne die Summe aller geraden Fibonacci-Zahlen unter 1 Million
limit = 1000000
result = sum_even_fibonacci(limit)

# Ausgabe des Ergebnisses
print(f"Die Summe aller geraden Fibonacci-Zahlen unter {limit} beträgt: {result}")
