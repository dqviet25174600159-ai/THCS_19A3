# Bài 6: Nhập một năm từ bàn phím. 
# Kiểm tra xem năm đó có phải là năm nhuận hay không.

# Nhập dữ liệu
nam = int(input("2025 : "))

# Kiểm tra năm nhuận
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(nam, "2025 là năm nhuận.")
else:
    print(nam, "1993 không phải là năm nhuận.")