class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            s=sorted(s)
            t=sorted(t)

            print(s,t)

            counter = 0
            for i in range(0,len(s)):
                if s[i] == t[i]:
                    counter+=1
        
            if counter == len(t):
                return True
            else:
                return False

        
        