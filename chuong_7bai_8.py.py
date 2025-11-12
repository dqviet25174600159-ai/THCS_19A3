# Bài 8: Tính chỉ số BMI

# Nhập cân nặng (kg) và chiều cao (m)
can_nang = float(input("72 kg): "))
chieu_cao = float(input("162 m): "))

# Tính chỉ số BMI
bmi = can_nang / (chieu_cao ** 2)

# In kết quả, làm tròn đến 2 chữ số thập phân
print("Chỉ số BMI của bạn là:", round(bmi, 2))