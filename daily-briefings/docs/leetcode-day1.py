import math

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        # Char in s
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1

        retval = 1
        for c, num_occured in d.items():
            # Even nubmer
            if num_occured % 2 == 0:
                retval += num_occured
            # Odd number
            else:
                retval += num_occured - 1

        return retval


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
