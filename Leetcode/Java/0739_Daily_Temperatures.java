class Solution {
    public int[] dailyTemperatures_naive(int[] T) {
        int[] res = new int[T.length];
        for (int i=0; i<T.length-1; i++) {
            for (int j=i+1; j<T.length; j++) {
                if (T[j] > T[i]) {
                    res[i] = j-i;
                    break;
                }
            }
        }
        return res;
    }

    public int[] dailyTemperatures_stack(int[] T) {
        int[] res = new int[T.length];
        Stack<Integer> stack = new Stack<Integer>();
        for (int i=0; i<T.length; i++) {
            // push each index into the stack, if the temperatures at the peek day of the stack
            // is smaller than the day now, just need to calculate the difference between two days
            // otherwise wait until we pop it out
            while (!stack.isEmpty() && T[stack.peek()] < T[i]) {
                int index = stack.pop();
                res[index] = i-index;
            }
            stack.push(i);
            // all elements in stack are the days always getting colder
        }
        // after for loop, left elements are still 0
        return res;
    }
}