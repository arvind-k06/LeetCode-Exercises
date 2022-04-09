#User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
		# code here
		s = set(arr)
		c=0
		for i in range(n):
		    for j in range(i+1,n):
		        if arr[i]+arr[j] in s:
		            c+=1
		            
		return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends