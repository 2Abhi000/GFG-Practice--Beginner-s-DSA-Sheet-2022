#Bitonic Point
from heapq import heappop, heappush, heapify
heap = []
heapify(heap)
heappush(heap, -1 * 1)
heappush(heap, -1 * 45)
heappush(heap, -1 * 47)
heappush(heap, -1 * 50)
heappush(heap, -1 * 5)
print(str(-1 * heap[0]))
