"""Bài 2: về xử lý ngoại lệ FileNotFoundError khi thực hiện chương trình đếm số từ trong file text
"""

filename='alice.txt'
try:
    with open(filename) as f_obj:
        ontents = f_obj.read()
except FileNotFoundError:
    msg = f"Xin lỗi, không tìm thấy file {filename}."
    print(msg)
else:
    # Đếm số từ trong file
    words = ontents.split()
    num_words = len(words)
    print(f"Tệp {filename} có khoảng {num_words} từ.")