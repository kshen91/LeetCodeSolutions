from collections import deque

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = deque(s)
        s.append('+')
        
        def calculateQueue(queue):
            ans, num = 0, 0
            queue.appendleft('+')
            sign = ''
        
            stack = []

            while len(s) != 0:
                ch = queue.popleft()
                if ch.isdigit():
                    num = num * 10 + int(ch)
                else:
                    if ch == ' ':
                        continue
                    
                    if ch == '(':
                        num = calculateQueue(queue)

                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack[-1] *= num
                    if sign == '/':
                        stack[-1] /= num
                    
                    if ch == ')':
                        break

                    num = 0
                    sign = ch

            return sum(stack)
        
        return calculateQueue(s)
