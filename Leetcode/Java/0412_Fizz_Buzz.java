class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<>();
        for (int i=1; i<n+1; i++) {
            if (i % 15 == 0) {
                res.add("FizzBuzz");
            } else if (i % 5 == 0) {
                res.add("Buzz");
            } else if (i % 3 == 0) {
                res.add("Fizz");
            } else {
                res.add(Integer.toString(i));
            }
        }
        return res;
    }
}


import java.util.Scanner;
        import java.util.ArrayList;

public class Main {
    public static int maxSum(int[] arr) {
        int[] dp = new int[arr.length];
        dp[0] = arr[0];
        int max = arr[0];
        for (int i=0; i<arr.length; i++) {
            dp[i] = (dp[i-1] > 0) ? dp[i-1]+arr[i] : arr[i];
            max = Math.max(max, dp[i]);
        }
        return max;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int len = scanner.nextInt();
        System.out.println(len);
        int[] nums = new int[len];
        int index = 0;
        while (scanner.hasNextInt()) {
            nums[index] = scanner.nextInt();
            index++;
        }
        int result = maxSum(nums);
        //System.out.println(result);
    }
}