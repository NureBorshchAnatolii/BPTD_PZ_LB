TABLE = {}
for i, ch in enumerate("АИТЕСНО"):
    TABLE[ch] = str(i + 1)
for row, letters in {"8": "БВГҐДЄЖЗІЇ", "9": "ЙКЛМПРУФХЦ", "0": "ЧШЩЬЮЯ "}.items():
    for i, ch in enumerate(letters):
        TABLE[ch] = row + "1234567890"[i]
BACK = {v: k for k, v in TABLE.items()}

def otp(data, key, decrypt=False):
    k = "".join(TABLE[c] for c in key.upper())
    if not decrypt:
        data = "".join(TABLE[c] for c in data.upper())
    sign = -1 if decrypt else 1
    res = "".join(str((int(d) + sign * int(k[i % len(k)])) % 10)
                  for i, d in enumerate(data))
    if not decrypt:
        return res
    out, i = "", 0
    while i < len(res):
        code = res[i] if res[i] in "1234567" else res[i:i + 2]
        out += BACK[code]
        i += len(code)
    return out