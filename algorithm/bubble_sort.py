from typing import List
'''
typing模块作用
1.类型检查，防止运行时出现参数和返回值类型不符合。
2.作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
3.该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒。
使用:int作为输入参数类型检查, -> List 作为返回类型检查
'''

def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j + 1], a[j]
                made_swap = True
        if not made_swap:
            break

if __name__ == "__main__":
    array = [3,6,1,3,7,9,0,4,23,54,1,2,2,34]
    bubble_sort(array)
    print(array)