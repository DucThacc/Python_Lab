def ten_hoa(ten):
    return " ".join(word.capitalize() for word in ten.split())


while True:
    ho_ten = input("Nhap ho ten (or 'Done' to out ): ")
    if ho_ten.lower() == "done":
        print("Goodbye")
        break
    print(ten_hoa(ho_ten))