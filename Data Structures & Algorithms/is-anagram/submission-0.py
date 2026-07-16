class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for charS in s:
            if charS in sDict:
                sDict[charS] +=1
            else:
                sDict[charS] = 0 

        for charT in t:
            if charT in tDict:
                tDict[charT] +=1
            else:
                tDict[charT] = 0 
        if sDict == tDict:
            return True
        return False
                    