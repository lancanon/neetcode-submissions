class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store the numbers in a heap (Python heapq is a min-heap)
        self.minHeap, self.k = nums, k  

        # Turn the input list into a valid heap in-place (O(n))
        heapq.heapify(self.minHeap)  

        # Keep only the largest k elements in the heap
        # Pop until the heap has exactly k items
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # removes the smallest element

    def add(self, val: int) -> int:
        # Add the new value into the heap
        heapq.heappush(self.minHeap, val)

        # If heap grows larger than k, remove the smallest element
        # This keeps only the k largest numbers in the heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The smallest element in the heap (root) is now the kth largest overall
        return self.minHeap[0]
