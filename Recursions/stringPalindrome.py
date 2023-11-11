def IsPalindrome(string):
    if len(string)==(1 or 0) :
        return True
    if string[0] != string[-1]:
        return False
    return IsPalindrome(string[1:len(string)-1])
str = input(">> ")
print(IsPalindrome(str))