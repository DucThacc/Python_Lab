"""Bài 23: Định nghĩa một hàm Check_chan(n) kiểm tra một số có phải là số chẵn hay không. Yêu cầu:
Hàm được luu vào tệp Kiem_tra.py
Tạo tệp Test.py để sử dụng hàm này nhằm kiểm tra một số nhập vào từ bàn phím có phải là số chẳn hay không.

Bước 1: Tạo tệp Kiem_tra.py
	def Check_chan(x): 	    if x%2 == 0:              print(x, "là số chẵn") 
           else:
              print(x, "là số lẻ")Bước 2: Tạo tệp Test.py            
      from Kiem_tra import *
      n = int(input("Nhập vào một số để kiểm tra: "))
      Check_chan(n) 
"""