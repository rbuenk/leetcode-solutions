class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False  # negative numbers aren't palindromes

        original = x
        length_x = 0
        original_list = []
        reversed_list = []
        
        while x > 0:
            digit_back = x % 10
            x = x // 10
            length_x = length_x + 1
            reversed_list.append(digit_back)
        
        length_y = length_x


        for i in range(0 , length_y):
            # print("i is: ", i)
            # print("original is: ", original)
            # print("length_x is: ", length_x)
            # print("10^length_x is: ", 10 ** (length_x-1))

            digit_front = original // (10 ** (length_x-1))
            # print("digit_front is: ", digit_front)

            digit_front_back = digit_front % 10
            # print("digit_front_back is: ", digit_front_back)
            length_x = length_x - 1
            # print("******************************")

            original_list.append(digit_front_back)

        # print("original_list is: ", original_list , "reversed_list is: ", reversed_list)

        for i in range(0, length_y):
            # print("original_list is: ", original_list[i] , "reversed_list is: ", reversed_list[i])

            if original_list[i] != reversed_list[i]:
                return False
        return True       