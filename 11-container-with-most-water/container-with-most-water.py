class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


        # y_vals = []
        # max_vol = 0
        # x_max = len(height) - 1

        # # print(x_max)

        # for x_dist in range(1, x_max+1):
        #     x_iter = x_max - x_dist + 1

        #     # print("x_dist : ", x_dist, "   x_iter : ", x_iter)

        #     for iter in range(0, x_iter):
        #         y_vals = []
        #         y_vals.append(height[iter])
        #         y_vals.append(height[iter+x_dist])
        #         volume = x_dist * min(y_vals)

        #         # print(x_dist, y_vals, volume)

        #         if(max_vol < volume):
        #             max_vol = volume
        # return max_vol
