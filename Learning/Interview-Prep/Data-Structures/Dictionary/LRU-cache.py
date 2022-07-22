#LRU CACHE
class LRUCache:
    from collections import OrderedDict
    """
    OrderedDict() tracks the insertion order of the keys and values while the normal     dict() does not. OrderedDict.popitem() removes the last inserted key-value pair       from the dictionary and returns it as a tuple.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        val = self.dict[key]
        del self.dict[key]
        self.dict[key] = val
        return val
            

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        self.dict[key] = value
        while len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


