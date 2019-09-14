class Solution {
    public int longestPalindrome_greedy(String s) {
        int len = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c: s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for (Character c: map.keySet()) {
            if (map.get(c) >= 2) {
                int j = map.get(c) / 2;
                len += j * 2;
                map.put(c, map.get(c) - j * 2);
            }
        }
        for (Character c: map.keySet()) {
            if (map.get(c) == 1) {
                len++;
                break;
            }
        }
        return len;
    }

    public int longestPalindrome_best(String s) {
        int[] freqs = new int[128];
        int ans = 0;
        int add = 0;
        for (char c: s.toCharArray()) {
            freqs[c]++;
        }
        for (int freq: freqs) {
            ans += freq / 2 * 2;

            if (freq % 2 != 0) {
                add = 1;
            }
        }
        ans += add;
        return ans;
    }
}