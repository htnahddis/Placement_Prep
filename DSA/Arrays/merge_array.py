class Solution:
    def merge(self, nums1, m, nums2, n):

        temp = nums1[:m]

        i = 0      # temp pointer
        j = 0      # nums2 pointer
        k = 0      # nums1 pointer

        while i < m and j < n:

            if temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1

        # Remaining elements from temp
        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1

        # Remaining elements from nums2
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1