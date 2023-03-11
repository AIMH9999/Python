while True:
    n = int(input("Nhập số n( 0 < n < 100 ): "))
    if n > 0 and n < 100:
        break
    else:
        print("Nhập sai vui lòng nhập lại")
        continue