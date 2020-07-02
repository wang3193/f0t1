from typing import List
import random

def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a) - 1)


def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        # get random prosition as the pivot
        # 获取随机角标作为中间位数据
        k = random.randint(low, high)
        # swap start and pivot value
        # 将中间位数据放到数组首位
        a[low], a[k] = a[k], a[low]

        #排序,并返回中间值所在的角标
        m = _partition(a, low, high) 
        # 递归排序中间值左边数据
        _quick_sort_between(a, low, m - 1)
        # 递归排序中间值右边数据
        _quick_sort_between(a, m + 1, high)


def _partition(a: List[int], low:int, high:int):
    pivot, j = a[low], low
    # 按角标循环,如果小于中间值,就放在左侧
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    # 交换中间值和小于中间值的角标位置
    a[low], a[j] = a[j], a[low]
    return j


if __name__ == "__main__":
    array = [3,6,1,3,7,9,0,4,23,54,1,2,2,34]
    quick_sort(array)
    print(array)



