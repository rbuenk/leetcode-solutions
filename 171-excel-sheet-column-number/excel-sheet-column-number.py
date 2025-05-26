class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alphabet = {'A': 1, 'B': 2, 'C': 3,'D': 4,'E': 5,'F': 6, 'G': 7,'H': 8, 'I': 9,'J': 10, 'K': 11,'L': 12, 'M': 13,'N': 14, 'O': 15,'P': 16, 'Q': 17,'R': 18, 'S': 19,'T': 20, 'U': 21,'V': 22, 'W': 23,'X': 24, 'Y': 25,'Z': 26}

        col_numb = 0
        col_len = len(columnTitle)

        for index, char in enumerate(columnTitle, start=1):
            reverse_index = col_len - index
            current_val = (26 ** reverse_index) * alphabet[char]
            col_numb = col_numb + current_val

            # print reverse_index , char , alphabet[char], current_val, col_numb

        # single_digit = alphabet[columnTitle[col_len-1]]
        # col_numb = col_numb + single_digit

        # print "columnTitle is: ", columnTitle
        # print "Last digit is: ", columnTitle[col_len-1]
        # print "Last digit value is: ", single_digit
        
        return col_numb
    
