#Viết một chương trình có thể tính giai thừa của một số cho trước.
#  Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

def GiaiThua(value):
    if value < 0 : 
        return -1
    Tich = 1
    while value != 0 :
        Tich*= value
        value = value -1

    return Tich

if __name__ == "__main__":
    a = int(input("Nhap vao : "))
    print("Giai thua cua", a, "la :", GiaiThua(a))