class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) {
            return 0;
        }
        int[] gains = new int[prices.length-1];
        int[] dp = new int[gains.length];
        for (int i = 0; i < gains.length; i++) {
            gains[i] = prices[i+1] - prices[i];
        }
        dp[0] = gains[0];
        if (dp.length == 1 && dp[0] > 0) {
            return dp[0];
        }
        int max = dp[0];
        for (int i = 1; i < gains.length; i++) {
            dp[i] = (dp[i-1] > 0) ? dp[i-1] + gains[i] : gains[i];
            max = Math.max(dp[i], max);
        }
        return (max > 0) ? max : 0;
    }
}