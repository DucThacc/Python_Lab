# Bài 35: Lọc số lẻ từ danh sách nhập bởi dấu phẩy
s = input("Nhập dãy số, phân tách bởi dấu phẩy: ")
nums = [int(x.strip()) for x in s.split(",") if x.strip() != ""]
odds = [str(x) for x in nums if x % 2 == 1]
print(",".join(odds))
