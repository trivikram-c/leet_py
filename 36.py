class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                res.append(comb.copy())
                return
            
            comb.append(candidates[i])
            dfs(i, total + candidates[i])
            comb.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res