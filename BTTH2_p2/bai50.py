# Bài 50: Tạo mật khẩu ngẫu nhiên dài 7..10 với ký tự ASCII 33..126
import random
def gen_password():
    length = random.randint(7, 10)
    s = ""
    for _ in range(length):
        s += chr(random.randint(33, 126))
    return s

print(gen_password())
