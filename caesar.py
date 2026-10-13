latin = "abcdefghijklmnopqrstuvwxyz"
cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def encrypt(text, shift):
    result = ""
    for char in text:
        low = char.lower()
        if low in latin:
            alphabet = latin
        elif low in cyrillic:
            alphabet = cyrillic
        else:
            result += char
            continue
        new_index = (alphabet.index(low) + shift) % len(alphabet)
        new_char = alphabet[new_index]
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
    return result

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
print(encrypt(text, shift))
