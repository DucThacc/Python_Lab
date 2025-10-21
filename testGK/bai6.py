file_path = r"E:\Python_Lab\testGK\doanhthu.txt"

try:
    # a) Đọc file và chuyển thành danh sách số nguyên
    with open(file_path, 'r', encoding='utf-8') as f:
        Danh_Thu = [int(s.strip()) for s in f.read().split(',')]

    if not Danh_Thu:
        print("Lỗi: File rỗng hoặc dữ liệu không hợp lệ.")
    else:
        # b) Tính tổng
        tong = sum(Danh_Thu)
        
        # c) Tính trung bình
        trung_binh = tong / len(Danh_Thu)
        
        # d) Tạo từ điển
        Tien_ban_min_max = {
            "Tháng bán thấp nhất": min(Danh_Thu),
            "Tháng bán nhiều nhất": max(Danh_Thu)
        }

        # In tất cả kết quả
        print(f"a) Dữ liệu doanh thu: {Danh_Thu}")
        print(f"b) Tổng doanh thu: {tong}")
        print(f"c) Doanh thu trung bình: {trung_binh:.2f}")
        print(f"d) & e) Min/Max: {Tien_ban_min_max}")

except FileNotFoundError:
    print(f"a) LỖI: Không tìm thấy file tại '{file_path}'.")
except ValueError:
    print("Lỗi: Dữ liệu trong file không phải là số hợp lệ.")
except Exception as e:
    print(f"Lỗi không mong muốn: {e}")