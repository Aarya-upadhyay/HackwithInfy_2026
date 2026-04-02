class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        k=len(words[0])
        m=len(words)
        win=k*m
        word_map={}
        for word in words:
            word_map[word]=word_map.get(word,0)+1
        res=[]
        for i in range(len(s)-win+1):
            temp_map={}
            j=i
            while j<i+win:
                w=s[j:j+k]
                if w not in word_map:
                    break
                temp_map[w]=temp_map.get(w,0)+1
                if temp_map[w]>word_map[w]:
                    break
                j+=k
            if j==i+win:
                res.append(i)
        return res
