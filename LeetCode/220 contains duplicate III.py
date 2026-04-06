class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        w = valueDiff + 1   # bucket size
        
        for i, num in enumerate(nums):
            bucket_id = num // w
            
            # 1. same bucket
            if bucket_id in buckets:
                return True
            
            # 2. left neighbor bucket
            if (bucket_id - 1 in buckets and 
                abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True
            
            # 3. right neighbor bucket
            if (bucket_id + 1 in buckets and 
                abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True
            
            # insert into bucket
            buckets[bucket_id] = num
            
            # maintain window size ≤ indexDiff
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // w
                del buckets[old_bucket]
        
        return False
