def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhap vao so can kiem tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "la so nguyen to.")
else:
    print(number, "khong phai la so nguyen to.")
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la:", dao_nguoc_chuoi(input_string))
