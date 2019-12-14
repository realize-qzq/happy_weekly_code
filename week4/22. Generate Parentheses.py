class Solution:
    def back(self, cur_left_ind, cur_str, cur_stack, cur_right_ind):
        if cur_left_ind == self.n and cur_right_ind == self.n:
            if cur_stack == []:
                self.ans.append("".join(cur_str))
            return
        if cur_left_ind > self.n or cur_right_ind > self.n:
            return
        for _ in range(2):
            if _ == 1:
                cur_stack.append("(")
                self.back(cur_left_ind + 1, cur_str + ["("], cur_stack, cur_right_ind)
                cur_stack.pop()
            else:
                if len(cur_stack) == 0:
                    continue
                if cur_stack[-1] == "(":
                    item = cur_stack.pop()
                    self.back(cur_left_ind, cur_str + [")"], cur_stack, cur_right_ind + 1)
                    cur_stack.append(item)
                else:
                    continue

    def generateParenthesis(self, n: int) -> List[str]:
        #更好的解法见 https://segmentfault.com/a/1190000018116657
        #这个还是太暴力了
        self.n = n
        self.ans = []
        self.back(0, [], [], 0)
        return self.ans
