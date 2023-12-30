# https://leetcode.co/probles/valid-parentheses/subissions/1131566455/

# Stacks question, easy, 95%, kinda had seent the solution before


class Solution:
    def isValid(self, s: str) -> bool:
        open_dict = {'{':'}','(':')','[':']'}
        buff = []
        for c in s:
            if c in open_dict:
                buff.append(c)
            elif (len(buff) > 0) and (c == open_dict[buff.pop()]):
                continue
            else:
                return False
        if len(buff) != 0:
            return False
        return True
