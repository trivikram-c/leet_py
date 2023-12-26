# https://leetcode.com/problems/top-k-frequent-elements/submissions/1128717998/

# Better than 90%

# Learnt lambda function use (needs an input)
# Somehow the lambda function is worse than the function def

#Dict.get(key, defaultval) returns defval if key not present in dict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # x = lambda :  0
        ele_dict = defaultdict(x)
        for num in nums:
            ele_dict[num] += 1
        out = []
        sorted_list = sorted(ele_dict.values())[-k:]
        for key, val in ele_dict.items():
            if val in sorted_list:
                out.append(key)
        return out

def x():
    return 0  
