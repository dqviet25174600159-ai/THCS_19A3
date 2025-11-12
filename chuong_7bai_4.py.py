# Bài 4: Nhập một số tiền bằng VNĐ từ bàn phím.
# Chuyển đổi sang USD (tỷ giá 1 USD = 24.500 VNĐ) và in kết quả làm tròn 2 chữ số thập phân.

# Nhập dữ liệu
vnd = float(input("70000: "))

# Tỷ giá quy đổi
ty_gia = 24500

# Tính số tiền USD
usd = vnd / ty_gia

# In kết quả (làm tròn 2 chữ số thập phân)
print("Số tiền quy đổi sang USD là:", round(usd, 2), "USD")