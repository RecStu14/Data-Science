class MyHashSet:

    def __init__(self):
        self.MyHashSet = set()
        

    def add(self, key: int) -> None:
        self.MyHashSet.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.MyHashSet:
            self.MyHashSet.discard(key)
        else:
            pass
        

    def contains(self, key: int) -> bool:
        if key in self.MyHashSet:
            return True
        else:
            return False
     
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)