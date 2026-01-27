def Sum(a, b):
    c = a + b
    return c

def CallHello(str1, str2, str3):
    print("Hello", str1, str2, str3)

# a = int("Nhap a :", input())
# b = int("Nhap b :", input())

if __name__ == "__main__":
    
    a, b = map(int, input("Nhap vao : ").split())


    print("Tong a va b la :", Sum(a, b))

    print(CallHello("Nam", "Dung", "Huy"))