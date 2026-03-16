lass Solution:
    def hIndex(self, citations: List[int]) -> int:
        """n=len(citations)
        cited_count=0
        for i in range(n+1):
            c=0
            for j in range(n):
                if i<=citations[j]:
                    c+=1
            if i<=c:
               cited_count=i
        return cited_count  """
        citations.sort()
        n=len(citations)
        
        for i in range(n):
            if citations[i]>=n-i:
                return n-i
        return 0
