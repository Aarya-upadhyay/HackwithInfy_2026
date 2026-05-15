import heapq

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

"""Review
Correctness (40%)

Logic correctly keeps only the k largest elements in the min-heap.
min_heap[0] is the k-th largest element.
Works for duplicates, negatives, k = 1, and k = len(nums) as long as inputs follow constraints.
Score: 40/40
Use of Min-Heap of Size k (25%)

Uses a min-heap via heapq.
Maintains heap size at most k and pops smallest when size exceeds k.
Returns the root as the answer.
Score: 25/25
Time and Space Efficiency (15%)

Each push/pop is O(log k), done n times → O(n log k) time.
Heap holds at most k elements → O(k) space.
Does not sort the entire array.
Score: 15/15
Code Quality and Readability (10%)

Code is short, clear, and idiomatic.
Adding a brief comment/docstring would improve clarity slightly.
Score: 9/10
Edge Case Handling (10%)

Works correctly for:
k = 1 (returns max element).
k = len(nums) (returns min element).
Negative values and duplicates.
Assumes valid k as per problem constraints, which is acceptable.
Score: 10/10
Overall Grade: 40 + 25 + 15 + 9 + 10 = 99/100

Summary:
Your solution is correct, efficient, and uses a min-heap of size k exactly as intended. Just consider adding minimal comments or a docstring for even better readability.
"""
