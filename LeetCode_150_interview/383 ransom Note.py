class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #is_true=True
        hash_map={}
        for i in magazine:
            hash_map[i]=hash_map.get(i,0)+1
        for i in ransomNote:
            """if i in hash_map:
                if hash_map[i]==0:
                    is_true=False
                    break
                    
                hash_map[i]-=1
            else:
                is_true=False"""
            if i not in hash_map or hash_map[i]==0:
                return False
            hash_map[i]-=1
        return True
        
        
