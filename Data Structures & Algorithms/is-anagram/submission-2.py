class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_hashmap = {}
        s_hashmap = {}

        if len(s) != len(t):
            return False

        for i in range (len(s)):
            if s[i] in s_hashmap:
                s_hashmap[s[i]] += 1
            else:
                s_hashmap[s[i]] = 1
        
        for i in range (len(t)):
            if t[i] in t_hashmap:
                t_hashmap[t[i]] += 1
            else:
                t_hashmap[t[i]] =1

        return s_hashmap == t_hashmap
        