"""Bài 27: Viết chương trình xác định tên của hình dạng dựa trên số cạnh của nó. 
Ví dụ, nhập số 3 thì là hình tam giác, 4 hình tứ giác,... 
Yêu cầu: Chương trình hỗ trợ các hình dạng từ 3 đến 10 cạnh. 
Nếu số cạnh vượt ra bên ngoài phạm vi này thì chương trình sẽ hiển thị thông báo lỗi thích hợp"""

so_canh = int(input("Nhap so canh: "))

if so_canh == 3:
    print("Hinh tam giac")
elif so_canh == 4:
    print("Hinh tu giac")
elif so_canh == 5:
    print("Hinh ngu giac")
elif so_canh == 6:
    print("Hinh luc giac")
elif so_canh == 7:
    print("Hinh that giac")
elif so_canh == 8:
    print("Hinh bat giac")
elif so_canh == 9:
    print("Hinh cuu giac")
elif so_canh == 10:
    print("Hinh thap giac")
else:
    print("Loi: So canh phai tu 3 den 10")
