class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // sort by two keys: int[x][y] --> first value of x, then value of y
        Arrays.sort(people, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] == o2[0] ? o1[1] - o2[1] : o2[0] - o1[0];
            }
        });
        // insert each int[] to a linkedlist, according to int[x][y] --> value of y
        List<int[]> res = new LinkedList<>();
        for (int[] ints : people) {
            res.add(ints[1], ints);
        }
        return res.toArray(new int[people.length][]);
        return people;
    }
}