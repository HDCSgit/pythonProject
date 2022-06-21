import copy
import random
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[i] > li[j]:
                li[j],li[j+1] = li[j+1],li[j]

def select_sort1(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]

def select_sort2(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if i != min_loc:
            li[i],li[min_loc] = li[min_loc],li[i]
    return li

def insert_sort(li):
    for i in range(len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp



def quickSort(li,left=None,right=None):
    left = 0 if not isinstance(left,(int,float)) else left
    right = len(li)-1 if not isinstance(right,(int,float)) else right
    if left < right:
        partitionIndex=partition(li,left,right)
        quickSort(li,left,partitionIndex-1)
        quickSort(li,partitionIndex+1,right)
    return li

def partition(li,left,right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if li[i] < li[pivot]:
            swap(li,i,index)
            index += 1
        i += 1
    swap(li,pivot,index-1)
    return index-1

def swap(li,i,j):
    li[i] , li [j] = li [j] , li [i]


def shellSort(li):
    import math
    gap = 1
    while gap < len(li)/3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap,len(li)):
            tmp = li [i]
            j = i - gap
            while j >= 0 and li[j] > tmp:
                li[j+gap] = li [j]
                j -= gap
            li[j+gap] = tmp
        gap = math.floor(gap/3)
    return li

li = [1,2,2,3,4,5,6,6,6,7,8,9]
print(li)
random.shuffle(li)
li2=copy.deepcopy(li)
li3=copy.deepcopy(li)
li4=copy.deepcopy(li)
li5=copy.deepcopy(li)
select_sort1(li)
select_sort2(li2)
insert_sort(li3)
quickSort(li4)
shellSort(li5)
print(li)
print(li2)
print(type(range(10)))
print(li3)
print(li4)
print(li5)
