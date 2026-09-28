class Solution:
    def carFleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        cars = sorted(zip(positions, speeds))
        st = []

        for pos, spd in cars:
            time = (target - pos) / spd

            while st and st[-1] <= time:
                st.pop()
            
            st.append(time)
        
        return len(st)