'Tuổi của một người'

age = int(input("Nhập tuổi của một người: "))
if age > 0 and age <= 2:
    print("Là trẻ sơ sinh")
elif age > 2 and age <= 10:
    print("Là nhi đồng")
elif age > 10 and age <= 17:
    print("Là vị thành niên")
elif age > 17 and age <= 39:
    print("Là thanh niên")
elif age > 39 and age <= 50:
    print("Là trung niên")
elif age > 50:
    print("Là cao niên")
else:
    print("Nhập sai")

'Năm SX của một chiếc máy tính'

year = int(input("Nhập năm sản xuất của một chiếc máy tính: "))
if year >= 15:
    print("Thay thế")
elif year >= 10 and year < 15:
    print("Bảo trì")
else:
    print("Không có đề xuất")

'Điểm trung bình va xét học bổng'

GPA = float(input("Nhập điểm trung bình:"))
if GPA >= 9:
    print("Học bổng là 5.000.000 VNĐ")
elif GPA >= 8 and GPA < 9:
    print("Học bổng là 3.000.000 VNĐ")
elif GPA >= 7 and GPA < 8:
    print("Học bổng là 1.000.000 VNĐ")
else:
    print("Không có học bổng")

