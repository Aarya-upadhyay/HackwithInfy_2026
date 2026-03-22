class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows=[""]*numRows
        cur_row=0
        dire=1
        for i in s:
            rows[cur_row]+=i
            if cur_row==0:
                dire=1
            elif cur_row==numRows-1:
                dire=-1
            cur_row+=dire
        return "".join(rows)
