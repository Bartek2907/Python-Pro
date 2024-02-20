def double_letter(str):
    # Wynik
    result = ''
    for letter in str:
        result += letter * 2
    return result

def secret_function(a, b):
    # Wpisz tutaj swój kod!
    return str(a) + str(b)

print(double_letter("TYLKO WIDZEW"))
print(secret_function(1, 2))
print(secret_function("TYLKO, ", "WIDZEW!"))
