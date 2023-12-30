# 


# Solution 2 (commented, mine) beats ~10. The actual solve beats 90+. I think the idea is that a lot of branches and functions with returns causes delays


#Actually one solve,as all copied solutions are showin bad ttiming as well. Eh







# class Solution:
#     def evalRPN(self, tokens) -> int:
#         self.op_dict = { "*":self.mult, '-':self.sub,"+":self.add,'/':self.div}
#         self.op_stack = []
#         for token in tokens:
#             self.op_dict[token]() if token in self.op_dict else self.op_stack.append(int(token))
#         return self.op_stack.pop()

#     def div(self):
#         b = self.op_stack.pop()
#         a = self.op_stack.pop()
#         self.op_stack.append(int(a/b))

#     def mult(self):
#         b = self.op_stack.pop()
#         a = self.op_stack.pop()
#         self.op_stack.append(int(b*a))
        
#     def add(self):
#         b = self.op_stack.pop()
#         a = self.op_stack.pop()
#         self.op_stack.append(int(b+a))
        
#     def sub(self):
#         b = self.op_stack.pop()
#         a = self.op_stack.pop()
#         self.op_stack.append(int(a-b))
        
