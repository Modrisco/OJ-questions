class Solution {
    public int tribonacci(int n) {
        int[] dp = new int[n+1];
        if (n == 0) {
            return 0;
        } else if (n <= 2) {
            return 1;
        } else {
            dp[1] = 1;
            dp[2] = 1;
            for (int i=3; i<n+1; i++) {
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
            }
        }
        return dp[n];
    }
}