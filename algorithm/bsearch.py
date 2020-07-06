from typing import List
def bsearch(nums: List[int], target: int) -> int:
    '''
    Bianry search of a target in a sorted array without duplicates.
    二分法搜索一个对象在一个无重复的排序数组
    If such a target does not exits, return -1, otherwise, return its index.
    '''
    low, high = 0, len(nums) -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
    