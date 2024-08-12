class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 :
            return [[]]
        perms = self.permute(nums[1:0])
        res = []
        for p in perms:
            for i in range(len(p)+1):
                pcop = p.copy()
                pcop.insert(i, nums[0])
                res.append(pcop)
        return res