class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        
        res = []
        k = 0
        i = 0
        j = 0
        print(nums1, nums2)

        while(i<m and j<n):
            print(i,j)
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
                
            k+=1
        print(res, i, j)

        while(i<m):
            res.append(nums1[i])
            i+=1

        while(j<n):
            res.append(nums2[j])
            j+=1
                
        nums1[:] = res
        """
        Do not return anything, modify nums1 in-place instead.
        """
        