class MyHashSet:

    def __init__(self):
        self.buckets = [None] * 1000

    def add(self, key: int) -> None:
        if not self.buckets[key % 1000]:
            self.buckets[key % 1000] = []
        
        bucket = self.buckets[key % 1000]
        
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % 1000]

        if not bucket:
            return
        
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key % 1000]

        if not bucket:
            return False
        
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)