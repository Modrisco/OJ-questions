class Solution {
    public List<List<Integer>> subsets_bit(int[] nums) {
        // Time complexity: O(n * 2^n)
        // Space complexity: O(1)
        List<List<Integer>> ans = new ArrayList<>();
        int len = nums.length;
        // from 0 to 2^len - 1
        // e.g 3 digits: 000 -> 111
        for (int i=0; i<1<<len; i++) {
            List<Integer> cur = new ArrayList<>();
            for (int j=0; j<len; j++) {
                // System.out.println(i);
                if ((i & (1<<j)) > 0) {
                    cur.add(nums[j]);
                }
            }
            // System.out.println(cur);
            ans.add(cur);
        }
        return ans;
    }
    public List<List<Integer>> subsets_dfs(int[] nums) {
        // Time complexity: O(n * 2^n)
        // Space complexity: O(n)
    }
}