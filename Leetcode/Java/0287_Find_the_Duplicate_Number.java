class Solution {
    // https://blog.csdn.net/wr339988/article/details/53617914
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }
        fast = 0;
        while (fast != slow) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }


    public int findDuplicate_BinarySearch(int[] nums) {
        int n = nums.length - 1;
        int low = 1;
        int high = n;
        int mid;
        while (low < high) {
            mid = (low + high) / 2;
            int count = 0;
            for (int num: nums) {
                if (num <= mid) {
                    count++;
                }
            }
            if (count > mid) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}