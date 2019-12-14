class Solution:
    def __init__(self):
        self.ans=set()
        self.map={"2":("a","b","c"),"3":("d","e","f"),"4":("g","h","i"),"5":("j","k","l"),
                 "6":("m","n","o"),"7":("p","q","r","s"),"8":("t","u","v"),"9":("w","x","y","z")}
    def back(self,s,ind,cur_str):
        if ind==len(s):
            self.ans.add(cur_str)
            return
        x=s[ind]
        vals=self.map[x]
        for cand_char in vals:
            self.back(s,ind+1,cur_str+cand_char)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.back(digits,0,"")
        return list(self.ans)