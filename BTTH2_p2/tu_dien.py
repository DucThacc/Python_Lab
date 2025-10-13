"""File chứa các hàm làm việc với từ điển"""

def Tao_TD(Max):
    """Tạo từ điển với key từ 1 đến Max và value là bình phương của key"""
    td = {}
    for i in range(1, Max + 1):
        td[i] = i ** 2
    return td

def Print_Item(TD):
    """In các phần tử của từ điển (key: value)"""
    print("Cac phan tu cua tu dien:")
    for key, value in TD.items():
        print(f"{key}: {value}")

def Print_Key(TD):
    """In các key của từ điển"""
    print("Cac key cua tu dien:")
    for key in TD.keys():
        print(key, end=" ")
    print()  # Xuống dòng

def Print_Value(TD):
    """In các value của từ điển"""
    print("Cac value cua tu dien:")
    for value in TD.values():
        print(value, end=" ")
    print()  # Xuống dòng
