class MyHashSet:
    '''
    705. Design HashSet
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.appearance = [0] * 1000001


    def add(self, key: int) -> None:
        self.appearance[key] = 1


    def remove(self, key: int) -> None:
        self.appearance[key] = 0


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.appearance[key] == 1



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)