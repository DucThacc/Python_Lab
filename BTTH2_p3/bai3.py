"""Bài 3: về thực hiện chương trình đếm số từ trong nhiều file text
"""

def count_words(filename):
    try: 
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "File" + filename + "khong ton tai"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("File " + filename + " có " + str(num_words) + " từ.")
filenames =  ["f1.txt", "f2.txt", "f3.txt"]
for filename in filenames:
    count_words(filename)

