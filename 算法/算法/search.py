
#递归的两个特点：①调用自身 ②结束自身
def fun1(x):
    if x>0:
        print(x)
        fun1(x-1)

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s" % (a,c))
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')

def linear_search(li,val):
    for ind,v in enumerate(li):
        if v == val:
            return ind
    else:
        return None
#二分查找
def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: #带查找的值在mid左侧
            right = mid - 1
        else: #li[mid] < val 带查找的值在mid右侧
            left = mid + 1

#插入排序
def insert_sort(li):
    for i in range(1,len(li)):#i表示摸到的牌的下标
        tmp = li[i]
        j = i -1 #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
