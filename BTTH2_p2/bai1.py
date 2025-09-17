"""Bài 1. Viết một chương trình nhập vào một số nguyên dương. 
Nếu nó là số chẵn thì in ra chuỗi “Đây là số chẵn”, ngược lại thì in ra chuỗi “Đây là số lẻ”:
"""

number = int(input(" Nhập số nguyên dương: "))

if(number > 0 ):
    if int(number)%2 == 0:
        print(" Đây là số chẵn!")
    else:
        print(" Đây là số lẻ!")
else:
    print(" Số bạn nhập không phải số nguyên dương!")
