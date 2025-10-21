def is_positive_integer(s):
    return s.isdigit() and int(s) > 0

numbers =[]
print("Nhap cac so nguyen duong (or 'Done' to out): ")
while True:
    user_input = input()
    if user_input.lower() == "done":
        print("Goodbye")
        break
    if is_positive_integer(user_input):
        numbers.append(int(user_input))
    else:
        print("Please enter a positive integer")
if numbers:
    print(f"So lon nhat la {max(numbers)}")        
    print(f"So nho nhat la {min(numbers)}")
else:
    print("Khong co so nao")