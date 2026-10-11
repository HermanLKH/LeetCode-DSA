# Time complexity:  O(N), N = a + b + c
# Space complexity: O(N)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []  # (char counts, char)
        
        # Time complexity: O(1) => O(log 1) + O(log 2) + O(log 3)
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        res = []

        # Time complexity: O(N)
        while heap:
            # Get the char with the most remaining occurrences
            cnt1, ch1 = heapq.heappop(heap)

            # Check if the last 2 char in res = char1
            if len(res) >= 2 and res[-1] == ch1 and res[-2] == ch1:
                # No valid char left to append, stop
                if not heap:
                    break
                
                # Time complexity: O(log 2)
                # Take the next frequent char
                cnt2, ch2 = heapq.heappop(heap)

                res.append(ch2)
                cnt2 += 1

                # Time complexity: O(log 2)
                # Push back to heap if char2 still have remaining occurrences
                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                
                # Time complexity: O(log 3)
                # Push the char1 back into the heap
                heapq.heappush(heap, (cnt1, ch1))

            else:
                # Can append char1
                res.append(ch1)
                cnt1 += 1

                # Push back to heap if char1 still have remaining occurrences
                if cnt1 < 0:
                    heapq.heappush(heap, (cnt1, ch1))

        # Time complexity: O(N)
        return "".join(res)