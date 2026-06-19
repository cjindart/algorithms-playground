from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = OrderedDict()
        self.capacity = capacity
        self.size = 0


    def get(self, key: int) -> int:
        if key in self.LRU.keys():
            self.LRU.move_to_end(key)
            return self.LRU[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU.keys():
            
            self.LRU[key] = value
            self.LRU.move_to_end(key)
            return
        if self.size == self.capacity:
            self.size -= 1
            self.LRU.popitem(last=False)
        
        self.LRU[key] = value
        self.size += 1
        return
        
        
