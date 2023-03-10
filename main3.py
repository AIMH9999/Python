import math

N = float(input("Nhập số N: "))
if N % 1 == 0 :
    print("N là số nguyên")
else:
    print("N không phải là số nguyên")
if N % 1 != 0:
    print("N không phải số chẵn cũng không phải số lẽ")
elif N % 2 == 0:
    print("N là số chẵn")
else :
    print("N là số lẻ")
if N > 0 and N % 2 == 0:
    print("N là số chẵn dương")
elif N < 0 and N % 2 != 0:
    print("N là số lẽ âm")
if math.sqrt(N) % 1 == 0 and N >= 0:
    print("N là số chính phương")
else:
    print("N không phải là số chính phương")




