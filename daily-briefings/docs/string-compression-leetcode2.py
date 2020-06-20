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
        retval = ""
        length = len(s)
        i = 0
        while i < length:
            j = i
            while j < length and s[j] == s[i]:
                j += 1
            retval += s[i] + str(j-i)
            i = j

        if len(retval) > length:
            return s

        return retval


if __name__ == "__main__":
    c = Compression()
    s1 = "aabcccccaaa"
    assert c.compress(s1) == "a2b1c5a3"
    s2 = "abbccd"
    assert c.compress(s2) == "abbccd"
