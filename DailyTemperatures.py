def dailyTemperatures(temperatures):
    ans = [0]*len(temperatures)
    stack = []
    j=1
    for i in range(len(temperatures)):
        print("hey")
        print("ans:", ans)
        print("stack:",stack)
        print("i:", i)
        print("this is current temp:", temperatures[i])

        while stack and temperatures[i]<stack[-1]:
            print(temperatures[i], stack[-1])
            print("j:", j)
            print("ans:", ans)
            print("stack:",stack)
            stack.pop()
            j=j+1
        ans[i-1] = j
        j=1
        
        stack.append(temperatures[i])
    return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))


expect = [1,0,0,2,1,0,0,0,0,0]
