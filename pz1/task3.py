ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
N = len(ALPHABET)

def find_key_vigenere(cipher, known):
    c = [ch for ch in cipher.lower() if ch in ALPHABET]
    p = [ch for ch in known.lower() if ch in ALPHABET]

    stream = "".join(ALPHABET[(ALPHABET.index(a) - ALPHABET.index(b)) % N]
                     for a, b in zip(c, p))

    for L in range(1, len(stream)):
        if all(stream[i] == stream[i % L] for i in range(len(stream))):
            return stream[:L]
    return stream
