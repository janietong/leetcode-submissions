from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = OrderedDict()
        self.cur = 0
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.d.move_to_end(key)
            return
        self.cur += 1
        if self.cur > self.cap:
            self.d.popitem(last=False)
        self.d[key] = value
        self.d.move_to_end(key)
            

        
