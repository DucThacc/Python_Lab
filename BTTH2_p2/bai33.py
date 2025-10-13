# Bài 33: Kiểm tra Palindrome
s = input("Nhập chuỗi: ")
t = "".join(ch.lower() for ch in s if ch.isalnum())
print("Palindrome" if t == t[::-1] else "Không phải palindrome")
