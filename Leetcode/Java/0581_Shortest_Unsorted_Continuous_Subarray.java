class Solution {
    public int findUnsortedSubarray_sortedArray(int[] nums) {
        int[] numsCopy = nums.clone();
        Arrays.sort(numsCopy);
        int start = nums.length;
        int end = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != numsCopy[i]) {
                start = Math.min(i, start);
                end = Math.max(i, end);
            }
        }
        return (end - start >= 0) ? end - start + 1 : 0;
    }

    public int findUnsortedSubarray_stack(int[] nums) {
        if (nums.length <= 1) {
            return 0;
        }
        Stack<Integer> stack = new Stack<>();
        int left = nums.length - 1;
        int right = 0;
        for (int i = 0; i < nums.length; i++) {
            if (stack.isEmpty() || nums[i] >= nums[stack.peek()]) {
                stack.push(i);
            } else {
                left = Math.min(left, stack.pop());
                i--;
            }
        }
        stack.clear();
        for (int i = nums.length - 1; i >= 0; i--) {
            if (stack.isEmpty() || nums[i] <= nums[stack.peek()]) {
                stack.push(i);
            } else {
                right = Math.max(right, stack.pop());
                i++;
            }
        }
        return right - left > 0 ? right - left + 1 : 0;
    }
}