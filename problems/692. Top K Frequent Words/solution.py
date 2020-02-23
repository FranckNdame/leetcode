class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-frequency, word) for word, frequency in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
