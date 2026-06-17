class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                prev1 = record[-1]
                prev2 = record[-2]
                record.append(prev1+prev2)
            elif op == "D":
                prev1 = record[-1]
                record.append(prev1*2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)