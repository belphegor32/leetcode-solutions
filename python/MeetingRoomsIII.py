from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = []
        avail = [i for i in range(n)]

        cnt = [0] * n

        # sort the meetings by starting time
        meetings.sort(key=lambda x: x[0])

        for st, end in meetings:
            while busy and busy[0][0] <= st:
                # if the meeting is finished, we get rid of the meeting
                meeting_end, room_numb = heapq.heappop(busy)
                heapq.heappush(avail, room_numb)
            
            if avail:
                # if there is an available room, we occupy the room
                room_numb = heapq.heappop(avail)
                heapq.heappush(busy, (end, room_numb))
            else:
                # else, we put the meeting on wait
                t, room_numb = heapq.heappop(busy)
                heapq.heappush(busy, (t + end - st, room_numb))

            cnt[room_numb] += 1

        # get the first room with max meetings
        maxCnt = max(cnt)
        for i in range(len(cnt)):
            if cnt[i] == maxCnt:
                return i