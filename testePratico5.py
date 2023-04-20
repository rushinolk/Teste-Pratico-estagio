string = input("Digite uma string: ")

string_invertida = "".join([string[i] for i in range(len(string)-1, -1, -1)])

print("String original:", string)
print("String invertida:", string_invertida)