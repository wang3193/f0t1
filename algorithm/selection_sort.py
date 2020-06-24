from typing import List

def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    
    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


if __name__ == "__main__":
    array = [3,6,1,3,7,9,0,4,23,54,1,2,2,34]
    selection_sort(array)
    print(array)



    
