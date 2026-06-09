class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 , p2 = 0, 0 # Initialize the pointer on Both Lists
        n1 , n2 = len(nums1)  ,len(nums2)
        ans = []
        while (p1 < n1 and p2 < n2):
            if nums1[p1] < nums2[p2]:
                ans.append(nums1[p1])
                p1 +=1
            else:
                ans.append(nums2[p2])
                p2 +=1
        if p1 != n1:
            while p1 <n1:
                ans.append(nums1[p1])
                p1 +=1
        else:
            while p2 < n2 : 
                ans.append(nums2[p2])
                p2 +=1 
        start  , end =  0 , len(ans)-1
        mid = (end + start) //2
        if len(ans) % 2 == 0 :
            return (ans[mid] + ans[mid+1]) /2
        else:
            return ans[mid] 





                
