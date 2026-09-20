class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result = []

        for asteroid in asteroids:
            if asteroid > 0:
                result.append(asteroid)
            else:
                curr_asteroid = abs(asteroid)
                
                while result:
                    next_asteroid = result[-1]

                    if next_asteroid > 0:
                        if curr_asteroid > next_asteroid:
                            result.pop()
                        elif curr_asteroid < next_asteroid:
                            break
                        else:
                            result.pop()
                            break
                    else:
                        result.append(asteroid)
                        break
                else:
                    result.append(asteroid)

        return result
