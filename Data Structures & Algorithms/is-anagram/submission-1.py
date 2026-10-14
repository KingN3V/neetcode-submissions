class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        const_s = {}
        const_t = {}
    
        for c in s:
            if c in const_s:
                const_s[c] += 1
            else:
                const_s[c] = 1

        for c in t:
            if c in const_t:
                const_t[c] += 1
            else:
                const_t[c] = 1
        
        return const_t == const_s

 
    
    


    
