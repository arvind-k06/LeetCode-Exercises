#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
	    maxi = [0]*n
	    maxi[0] = Arr[0]
	    for i in range(n):
	        maxi[i] = Arr[i]
	        for j in range(0, i):
	            if Arr[j]<Arr[i]:
	                maxi[i] = max(maxi[i], Arr[i]+maxi[j])
	    return max(maxi)
	            
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends