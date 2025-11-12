# Bài 9: Tính tiền điện theo số kWh tiêu thụ

# Nhập số kWh điện tiêu thụ
so_kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))

# Tính tiền điện theo các bậc
if so_kwh <= 100:
    tien = so_kwh * 1678
elif so_kwh <= 200:
    tien = 100 * 1678 + (so_kwh - 100) * 1734
elif so_kwh <= 300:
    tien = 100 * 1678 + 100 * 1734 + (so_kwh - 200) * 2014
else:
    # Nếu vượt 300 kWh thì áp dụng bậc 3 cho phần còn lại
    tien = 100 * 1678 + 100 * 1734 + 100 * 2014 + (so_kwh - 300) * 2014

# In ra kết quả
print("Tổng số tiền điện phải trả là:", tien, "VNĐ")