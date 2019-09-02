class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int start = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (map.containsKey(chars[i])) {
                start = Math.max(start, map.get(chars[i]));
            }
            res = Math.max(i - start + 1, res);
            map.put(chars[i], i+1);
        }
        return res;
    }
}