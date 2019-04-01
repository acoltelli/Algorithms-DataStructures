from Stack import Stack




def parentheses(str):
	stack = Stack(len(str))
	 
	for i in str:
		if i == '(':
			stack.push(i)
		if i == ')':
			stack.pop()


	if stack
	print stack


parentheses('((()))')
parentheses('(()')