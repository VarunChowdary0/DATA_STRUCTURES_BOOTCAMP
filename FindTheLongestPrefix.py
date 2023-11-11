def FindTheLongestPrefix(StringArr):
    Counter ={}
    ans =''
    for ind in range(len(StringArr)):
        if ind+1 != len(StringArr):
            for ch in range(len(min(StringArr[ind],StringArr[ind+1]))):
                if StringArr[ind][ch] == StringArr[ind+1][ch]:
                    if StringArr[ind][ch] in Counter.keys():
                        Counter[StringArr[ind][ch]] += 1
                    else:
                        Counter[StringArr[ind][ch]] = 1
                else:
                    break
    The_pre = (max(Counter.values()))
    for x in Counter.keys():
        if Counter[x] == The_pre:
            ans += x
    return ans
StrArr = ['flower','flow','flowing','flaws']
print(FindTheLongestPrefix(StrArr))