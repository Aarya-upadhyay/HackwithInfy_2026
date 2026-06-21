class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        k=2
        max_len=-1
        freq={}
        for i in range(len(fruits)):
            freq[fruits[i]]=freq.get(fruits[i],0)+1
            while len(freq)>k:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            max_len=max(max_len,i-left+1)
        return max_len
        
