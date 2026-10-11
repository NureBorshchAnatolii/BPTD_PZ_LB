ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def vigenere(text, key, decrypt=False):
    result = ""
    k = 0
    for ch in text:
        low = ch.lower()
        if low in ALPHABET:
            shift = ALPHABET.index(key[k % len(key)])
            if decrypt:
                shift = -shift
            new = ALPHABET[(ALPHABET.index(low) + shift) % len(ALPHABET)]
            result += new.upper() if ch.isupper() else new
            k += 1
        else:
            result += ch
    return result