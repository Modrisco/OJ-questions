class Solution {
    public int[] countBits_naive(int num) {
        int[] result = new int[num+1];
        int i = 0;
        while (i<=num) {
            int one = 0;
            String bin = Integer.toString(i, 2);
            for (int j=0; j<bin.length(); j++) {
                if (bin.charAt(j) == '1') {
                    one++;
                }
            }
            result[i] = one;
            i++;
        }
        return result;
    }

    public int[] countBits_dp(int num) {
        int[] result = new int[num+1];
        for (int i=1; i<=num; i++) {
            result[i] = result[i/2];
            if (i % 2 == 1) {
                result[i]++;
            }
        }
        return result;
    }
}
