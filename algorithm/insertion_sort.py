from typing import List

def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    
    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = value


if __name__ == "__main__":
    array = [3,6,1,3,7,9,0,4,23,54,1,2,2,34]
    insertion_sort(array)
    print(array)
