class Solution:
    def back(self, xind, res, y_visited):
        if xind == self.n:
            if len(res) == self.n:
                self.candidates.append(res[:])
            return
        for y in range(self.n):
            if y in y_visited:
                continue#不是return，否则这行其他y就不会尝试了
            else:
                good_flag=True
                for point in res:
                    px, py = point
                    if abs(px - xind) == abs(py - y):
                        good_flag=False
                        break
                if good_flag is False:
                    continue#不是return，否则这行其他y就不会尝试了
                y_visited.add(y)
                self.back(xind + 1, res + [[xind, y]], y_visited)
                y_visited.remove(y)

    def solveNQueens(self, n):
        self.n = n
        self.candidates = []
        y_visited = set()
        self.back(0, [], y_visited)
        results = []
        for points in self.candidates:

            temp = [["."] * self.n for i in range(self.n)]
            cur_ans = []
            for point in points:
                x, y = point
                temp[x][y] = "Q"
                cur_ans.append("".join(temp[x]))
            results.append(cur_ans[:])
        return results

if __name__=="__main__":
    sol=Solution()
    results=sol.solveNQueens(4)
    for _ in results:
        print(_)
        print()