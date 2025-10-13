# Bài 54: Ghép danh sách từ kiểu tiếng Anh: a, b and c
def join_english(words):
    n = len(words)
    if n == 0:
        return ""
    if n == 1:
        return words[0]
    if n == 2:
        return words[0] + " and " + words[1]
    return ", ".join(words[:-1]) + " and " + words[-1]

print("Nhập các từ (mỗi từ một dòng, trống để dừng):")
lst = []
while True:
    s = input().strip()
    if s == "":
        break
    lst.append(s)
print(join_english(lst))
