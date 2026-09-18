class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        total_scores = 0

        for ops in operations:
            if ops == '+':
                score = scores[-1] + scores[-2]
            elif ops == 'D':
                score = scores[-1] * 2
            elif ops == 'C':
                total_scores -= scores.pop()
                continue
            else:
                score = int(ops)

            scores.append(score)
            total_scores += score
        
        return total_scores
