def count_letter_a(text):
    count = text.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes."
    else:
        return "A letra 'a' não aparece na string."

# Exemplo de entrada
string = input("Digite uma palavra: ")
print(count_letter_a(string))
