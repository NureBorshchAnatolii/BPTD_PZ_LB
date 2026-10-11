def decrypt_text(encrypted_text, k):
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
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

    return original_text
