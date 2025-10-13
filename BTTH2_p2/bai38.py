# Bài 38: Nhập nguyên (trống để dừng). In âm trước, rồi 0, rồi dương (giữ thứ tự gốc)
neg = []
zero = []
pos = []
print("Nhập số nguyên từng dòng (trống để dừng):")
while True:
    s = input().strip()
    if s == "":
        break
    x = int(s)
    if x < 0:
        neg.append(x)
    elif x == 0:
        zero.append(x)
    else:
        pos.append(x)
out = neg + zero + pos
print(", ".join(str(v) for v in out))
