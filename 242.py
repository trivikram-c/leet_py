# https://leetcode.com/problems/valid-anagram/description/

# Beats 90% + but the part I have commented was written by me, but the last loop is solution

# Apparently the if in every for loop takes more time than the additional for loop over letters


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self_dict = {}
        # if len(s) != len(t):
        #     return False
        for l in s:
            if l in self_dict:
                self_dict[l] +=1
            else:
                self_dict[l] = 1
        for l in t:
            if l in self_dict:
                self_dict[l] -= 1
                # if self_dict[l] == 0:
                #     del(self_dict[l])
            else:
                return False
        for v in self_dict.values():
            if v != 0:
                return False
        return True
