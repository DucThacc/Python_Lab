def is_positive_integer(s):
    return s.isdigit() and int(s) > 0

while True:
    number=[]
    print("Enter a positive integer (or 'Done' to out): ")
    num = input()
    if num.lower() == "done":
        print("Goodbye")
        break
    if is_positive_integer(num):
        number.append(num)
    else:
        print("Plsease enter a positive integer")

if number:
    print(f"So lon nhat la {max(number)}") 
    print(f"So nho nhat la {min(number)}")
else:
    print("Khong co so nao")