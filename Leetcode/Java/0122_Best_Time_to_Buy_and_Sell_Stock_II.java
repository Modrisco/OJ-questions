class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int gain = 0;
        int[] gains = new int[prices.length - 1];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - prices[i - 1] > 0) {
                gain += prices[i] - prices[i - 1];
            }
        }
        return gain;
    }
}