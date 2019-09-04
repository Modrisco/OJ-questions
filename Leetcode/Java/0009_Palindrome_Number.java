class Solution {
    public boolean isPalindrome(int x) {
        int origin = x;
        if (x < 0) {
            return false;
        }
        int reversed = 0;
        while (x != 0) {
            int t = x % 10;
            reversed = reversed * 10 + t;
            x = x / 10;
        }
        if (origin == reversed) {
            return true;
        } else {
            return false;
        }
    }
}