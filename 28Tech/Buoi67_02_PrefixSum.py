import numpy as np
import sys

def TongKhoang(arr1, arr2, l, r):
    for i in range (1, len(arr1)):
        arr2[i] = arr2[i-1] + arr1[i]
    return arr2[r] - arr2[l-1]



if __name__ == "__main__":

    n = int(input("Số phần tử mảng : "))
    arr1 = input().split()

    if len(arr1) < n or len(arr1) > n :
        sys.exit(0)

    arr2 = [0]*n

    l, r = map(int, input().split())
    if l <= 0 or r <= 0:
        sys.exit(0)

    arr3 = np.array(arr1, dtype= int)
    arr4 = np.array(arr2, dtype= int)

    print(TongKhoang(arr3, arr4, l, r))

