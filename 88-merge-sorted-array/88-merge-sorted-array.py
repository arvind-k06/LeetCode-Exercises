class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = m-1
        j= n-1
        k = m+n-1
        
        if m == 0:
            nums1[:] = nums2
        
        while(i>=0 and j>=0):
            
            if nums1[i]>nums2[j]:
                nums1[k]= nums1[i]
                nums1[i] = -1
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            
            k-=1
        # print(nums1)
        
        if j>=0:
            nums1[:k+1] = nums2[:j+1]
        print(i,j,k)
#         res = []
#         k = 0
#         i = 0
#         j = 0
#         # print(nums1, nums2)

#         while(i<m and j<n):
#             # print(i,j)
#             if nums1[i] < nums2[j]:
#                 res.append(nums1[i])
#                 i+=1
#             else:
#                 res.append(nums2[j])
#                 j+=1
                
#             k+=1
#         print(res, i, j)

#         while(i<m):
#             res.append(nums1[i])
#             i+=1

#         while(j<n):
#             res.append(nums2[j])
#             j+=1
                
#         nums1[:] = res
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        