class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fibo_list = [0, 1]

        for i in range(2,n+2):
            fibo_sum_next = fibo_list[i-2] + fibo_list[i-1]
            fibo_list.append(fibo_sum_next)

            print i , fibo_sum_next

        val = fibo_list[n+1]
                
        return fibo_list[n+1]


        # if n = 1:
        #     return 1
        
        # remain = n % 2
        # half = n // 2      # this is the maximum number of twos
        # steps = 0
        # counter_2s = 0

        # for i in range(1,half+1):
        #     counter_2s = counter_2s + i

        # if n % 2 == 0:
        #     steps = 1 + (n - 1) + counter_2s


        # steps = 1 + (n - 1) + counter_2s

        # return steps
