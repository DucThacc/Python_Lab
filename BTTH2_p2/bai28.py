"""Bài 28: Số ngày của một tháng thay đổi từ 28 đến 31 ngày. 
Viết một chương trình đọc tên của một tháng từ người dùng dưới dạng một chuỗi. 
Sau đó, chương trình sẽ hiển thị số ngày trong tháng đó 
(Chú ý: Số ngày là 28 hoặc 29 ngày để biểu diễn cho tháng 2)"""

thang = input("Nhap ten thang: ").lower()

if thang in ['thang 1', 'thang mot', 'january', 'jan']:
    print("Thang 1 co 31 ngay")
elif thang in ['thang 2', 'thang hai', 'february', 'feb']:
    print("Thang 2 co 28 hoac 29 ngay")
elif thang in ['thang 3', 'thang ba', 'march', 'mar']:
    print("Thang 3 co 31 ngay")
elif thang in ['thang 4', 'thang tu', 'april', 'apr']:
    print("Thang 4 co 30 ngay")
elif thang in ['thang 5', 'thang nam', 'may']:
    print("Thang 5 co 31 ngay")
elif thang in ['thang 6', 'thang sau', 'june', 'jun']:
    print("Thang 6 co 30 ngay")
elif thang in ['thang 7', 'thang bay', 'july', 'jul']:
    print("Thang 7 co 31 ngay")
elif thang in ['thang 8', 'thang tam', 'august', 'aug']:
    print("Thang 8 co 31 ngay")
elif thang in ['thang 9', 'thang chin', 'september', 'sep']:
    print("Thang 9 co 30 ngay")
elif thang in ['thang 10', 'thang muoi', 'october', 'oct']:
    print("Thang 10 co 31 ngay")
elif thang in ['thang 11', 'thang muoi mot', 'november', 'nov']:
    print("Thang 11 co 30 ngay")
elif thang in ['thang 12', 'thang muoi hai', 'december', 'dec']:
    print("Thang 12 co 31 ngay")
else:
    print("Khong tim thay thang hop le")
