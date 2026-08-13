class TimeMap:

    def __init__(self):
        self.ds = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = [[value, timestamp]]
        else:
            self.ds[key].append([value, timestamp]) 

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.ds:
            return ""
        else:
            curr = self.ds[key]
            if not curr:
                return res
            l, r = 0, len(curr) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if curr[mid][1] == timestamp:
                    return curr[mid][0]
                
                elif curr[mid][1] > timestamp:
                    r = mid - 1
                    
                
                elif curr[mid][1] < timestamp:
                    l = mid + 1
                    res = curr[mid][0]

        return res
        
