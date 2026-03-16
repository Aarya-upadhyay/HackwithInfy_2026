class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        k=0
        for i in range(len(arr)):
            if arr[i]!=val:
                arr[k]=arr[i]
                k+=1
            else:
                continue
        return k
