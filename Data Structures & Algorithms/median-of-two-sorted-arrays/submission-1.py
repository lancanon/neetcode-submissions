class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Make sure A is the smaller array (we binary search on it)
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2  # Mid index for A
            j = half - i - 2  # Corresponding index for B

            # Handle edge cases for out-of-bound indices
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # ✅ Found the correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # If total length is odd → return min of right side
                if total % 2:
                    return min(Aright, Bright)
                # If even → average of max left and min right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # ❌ Partition is too far right in A → move left
            elif Aleft > Bright:
                r = i - 1
            # ❌ Partition is too far left in A → move right
            else:
                l = i + 1
