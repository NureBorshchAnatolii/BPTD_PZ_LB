alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

encrypted_text = ("Єщеу х ещєщ зщхєбожцж б хбиєбожцж джмеуєу, тґ Ґуизж Дщїснаг, лжн хбє б ежджшаг. "
                  "Зжіадус гжцж, їж хіщ жшєж, пж г іуе вшй, — жшґуяух жїуеує")

k = 23
n = len(alphabet)

original_text = ""

for character in encrypted_text:
    lower_character = character.lower()

    if lower_character not in alphabet:
        original_text += character

    else:
        index = ((alphabet.index(lower_character) + n) - k % n) % n
        decoded_character = alphabet[index]
        original_text += decoded_character.upper() if character.isupper() else decoded_character

print(original_text)

print(original_text == "Нема в мене певнішого і вірнішого лоцмана, як Карпо Летючий, хоч він і молодий. "
                       "Посилаю його, то все одно, що й сам їду, — одказав отаман")