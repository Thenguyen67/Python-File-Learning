if __name__ == "__main__":

    a = [0, 1, 2, 3, 4, 5]
    print(a)
    print(len(a))

    b = [0, 1, "A", "B"]

    print(b[3])

    for i in b:
        print(i)

    b.append("C")

    d = 0
    for d in range(d, len(b), 1):
        print(b[d], end = " ")

    # append chèn vào cuối

    b.insert(2, 100) #Insert chèn vào index tùy chỉnh insert(index, value)

    b.pop(2) # Xóa phần tử ở index 2, nếu không truyền tham số sẽ xóa phần tử cuối

    del b[1] # Giống pop

    a.clear() # Xóa hết mọi phần tử trong list

    c = [1, 2, 3]

    e = c*2

    print(e)

    b.reverse()

    b.sort() #Sắp xếp quicksort

    c.copy(b) 