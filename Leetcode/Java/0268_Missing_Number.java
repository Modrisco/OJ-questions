class Solution {
    public int missingNumber_xor(int[] nums) {
        int miss = 0;
        // each number show twice, a ^ a = 0
        for (int i=0; i<nums.length; i++) {
            miss = miss ^ (i+1) ^ nums[i];
        }
        return miss;
    }

    public int missingNumber(int[] nums) {
        int sum = nums.length * (nums.length + 1) / 2;
        for (int num: nums) {
            sum -= num;
        }
        return sum;
    }
}
