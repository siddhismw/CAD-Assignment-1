
stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return None
    return stack.pop()

def peek():
    if len(stack) == 0:
        return None
    return stack[-1]



# priority function
def priority(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# in to post
def inf_to_postf(exp):
    result = ""
    for ch in exp:
        if ch.isalnum():   # operand
            result += ch
        elif ch == '(':
            push(ch)
        elif ch == ')':
            while peek() != '(':
                result += pop()
            pop()
        else:  # operator
            while stack and priority(ch) <= priority(peek()):
                result += pop()
            push(ch)

    while stack:
        result += pop()

    return result

# postfix
def eval_postf(exp):
    s = []
    for ch in exp:
        if ch.isdigit():
            s.append(int(ch))
        else:
            b = s.pop()
            a = s.pop()
            if ch == '+': s.append(a+b)
            elif ch == '-': s.append(a-b)
            elif ch == '*': s.append(a*b)
            elif ch == '/': s.append(a/b)
    return s[0]

# operations
infix = input("Enter infix expression: ")

postfix = inf_to_postf(infix)
print("Postfix:", postfix)

value = eval_postf(postfix)
print("Evaluation:", value)

