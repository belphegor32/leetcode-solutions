class TimeMap:

    def __init__(self):
        self.store_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if there no such key in hashmap, create it to avoid key error
        if key not in self.store_map:
            self.store_map[key] = []
        
        # append pair with a key to the hashmap
        self.store_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        # find the value by key in hashmap, else get an empty list
        vals = self.store_map.get(key, [])
        
        # run a binary search to look for timestamp in log(n)
        left, right = 0, len(vals) - 1
        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)