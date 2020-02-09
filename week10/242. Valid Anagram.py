from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sc=Counter(s)
        tc=Counter(t)
        if len(sc)!=len(tc):
            return False
        for key in tc:
            if key not in sc or tc[key]!=sc[key]:
                return False
        return True