def merge(self, arr: List[List[int]]) -> List[List[int]]:
        list1=[]
        arr.sort()
        for i in arr:
            if not list1 or list1[-1][1]<i[0]:
                list1.append(i)
            else:
                list1[-1][1]=max(list1[-1][1],i[1])
        return list1
