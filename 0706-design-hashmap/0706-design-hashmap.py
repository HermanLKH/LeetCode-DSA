class MyHashMap:

    def __init__(self):
        self.buckets = [None for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        if not self.buckets[key % 1000]:
            self.buckets[key % 1000] = []

        bucket = self.buckets[key % 1000]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return

        bucket.append((key, value))
            

    def get(self, key: int) -> int:
        bucket = self.buckets[key % 1000]

        if not bucket:
            return -1

        for k, v in bucket:
            if k == key:
                return v

        return -1
            

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % 1000]

        if not bucket:
            return

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, -1)
                return
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)