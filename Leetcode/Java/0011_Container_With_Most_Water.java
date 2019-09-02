// Two pointers
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max = 0;
        while (right > left) {
            int volume = Math.min(height[left], height[right]) * (right - left);
            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
            max = Math.max(max, volume);
        }
        return max;
    }
}