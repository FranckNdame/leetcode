import heapq
heap = []
heapq.heappush(heap, (1, "lzve"))
heapq.heappush(heap, (1, "love"))
heapq.heappush(heap, (1, "i"))

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
