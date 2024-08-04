class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.map[key] = self.map.get(key, []).append([timestamp, value])
        if key not in self.map:
            self.map[key] = [[timestamp, value]]
        else:
            self.map[key].append([timestamp, value])
        # print(self.map[key])

        

    def get(self, key: str, timestamp: int) -> str:
        tl = self.map.get(key, [])
        l, r = 0, len(tl) -1
        res = ''
        while l <= r:
            curr = r - (r-l)//2
            if timestamp < tl[curr][0]:
                r = curr - 1
            else:
                l = curr + 1
                res = tl[curr][1]
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)