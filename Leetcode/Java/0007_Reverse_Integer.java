class Solution {
    public int reverse(int x) {
        int sign = (x >= 0) ? 1 : -1;
        x = Math.abs(x);
        int res = 0;
        while (x != 0) {
            int t = x % 10;
            int temp = res * 10 + t;
            if ((temp - t) / 10 !=  res) {
                return 0;
            }
            x = x / 10;
            res = temp;
        }
        return res * sign;
    }
}