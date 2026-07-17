class MyHashSet:

    def __init__(self):
        self.hs = [-1]*1000001

    def add(self, key: int) -> None:
        self.hs[key] = 0

    def remove(self, key: int) -> None:
        self.hs[key] = -1

    def contains(self, key: int) -> bool:
        return self.hs[key] == 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)