class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums.append('')
        # n = len(nums)
        # out = []
        # for idx in range(2**n):
        #     idxlist = format(idx, '0'+str(n)+'b')
        #     newout = []
        #     for i, j in enumerate(idxlist):
        #         if int(j):  newout.append(nums[i])
        #     out.append(newout)
        # return out

        subset = []
        res = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res