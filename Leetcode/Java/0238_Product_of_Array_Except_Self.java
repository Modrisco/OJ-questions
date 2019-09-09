class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prod = 1;
        int[] product = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            product[i] = prod;
            prod = prod * nums[i];
        }
        prod = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            product[i] = product[i] * prod;
            prod = prod * nums[i];
        }
        return product;
    }
}