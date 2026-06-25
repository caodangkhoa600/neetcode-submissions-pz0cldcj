class Solution:
    def calculate(self, s1, s2, ope):
        v2 = int(s1)
        v1 = int(s2)
        if ope == '*':
            return v1 * v2
        
        if ope == '+':
            return v1 + v2
        
        if ope == '-':
            return v1 - v2
        
        if ope == '/':
            return int(v1 / v2)

    def evalRPN(self, tokens: List[str]) -> int:
        n = []
        for i in tokens:
            if i == '*' or i == '+' or i == '/' or i == '-':
                n1 = n.pop()
                n2 = n.pop()

                n.append(self.calculate(n1, n2, i))
            else:
                n.append(i)

        return int(n.pop())