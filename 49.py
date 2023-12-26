# https://leetcode.com/problems/group-anagrams/submissions/1128705227/

# Beat most users, but was completley copied
# Learnt about defauldict, which is a dict which raises a preset value instead of KeyError
# doubt - why does this srted solutio work better than iterating over a list of chars?
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)

        for word in strs:
            sorted_word =  ''.join(sorted(word))
            ana_map[sorted_word].append(word)
        return list(ana_map.values())
