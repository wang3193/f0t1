'''
归并排序:
'''
from typing import List

def merge_sort(a: List[int]):
    _merge_sort_between(a, 0, len(a) - 1)

def _merge_sort_between(a: List[int], low: int, high: int):

    if low < high:
        # 确认中间角标
        mid = low + (high - low) // 2
        # 拆分前半数组
        _merge_sort_between(a, low, mid)
        # 拆分后半数组
        _merge_sort_between(a, mid + 1, high)
        # 合并排序
        _merge(a, low, mid, high)
    
def _merge(a: List[int], low: int, mid: int, high: int):
    # 确认两端数组的开始角标
    i, j = low, mid + 1
    # 申请临时数组
    tmp = []
    # 循环两个有序数组,按从小到大填充进tmp数组中
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    # 因为只需要循环完一个数组,可能有数组中有未填入tmp的数据
    # 获取剩余的元素在a数组中的位置
    start = i if i <= mid else j
    end = mid if i <= mid else high
    # 将元素插入tmp数组中
    tmp.extend(a[start:end + 1])
    # 将排序后的数据和a数组中对应角标中的数据替换
    a[low:high + 1] = tmp

if __name__ == "__main__":
    array = [3,6,1,3,7,9,0,4,23,54,1,2,2,34]
    merge_sort(array)
    print(array)


