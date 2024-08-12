class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ### Can do better
        ts = Counter(tasks)
        maxh = [-cnt for cnt in ts.values()]
        heapq.heapify(maxh)


        time = 0
        q = collections.deque()
        while maxh or q:
            time += 1
            if maxh:
                cnt = 1 + heapq.heappop(maxh)
                if cnt:
                    q.append([cnt, time +n])
            if q and q[0][1] == time:
                heapq.heappush(maxh, q.popleft()[0])
        return time