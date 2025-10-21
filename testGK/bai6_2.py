
try:
    with open(r'E:\Python_Lab\testGK\doanhthu.txt', 'r') as f:
        Doanh_Thu = [int(x) for x in f.read().split(',')]
    tong_tien = sum(Doanh_Thu)
    trung_binh = tong_tien / len(Doanh_Thu)
    tien_ban_min_max = {
        "Tháng bán thấp nhất: ": min(Doanh_Thu),
        "Tháng bán cao nhất: ": max(Doanh_Thu),
    }

    print(f"Tổng số tiền bán: {tong_tien}")
    print(f"trung bình: {trung_binh}")
    print(f"Từ điển:  {tien_ban_min_max}")
except FileNotFoundError:
    print(f"LỖI: Không tìm thấy file tại .")
except ValueError:    
    print(f"LỖI: Dữ liệu không hợp lệ.")

