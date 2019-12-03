class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        List<String> result = new ArrayList<>();
        for (String word: words) {
            map.put(word, map.getOrDefault(word, 0)+1);
        }
        PriorityQueue<Map.Entry<String, Integer>> queue = new PriorityQueue<>(k, (a, b) -> {
            if (a.getValue() != b.getValue()) {
                return b.getValue() - a.getValue();
            } else {
                return a.getKey().compareTo(b.getKey());
            }
        });
        for (Map.Entry<String, Integer> entry: map.entrySet()) {
            queue.add(entry);
        }
        for (int i = 0; i < k; i++) {
            result.add(queue.poll().getKey());
        }
        return result;
    }
}