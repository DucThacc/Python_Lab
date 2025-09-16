"""Bài 3. Cho chuỗi biểu diễn:  
        "minhnhutvh@gmai.comSatJan509:14:16"
Rút trích và hiển thị chuỗi “gmail.com”
"""

data = "minhnhutvh@gmail.com Sat Jan 5 09:14:16"
Start_position = data.find("@")                
End_position = data.find(" ", Start_position)  
host = data[Start_position +1 : End_position]
print(host)