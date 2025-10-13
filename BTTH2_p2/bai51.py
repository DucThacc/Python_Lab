# Bài 51: Kiểm tra mật khẩu tốt
def good_password(pw):
    if len(pw) < 8:
        return False
    has_upper = any(ch.isupper() for ch in pw)
    has_lower = any(ch.islower() for ch in pw)
    has_digit = any(ch.isdigit() for ch in pw)
    return has_upper and has_lower and has_digit

pw = input("Nhập mật khẩu: ")
print("Mật khẩu tốt" if good_password(pw) else "Mật khẩu chưa đạt")
