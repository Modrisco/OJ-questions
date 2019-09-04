class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (stack.size() == 0 && (c == ')' || c == ']' || c == '}')) {
                return false;
            }
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.peek() == '(') {
                    stack.pop();
                } else {
                    return false;
                }
            } else if (c == ']') {
                if (stack.peek() == '[') {
                    stack.pop();
                } else {
                    return false;
                }
            } else if (c == '}') {
                if (stack.peek() == '{') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        if (stack.size() == 0) {
            return true;
        } else {
            return false;
        }
    }
}