class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]
    
    def __setitem__(self, index: int, value: object):
        self._data[index] = value
    
    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item
    
    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None 

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)
            return True
    
    def print_all(self):
        for item in self:
            print(item)

def test_myArray():
    array = MyArray(10)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 6)
    assert array.insert(3, 100) is True
    assert array.insert(10, 20) is True
    assert len(array) == 6
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()

if __name__ == "__main__":
    test_myArray()




