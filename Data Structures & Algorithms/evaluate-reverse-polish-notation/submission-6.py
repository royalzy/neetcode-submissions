class Solution:

    def addition(self,num1, num2):
        return num1 + num2

    def subtract(self,num1,num2):
        return num1 - num2
    
    def multiply(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        pos = 1
        if num1<0:
            pos *= -1
            num1 = abs(num1)
        if num2<0:
            pos *= -1
            num2 = abs(num2)

        return (num1//num2)*pos

    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+","-","*","/"])

        # stack solution
        stack = []

        for char in tokens:
            if char not in ops:
                # char is number
                stack.append(int(char))

            if char in ops:

                operator = char
                num2 = stack.pop()
                num1 = stack.pop()

                if operator == "+":
                    stack.append(self.addition(num1,num2))
                elif operator == "-":
                    stack.append(self.subtract(num1,num2))
                elif operator == "*":
                    stack.append(self.multiply(num1,num2))
                elif operator == "/":
                    stack.append(self.divide(num1,num2))

        return int(stack[0])
                        

