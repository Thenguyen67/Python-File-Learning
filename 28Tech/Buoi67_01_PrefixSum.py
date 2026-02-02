import sys

n = int(input())
list1 = list(map(int, input().split()))

if(len(list1) > n or len(list1) < n):
    sys.exit(0)

l, r = map(int, input().split())
    
list2 = [0] *n

for i in range (1, n):
    list2[i] = list2[i -1] + list1[i]

print(list2[r] - list2[l -1])