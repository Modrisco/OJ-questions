/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    List<Integer> list = new LinkedList<>();
    public List<Integer> postorder_recursive(Node root) {
        if (root == null) {
            return list;
        } if (root.children != null) {
            for (Node child: root.children) {
                postorder(child);
            }
        }
        list.add(root.val);

        return list;
    }

    public List<Integer> postorder_non_recursive(Node root) {
        List<Integer> list = new LinkedList<>();
        Stack<Node> stack = new Stack<>();
        if (root == null) {
            return list;
        }
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            for (Node child: node.children) {
                stack.push(child);
            }
            list.add(node.val);
        }
        Collections.reverse(list);
        return list;
    }
}