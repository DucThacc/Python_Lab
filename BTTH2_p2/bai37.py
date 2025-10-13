# Bài 37: Nhập từ đến khi dòng trống, in bỏ trùng, giữ thứ tự
seen = set()
out = []
print("Nhập từ từng dòng (trống để dừng):")
while True:
    s = input().strip()
    if s == "":
        break
    if s not in seen:
        seen.add(s)
        out.append(s)
print(" ".join(out))
