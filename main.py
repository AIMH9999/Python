'BÀI 1: Chương trình kiểm tra số chẵn hay lẻ trong Python'

n = float(input("Nhập vào một số:"))
if n % 2 == 0 and n != 0:
    print("n là số chẵn")
elif n % 2 == 1:
    print("n là số lẻ")
else :
    print("n không phải là số chẵn cũng không phải là số lẽ")

'BÀI 2: Chương trình tìm số lớn nhất trong 3 số bằng Python'

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
c = int(input("Nhập số c:"))
max = a
if b > max:
    max = b
if c > max:
    max = c
print("Max = %d" %max)

'BÀI 3:	Chương trình in ra các ngày trong tháng bằng Python'

month = 30
day = 1
while day <= month:
    print("Ngày %d" %day)
    day = day + 1

'''
Bài 4:Viết chương trình cho người dùng nhập vào một số nguyên n.
Nếu n lẻ thì in ra màn hình dòng chữ “Số lẻ”. Nếu số n chẵn và lớn hơn hoặc bằng 100 thì in ra màn hình dòng chữ “Số chẵn và lớn hơn hoặc bằng 100”, 
ngược lại thì in ra dòng chữ “Số chẵn và bé hơn 100”.
'''

n = int(input("Nhập số nguyên n:"))
if n % 2 == 0 and n != 0:
    if n >= 100:
        print("n là số chẵn và n lớn hơn hoặc bằng 100")
    else:
        print("n là số chẵn và n bé hơn 100")
elif n % 2 == 1:
    if n >= 100:
        print("n là số lẻ và n lớn hơn hoặc bằng 100")
    else:
        print("n là số lẽ và n bé hơn 100")
else:
    print("n = 0")

'Bài 5: Biện luận phương trình bậc nhất ax+b=0'

a = int(input("Nhập a:"))
b = int(input("Nhap b:"))

if a == 0 and b !=0:
    print("Phương trình vô nghiệm")
elif a != 0 and b == 0:
    print("Phương trình có một nghiệm x = 0")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Phương trình có một nghiệm = %.1f"%(-b/a))



