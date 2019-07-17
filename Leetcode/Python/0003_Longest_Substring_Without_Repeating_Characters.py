class Solution(object):
    def lengthOfLongestSubstring_bruteforce(self, s):
        """
        :type s: str
        :rtype: int
        """
        # brute force will execute runtime error for the last testcase!
        if not s:
            return 0
        longest = 1
        for i in range(len(s)-1):
            unique = set(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in unique:
                    unique.add(s[j])
                    if len(unique) > longest:
                        longest = len(unique)
                else:
                    break
        return longest
    
    def lengthOfLongestSubstring_slidingarray(self, s):
        if len(s) == 0 or not s:
            return 0
        i, j, res = 0, 0, 0
        seen = set()
        while i < len(s) and j < len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1
            res = max(res, len(seen))
        return res

    # best solution
    def lengthOfLongestSubstring_opt_slidingarray(self, s):
        res, start = 0, 0
        seen = dict()

        for i, x in enumerate(s):
            if x in seen:
                start = max(seen[x], start)
            res = max(i-start+1, res)
            seen[x] = i+1
        return res