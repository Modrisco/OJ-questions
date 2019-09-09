class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        HashSet<List<Integer>> set = new HashSet<>();
        HashMap<Integer, ArrayList<int[]>> map = new HashMap<>();
        Arrays.sort(nums);
        int right = nums.length - 1;
        if (nums.length < 3 || nums[right] < 0) {
            return res;
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= 0) {
                int target = Math.abs(nums[i]);
                int l = i + 1;
                int r = right;
                while (l < r) {
                    int sum = nums[l] + nums[r];
                    if (sum == target) {
                        ArrayList<int[]> list = new ArrayList<>();
                        if (map.containsKey(nums[i])) {
                            list = map.get(nums[i]);
                            list.add(new int[]{nums[l], nums[r]});
                        } else {
                            list.add(new int[]{nums[l], nums[r]});
                        }
                        map.put(nums[i], list);
                        l += 1;
                    } else if (sum < target) {
                        l += 1;
                    } else if (sum > target) {
                        r -= 1;
                    }
                }
            }
        }
        for (Integer i: map.keySet()) {
            ArrayList<int[]> arrayList = map.get(i);
            for (int j = 0; j < arrayList.size(); j++) {
                int[] two = arrayList.get(j);
                List<Integer> list = Arrays.asList(i, two[0], two[1]);
                set.add(list);
            }
        }
        for (List list: set) {
            res.add(list);
        }
        return res;
    }

    public List<List<Integer>> threeSum_best(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        if (nums.length < 3 || nums[nums.length - 1] < 0) {
            return res;
        }
        for (int i = 0; i < nums.length - 2; i++) {
            // [-3, -1, -1, 0, 1, 2] --> skip the second '-1'
            if ((i > 0 && nums[i] == nums[i - 1]) || nums[i] > 0) {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            int target = Math.abs(nums[i]);
            while (left < right) {
                if (nums[left] + nums[right] == target) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while (left < right && nums[left - 1] == nums[left]) {
                        left++;
                    }
                    while (left < right && nums[right + 1] == nums[right]) {
                        right--;
                    }
                } else if (nums[left] + nums[right] < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return res;
    }
}