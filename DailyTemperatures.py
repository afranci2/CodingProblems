def dailyTemperatures(temperatures):
    new_list = [73,76,72,69,71,75,74,73]
    ans = []
    for i in range(len(temperatures)):
        print(new_list)
        first = new_list[len(temperatures)]
        second = new_list[len(temperatures)-1]
        print(new_list)
        while first > second and new_list:
            j=0
            ans.append(j)
            new_list.pop()
            j=j+1
        ans.append(0)
    return ans


print(dailyTemperatures([73,74,75,71,69,72,76]))