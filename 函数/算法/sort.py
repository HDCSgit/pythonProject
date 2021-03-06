# -*-coding:utf-8-*-
import copy
import random
from cal_time import *

#冒泡排序
@cal_time
def bubble_sort(li):
    for i in range(len(li)-1): #第i趟
        for j in range(len(li)-i-1): #第j位
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]


#选择排序
@cal_time
def select_sort(li):
    for i in range(len(li)-1): #i是第几趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if i != min_loc:
            li[i],li[min_loc] = li[min_loc],li[i]
    return li

#插入排序
@cal_time
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp


#快速排序分两步和一个套娃：
def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:#从右面找比tmp小的数
            right -= 1 #往左走一步
        li[left] = li[right] #把右边的值写到左边的空位上
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]#把左边的值写到右边的空位上
    li[left] = tmp #把tmp归为
    return left

def _quick_sort(li, left, right):
    if left < right: #至少两个元素

        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)




@cal_time
def quick_sort(li):
    try:
        _quick_sort(li,0,len(li)-1)
    except:
        pass

# 堆排序

def sift(li,low,high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
        li[i] = tmp

def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    #1.建堆
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)
    #2.遍历
    for i in range(k-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap,0,i - 1)
    #3.出数
    return heap
@cal_time
def topk_sort(li):
    topk(li,len(li))


#归并排序 时间复杂度O(nlogn) 空间复杂度O(n)
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []  # 新列表来储存 li[i]与li[j]比较后较小的值
    while i <= mid and j <= high:  # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # 执行完后有一部分没有数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    # 切片赋值回去
    li[low:high + 1] = ltmp

def _merge_sort(li, low, high):
    if low < high:  # 至少有两个元素，递归
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)

@cal_time
def merge_sort(li):
    try:
        _merge_sort(li,0,len(li))
    except:
        pass


def insert_sort_gap(li,gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and tmp < li[j]:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp



@cal_time
def shell_sort(li):
    d = len(li)//2
    while d >= 1:
        insert_sort_gap(li,d)
        d = d//2


@cal_time
def _shell_sort(list):
    n =len(list)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = list[i]
            j = i 
            while j >= 0 and j-gap >= 0 and list[j-gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = gap//2
    return list

@cal_time
def count_sort(li, max_count=10000):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for _ in range(val):
            li.append(ind)

@cal_time
def sort_test(li):
    return sorted(li)

@cal_time
def bucket_sort(li):
    max_val = max(li)
    min_val = min(li)
    bucket_size = (max_val - min_val) // len(li) + 1
    bucket = [[] for _ in range(len(li))]
    for val in li:
        bucket[(val - min_val) // bucket_size].append(val)
    li.clear()
    for b in bucket:
        li.extend(b)
    return li



li = list(range(10000))
random.shuffle(li)

li1=copy.deepcopy(li)
li2=copy.deepcopy(li)
li3=copy.deepcopy(li)
li4=copy.deepcopy(li)
li5=copy.deepcopy(li)
li6=copy.deepcopy(li)
li7=copy.deepcopy(li)
li8=copy.deepcopy(li)
li9=copy.deepcopy(li)
li10=copy.deepcopy(li)

bubble_sort(li1)
insert_sort(li2)
select_sort(li3)
quick_sort(li4)
topk_sort(li5)
merge_sort(li6)
shell_sort(li7)
sort_test(li8)
count_sort(li9)
bucket_sort(li10)