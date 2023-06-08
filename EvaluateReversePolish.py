def evalRPN(tokens):
    values=[]
    for i in range(len(tokens)):
        if tokens[i]=="+":
            first = values.pop()
            second = values.pop()
            values.append(first+second)
        elif tokens[i]=="*":
            first = values.pop()
            second = values.pop()
            values.append(first*second)
        elif tokens[i]=="/":
            first = values.pop()
            second = values.pop()
            values.append(int((second/first)))
        elif tokens[i]=="-":
            first = values.pop()
            second = values.pop()
            values.append(second-first)
        else:
            num = int(tokens[i])
            values.append(num)
    return values[0]

"""
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ["10","6","12","-11","*","/","*","17","+","5","+"]
    ["10","6","-132","/","*","17","+","5","+"]
    ["10","0","*","17","+","5","+"]
    ["0","17","+","5","+"]
    ["17","+","5","+"]
"""
    

print(evalRPN(["2","1","+","3","*"]))