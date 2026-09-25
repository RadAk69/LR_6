n = input("Введите любой произвольный текст: ")
a, b = input("Введите две строки через пробел: ").split()
new_text = n.replace(a, b)
print(new_text)
