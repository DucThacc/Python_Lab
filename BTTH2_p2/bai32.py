# Bài 32: Mã hóa/giải mã Caesar với dịch chuyển k
mode = input("Chọn 'e' để mã hóa hoặc 'd' để giải mã: ").strip().lower()
k = int(input("Nhập số dịch chuyển k: "))
s = input("Nhập thông điệp: ")
if mode == 'd':
    k = -k
res = ""
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr((ord(ch)-97+k)%26 + 97)
    elif 'A' <= ch <= 'Z':
        res += chr((ord(ch)-65+k)%26 + 65)
    else:
        res += ch
print(res)
