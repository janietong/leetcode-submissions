class MyHashMap:

    def __init__(self):
        self.hmap = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hmap)):
            k, v = self.hmap[i]
            if k == key:
                self.hmap[i][1] = value
                return
        self.hmap.append([key, value])
        

    def get(self, key: int) -> int:
        for i in range(len(self.hmap)):
            k, v = self.hmap[i]
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:    
        for i in range(len(self.hmap)):
            k, v = self.hmap[i]
            if k == key:
                self.hmap.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)