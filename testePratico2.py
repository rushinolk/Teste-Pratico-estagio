NUM = int(input("Digite um número: "))
F1 = 0
F2 = 1

while F2 < NUM:
    F1, F2 = F2, F1 + F2

if F2 == NUM:
    print(NUM, "pertence à sequência de Fibonacci")
else:
    print(NUM, "não pertence à sequência de Fibonacci")