"""
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

Example 2:
Input: "abbccd"
Output: "abbccd"
Explanation: 
The compressed string is "a1b2c2d1", which is longer than the original string.
 
Note:
0 <= S.length <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Compression():

    def compress(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        retval = ""
        # The reason I use while is that the `step` is variable-length,
        # thus a forloop is probably not a good idea.
        # Input: "aabcccccaaa"
        # Output: "a2b1c5a3"
        while i < len(s):
            cur_char = s[i]
            num_occured = 1
            for j in range(0, len(s)-i-1):
                if i+j == len(s):
                    break
                c_next = s[i+j]
                if c_next == cur_char:
                    num_occured += 1
                else:
                    break
            retval += cur_char + str(num_occured)
            i = j+1

        return retval


if __name__ == "__main__":
    c = Compression()
    string1 = 'aabcccccaaa'
    print(c.compress(string1))
