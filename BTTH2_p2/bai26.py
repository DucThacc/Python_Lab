"""Bài 26: Viết một chương trình đọc một chữ cái từ người dùng. 
Nếu người dùng nhập a, e, i, o hoặc u thì chương trình hiển thị một thông báo cho biết rằng chữ cái đã nhập là nguyên âm (xét ngôn ngữ Anh). 
Nếu người dùng nhập y thì chương trình sẽ hiển thị một thông báo cho biết có thể y là nguyên âm hoặc phụ âm. 
Nếu không phải các trường hợp trên, chương trình sẽ hiển thị một thông báo cho biết rằng chữ cái là phụ âm"""

chu_cai = input("Nhap mot chu cai: ").lower()

if chu_cai in ['a', 'e', 'i', 'o', 'u']:
    print(f"'{chu_cai}' la nguyen am")
elif chu_cai == 'y':
    print(f"'{chu_cai}' co the la nguyen am hoac phu am")
else:
    print(f"'{chu_cai}' la phu am")
