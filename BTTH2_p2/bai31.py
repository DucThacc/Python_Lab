# Bài 31: Mã hóa Caesar shift 3
s = input("Nhập thông điệp: ")
res = ""
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr((ord(ch)-97+3)%26 + 97)
    elif 'A' <= ch <= 'Z':
        res += chr((ord(ch)-65+3)%26 + 65)
    else:
        res += ch
print(res)
