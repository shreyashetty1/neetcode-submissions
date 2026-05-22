class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        return Counter(s)==Counter(t)
        if length(s)!=length(t):
            return False
        
        countS,countT={},{}
        for i in range(length(s)):
            count[s[i]]=1+count.get(s[i],0)
            count[t[i]]=1+count.get(t[i],0)

        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False

            return True