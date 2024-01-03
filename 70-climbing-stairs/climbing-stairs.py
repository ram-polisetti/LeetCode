class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n==0 or n==1:
        #     return 1
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        # This solution works but it is exceeding the time limit

        # if n==0 or n==1:
        #     return 1
        # temp_arr = [0]*(n+1)
        # temp_arr[0] = temp_arr[1] = 1
        # for i in range(2, n+1):
        #     temp_arr[i] = temp_arr[i-1] + temp_arr[i-2]
        # return temp_arr[n]

        # We can also do this by just using prev and curr values
        if n==0 or n==1:
            return 1
        prev = curr =1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr