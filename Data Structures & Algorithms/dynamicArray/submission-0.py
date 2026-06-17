class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        length = self.getSize()
        capacity = self.getCapacity()
        if capacity > length:
            self.array[length] = n
        else:
            self.resize()
            self.array[length] = n
        self.size += 1


    def popback(self) -> int:
        length = self.getSize()
        elem = self.array[length - 1]
        self.array[length - 1] = None
        self.size -= 1
        return elem

    def resize(self) -> None:
        capacity = self.getCapacity()
        new_capacity = capacity * 2
        new_arr = [None] * new_capacity
        for i, elem in enumerate(self.array):
            new_arr[i] = elem
        self.array = new_arr
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity