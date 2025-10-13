"""Bài 29: Một hình tam giác có thể được phân loại dựa trên độ dài của các cạnh của nó. 
Tất cả ba cạnh của một tam giác đều có cùng độ dài. 
Một tam giác cân có hai cạnh có cùng độ dài và một cạnh thứ ba có độ dài khác nhau,... 
Viết chương trình đọc độ dài ba cạnh của một tam giác từ người dùng. 
Sau đó hiển thị một thông báo cho biết loại tam giác."""

a = float(input("Nhap do dai canh thu nhat: "))
b = float(input("Nhap do dai canh thu hai: "))
c = float(input("Nhap do dai canh thu ba: "))

# Kiểm tra xem có phải tam giác không
if a + b > c and a + c > b and b + c > a:
    # Phân loại tam giác
    if a == b == c:
        print("Day la tam giac deu")
    elif a == b or a == c or b == c:
        print("Day la tam giac can")
    else:
        print("Day la tam giac thuong")
else:
    print("Ba canh nay khong the tao thanh mot tam giac")
