#https://leetcode.com/problems/length-of-last-word/submissions/
#Length of Last Word
class Solution():
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(' ')[-1])
    s="DEVA KUMAR"
    print(lengthOfLastWord(s))
