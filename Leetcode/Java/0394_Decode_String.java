class Solution {
    public String decodeString(String s) {
        String res = "";
        int time = 0;
        Stack<String> stackStr = new Stack<>();
        Stack<Integer> stackInt = new Stack<>();
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                time = time * 10 + (c - '0');
            } else if (c == '[') {
                stackInt.push(time);
                time = 0;
                stackStr.push(res);
                res = "";
            } else if (Character.isLetter(c)) {
                res += c;
            } else if (c == ']') {
                time = stackInt.pop();
                StringBuilder temp = new StringBuilder(stackStr.pop());
                // res = stringMultiply(temp.toString(), time);
                for (int j=0; j<time; j++) {
                    temp.append(res);
                }
                res = temp.toString();
                time = 0;
            }
        }
        // StringBuilder sb = new StringBuilder();
        // while (!stackChar.isEmpty()) {
        //     sb.append(stackChar.pop());
        // }
        // sb = sb.reverse();
        // res += sb.toString();
        return res;
    }

    public static String stringMultiply(String s, int n) {
        String res = "";
        for (int i=0; i<n; i++) {
            res += s;
        }
        return res;
    }
}