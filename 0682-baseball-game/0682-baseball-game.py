class Solution:
    def calPoints(self, operations: list[str]) -> int:
        l = []
        for i in operations:
            if i.lstrip('-').isdigit():
                l.append(int(i))
            elif i == '+':
                r = l[-1]+l[-2]
                l.append(r)
            elif i == 'D':
                r1 = 2*l[-1]
                l.append(r1)
            elif i == 'C':
                r2 = l.pop(-1)
        return sum(l)


        