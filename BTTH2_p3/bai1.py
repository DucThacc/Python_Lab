"""Bài 1: Xử lý ngoại lệ FileNotFoundError:
Lỗi này xuất hiện khi mở 1 file mà không tồn tại. Không tồn tại có thể do file chưa được tạo hoặc đường dẫn đến file không đúng.
"""

filename='alice.txt'
try:
    with open(filename) as f_obj:
        ontents = f_obj.read()
except FileNotFoundError:
    msg = f"Xin lỗi, không tìm thấy file {filename}."
    print(msg)

